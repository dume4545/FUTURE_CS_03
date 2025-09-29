🔐 Secure File Sharing System
🚀 Cyber Security Task 3 - Future Interns Internship
A professional, secure web application for encrypted file storage and sharing using military-grade AES-256 encryption. Developed as the final task for the Cyber Security Internship at Future Interns, demonstrating real-world security implementation skills.



✨ Features
🔒 Security Features
Military-Grade Encryption: AES-256-CBC encryption for all files

Secure File Upload: Automatic encryption before storage

Protected Downloads: On-the-fly decryption during download

Cryptographic Best Practices: Random IV generation, PKCS7 padding

No Plaintext Storage: Files never stored unencrypted

🎯 User Experience
Beautiful Modern UI: Responsive, professional interface

Real-time Notifications: Success/error messages with animations

File Management: Upload, download, and delete encrypted files

Progress Indicators: Download status notifications

Mobile Responsive: Works perfectly on all devices

🛡️ Security Implementation
AES-256-CBC: NIST-approved encryption standard

Unique IV per File: Prevents pattern analysis attacks

Secure Key Management: Proper key handling practices

Input Validation: File type and size restrictions

Error Handling: Secure error messages without information leakage

📸 Screenshots
(Add your screenshots here)

Main Interface: Clean, professional file management dashboard

Upload Process: Secure file encryption with success confirmation

Download Flow: Real-time decryption with progress indicators

🛠️ Installation
Prerequisites
Python 3.7 or higher

pip package manager

Quick Start
Clone the repository

bash
git clone https://github.com/yourusername/secure-file-sharing.git
cd secure-file-sharing
Create virtual environment (recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python app.py
Access the application
Open your browser and navigate to http://localhost:5000


🔧 Usage Guide
📤 Uploading Files
Click "Choose File" and select your file

Click "🔒 Encrypt & Upload"

Receive instant success confirmation

File is automatically encrypted with AES-256 before storage

📥 Downloading Files
Click "🔓 Download & Decrypt" next to any file

Watch the download progress notification

File is decrypted on-the-fly during download

Download starts automatically

🗑️ Managing Files
Delete: Remove encrypted files permanently

View: See all your encrypted files in a clean list

Security: All operations are cryptographically secured

🔐 Security Architecture
Encryption Process
python
# File Upload
file_data → Generate Random IV → AES-256-CBC Encryption → Store IV + Encrypted Data

# File Download
encrypted_data → Extract IV → AES-256-CBC Decryption → Serve Decrypted File
Key Features
AES-256-CBC: Military-grade encryption standard

Random IV: Unique initialization vector for each file

PKCS7 Padding: Standards-compliant padding scheme

Secure Storage: No plaintext files on server
