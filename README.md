# 🔐 Secure File Sharing System

## Cyber Security Task 3 - Future Interns

A secure web application for encrypted file storage and sharing using AES-256 encryption. Developed as the final task for the Cyber Security Internship at Future Interns.

## 🚀 Features

- **Military-Grade Encryption**: AES-256-CBC encryption for all files
- **Secure File Upload**: Automatic encryption before storage
- **Protected Downloads**: Decryption on-the-fly during download
- **Beautiful UI**: Modern, responsive web interface
- **File Management**: Upload, download, and delete encrypted files

## 🛡️ Security Implementation

### Encryption Details
- **Algorithm**: AES-256 (Advanced Encryption Standard)
- **Mode**: CBC (Cipher Block Chaining)
- **Key Size**: 256-bit
- **IV Generation**: Cryptographically secure random IV per file
- **Padding**: PKCS7

### Key Features
- Files encrypted before storage (encryption at rest)
- Unique Initialization Vector for each file
- No plaintext file storage
- Secure key management

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip package 
