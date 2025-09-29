import os
import secrets
import base64
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import io

app = Flask(__name__)
app.secret_key = 'flash-message-secret-key'  # For flash messages

# Generate a secret key (run this once, then save the key)
# Or use this default key for testing (change in production!)
app.config['SECRET_KEY'] = "u-sBWkZf4v7y2C5x8z9AbCdEfGhJkLmNqRsTuVwXyZ0123456789abc="
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def get_encryption_key():
    """Convert base64 key to bytes for AES encryption"""
    try:
        key_bytes = base64.urlsafe_b64decode(app.config['SECRET_KEY'])
        return key_bytes[:32]  # Use first 32 bytes for AES-256
    except:
        # Fallback if key decoding fails
        return app.config['SECRET_KEY'].encode()[:32].ljust(32, b'0')

def encrypt_file(file_data):
    """Encrypt file data using AES-256-CBC"""
    key = get_encryption_key()
    iv = secrets.token_bytes(16)  # Random initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))
    return iv + encrypted_data  # Prepend IV to encrypted data

def decrypt_file(encrypted_data):
    """Decrypt file data using AES-256-CBC"""
    key = get_encryption_key()
    iv = encrypted_data[:16]  # Extract IV from beginning
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted_data

@app.route('/')
def index():
    """Main page with file upload form"""
    # Get list of uploaded files
    files = []
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            if filename.endswith('.enc'):
                original_name = filename[:-4]  # Remove .enc extension
                files.append(original_name)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and encryption"""
    if 'file' not in request.files:
        flash('❌ No file selected! Please choose a file to upload.', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('❌ No file selected! Please choose a file to upload.', 'error')
        return redirect(url_for('index'))
    
    if file:
        try:
            # Read file data
            file_data = file.read()
            
            # Check file size
            if len(file_data) > app.config['MAX_CONTENT_LENGTH']:
                flash('❌ File too large! Maximum size is 16MB.', 'error')
                return redirect(url_for('index'))
            
            # Encrypt the file
            encrypted_data = encrypt_file(file_data)
            
            # Save encrypted file
            encrypted_filename = file.filename + '.enc'
            encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], encrypted_filename)
            
            with open(encrypted_path, 'wb') as f:
                f.write(encrypted_data)
            
            flash(f'✅ Success! File "{file.filename}" has been encrypted and stored securely.', 'success')
            return redirect(url_for('index'))
        
        except Exception as e:
            flash(f'❌ Error uploading file: {str(e)}', 'error')
            return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    """Handle file download and decryption"""
    encrypted_filename = filename + '.enc'
    encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], encrypted_filename)
    
    if not os.path.exists(encrypted_path):
        flash('❌ File not found!', 'error')
        return redirect(url_for('index'))
    
    try:
        # Read encrypted file
        with open(encrypted_path, 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt the file
        decrypted_data = decrypt_file(encrypted_data)
        
        # Flash success message
        flash(f'📥 Downloading "{filename}"... File is being decrypted and downloaded.', 'info')
        
        # Send decrypted file to user
        return send_file(
            io.BytesIO(decrypted_data),
            as_attachment=True,
            download_name=filename,
            mimetype='application/octet-stream'
        )
    
    except Exception as e:
        flash(f'❌ Error decrypting file: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/delete/<filename>')
def delete_file(filename):
    """Delete an encrypted file"""
    encrypted_filename = filename + '.enc'
    encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], encrypted_filename)
    
    if os.path.exists(encrypted_path):
        os.remove(encrypted_path)
        flash(f'🗑️ File "{filename}" has been permanently deleted.', 'success')
    else:
        flash('❌ File not found!', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)