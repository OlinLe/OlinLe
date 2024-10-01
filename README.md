# RSA Encryption and Decryption Tool

This is a simple Python program that demonstrates RSA encryption and decryption using the `PyCryptodome` library. The tool allows you to generate RSA keys, encrypt messages, and decrypt them back to their original form.

## Features

- **Key Generation**: Generates RSA public and private keys.
- **Encryption**: Encrypts messages using the RSA public key.
- **Decryption**: Decrypts messages using the RSA private key.
- **Key Storage**: Saves generated keys to files for reuse.
- **User Interaction**: Prompts user for messages and choices between encryption and decryption.

## Prerequisites

- **Python 3.6 or higher**

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo.git
Navigate to the project directory

bash
Copy code
cd your-repo
Create and activate a virtual environment (optional but recommended)

On Windows

bash
Copy code
python -m venv venv
venv\Scripts\activate
On macOS/Linux

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required packages

bash
Copy code
pip install -r requirements.txt
Usage
Run the encryption-decryption.py script to start the tool.

bash
Copy code
python encryption-decryption.py
Encrypting a Message
Choose to encrypt a message when prompted.

mathematica
Copy code
Do you want to (E)ncrypt or (D)ecrypt a message? E
Enter the message you wish to encrypt.

vbnet
Copy code
What message would you like to encrypt? Hello, World!
The tool will display the encrypted message in hexadecimal format.

bash
Copy code
Encrypted Message
b'...'
Decrypting a Message
Choose to decrypt a message when prompted.

mathematica
Copy code
Do you want to (E)ncrypt or (D)ecrypt a message? D
Enter the encrypted message in hexadecimal format.

perl
Copy code
Enter the encrypted message in hex format: ...
The tool will display the decrypted message.

mathematica
Copy code
Decrypted Message
Hello, World!
Key Management
Public Key (public_key.pem)

The public key is saved to public_key.pem.
Share this key with anyone who needs to encrypt messages to you.
Private Key (private_key.pem)

Important: Do not share your private key.
The private key is saved to private_key.pem and is used to decrypt messages.
Security Considerations
Protect Your Private Key

Keep your private_key.pem file secure.
Do not share it or commit it to version control systems like GitHub.
Use Secure Channels

When sharing your public key, use secure methods to prevent tampering.
Dependencies
PyCryptodome

Provides cryptographic functions for key generation, encryption, and decryption.
Installed via requirements.txt.
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

Acknowledgments
PyCryptodome: https://www.pycryptodome.org/
