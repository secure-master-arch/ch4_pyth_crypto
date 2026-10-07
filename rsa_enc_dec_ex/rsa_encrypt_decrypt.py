from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import  hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa 


print("=== 1. GENERAZIYA KLYUCHEI V PAMYATI ===")

private_key = rsa.generate_private_key (
    public_exponent=65537, 
    key_size=3072, 
    backend=default_backend(),
)

public_key = private_key.public_key() 
print("[+] Para klyuchei RSA uspeshno sozdane v operativnoj pamyati.")

print("\n=== 2. NASTROJKA SHEMI DOPOLNENIYA (PADDING) ===")

padding_config = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None 
)
print("[+] Konfiguraziya dopolneniya OAEP uspeshno podgotovlena.")

print("\n=== 3. SHOFROVANIE i RASHIFROVANIE (Listing 5.4) ===")

plaintext = b'message from Alice to Bob'
print(f"Ishodyachij text: {plaintext}") 

ciphertext = public_key.encrypt( 
    plaintext=plaintext,
    padding=padding_config, 
)

print(f"Zashifrovannie dannie (shifrotext v baitah): {ciphertext[:30]}... [obrezano]")

decrypted_by_private_key = private_key.decrypt( 
    ciphertext=ciphertext, 
    padding=padding_config 
)

print(f"Rashifrovannij text: {decrypted_by_private_key}")

assert decrypted_by_private_key == plaintext 

print("\n[USPEH] Proverka proshla uspeshno! Rashifrovannij text polostyu sovpal s originalom.")
