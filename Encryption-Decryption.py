from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import os

# Check if keys already exist
if os.path.exists('public_key.pem') and os.path.exists('private_key.pem'):
    # Load keys from files
    with open('public_key.pem', 'rb') as f:
        public_pem = f.read()
    public_key = RSA.import_key(public_pem)

    with open('private_key.pem', 'rb') as f:
        private_pem = f.read()
    private_key = RSA.import_key(private_pem)
else:
    # Generate RSA key pair (public and private keys)
    key_pair = RSA.generate(2048)
    public_key = key_pair.publickey()
    private_key = key_pair

    # Export and save the public key in PEM format
    public_pem = public_key.export_key()
    with open('public_key.pem', 'wb') as f:
        f.write(public_pem)
    print('Public Key saved to public_key.pem')

    # Export and save the private key in PEM format
    private_pem = private_key.export_key()
    with open('private_key.pem', 'wb') as f:
        f.write(private_pem)
    print('Private Key saved to private_key.pem')

# Ask the user whether they want to encrypt or decrypt
choice = ''
while (choice.upper()!= 'E' or choice.upper()!= 'D' or choice.upper()!='Q'):
    choice = input('Do you want to (E)ncrypt or (D)ecrypt a message or (Q)uit? ').upper()
    if choice == 'E':
        # Get message input from the user
        message = input('What message would you like to encrypt? ')

        # Encrypt the message using the public key
        encryptor = PKCS1_OAEP.new(public_key)
        encrypted_msg = encryptor.encrypt(message.encode('utf-8'))
        print('\nEncrypted Message')
        print(binascii.hexlify(encrypted_msg))

        # Optionally, save the encrypted message to a file
        with open('encrypted_message.bin', 'wb') as f:
            f.write(encrypted_msg)

    elif choice == 'D':
        # Optionally, read the encrypted message from a file
        # with open('encrypted_message.bin', 'rb') as f:
        #     encrypted_msg = f.read()

        # Or get the encrypted message from the user
        hex_encrypted_msg = input('Enter the encrypted message in hex format: ')
        encrypted_msg = binascii.unhexlify(hex_encrypted_msg)

        # Decrypt the message using the private key
        decryptor = PKCS1_OAEP.new(private_key)
        try:
            decrypted_msg = decryptor.decrypt(encrypted_msg)
            print('\nDecrypted Message')
            print(decrypted_msg.decode('utf-8'))
        except ValueError as e:
            print("Decryption failed:", e)
    elif choice == 'Q':
        break
    else:
        print('Invalid choice. Please enter "E" to encrypt, "D" to decrypt, or "Q" to quit')
