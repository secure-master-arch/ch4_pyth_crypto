import secrets 
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms , modes
)

key = b'key must be 128, 196 or 256 bits'

def encrypt(data):
    
    iv = secrets.token_bytes(16)
    
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    
    encryptor = cipher.encryptor()
    
    return iv, encryptor.update(data) + encryptor.finalize()

plaintext = b'block size = 128'

iv_1, ciphertext_1 = encrypt(plaintext)
iv_2, ciphertext_2 = encrypt(plaintext)

print("IV 1:", iv_1)
print("Shifrotext 1:", ciphertext_1)
print("IV 2:", iv_2)
print("Shifrotext 2:", ciphertext_2)

are_ciphertexts_equqal = (ciphertext_1 == ciphertext_2)
print("Shifrotexti ravni?", are_ciphertexts_equqal)