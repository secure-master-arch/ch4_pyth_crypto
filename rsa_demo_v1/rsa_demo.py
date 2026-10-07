from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import rsa

print("=== 1. generaziya klyuchei RSA ===")

private_key = rsa.generate_private_key(
    public_exponent=65537, 
    key_size=3072 ,
    backend=default_backend(), 
                                       )
print("[+] Zakritij kluych uspesho sgenerirovan v operativnoj pamyati.")

public_key = private_key.public_key() 

print("[+] Zakritij klyuch uspesho sgenerirovan v operativnoj pamyati.")

public_key = private_key.public_key() 
print("[+] Otkritij kluch uspeshno izvlechen iz zakritogo.")

print("\n=== 2. SOHRANENIE KLYUCHEJ NA DISK (Listing 5.2) ===")

private_bytes = private_key.private_bytes( 
                                          
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8, 
    encryption_algorithm=serialization.NoEncryption(), 
) 

try:
   with open('private_key.pem', 'xb') as private_file: 
        private_file.write(private_bytes)
   print("[+] Fail 'private_key.pem' uspeshno sozdan i zapisan.")
except FileExistsError:
   print("[-] Fail 'private_key.pem' uge suchestvuet (propuskaem zapis).")
   
public_bytes = public_key.public_bytes( 
    encoding=serialization.Encoding.PEM, 
    format=serialization.PublicFormat.SubjectPublicKeyInfo, 
)
  
try: 
    with open('public_key.pem', 'xb') as public_file:
        public_file.write(public_bytes)
    print("[+] Fail 'public_key.pem' uspeshno sozdan i zapisn.")
except FileExistsError: 
    print("[-] Fail 'public_key.pem' uge suchestvuet (propuskaem zapis).")
    
print("\n=== 3. VISUALNIJ OSMOTR FIZICHESKIH FAILOV KLUCHEJ ===")

print("\n--- Sodergimoe private_key.pem (pervie 4 stroki) ---")

with open('private_key.pem', 'r') as f:
    lines = [f.readline() for _ in range(4)]
    print("".join(lines) + "...\n[Skrito dlya kompaktnosti] ...\n-----END PRIVATE KEY------")
    
print("\n--- Sodergimoe public_key.pem (polonstyu) ---")
with open('public_key.pem', 'r') as f: 
    print(f.read())
    
    
print("=== 4. CHTENIE KLYUCHEJ OBRATNO IZ FAILOV (Listing 5.3) ===")

with open('private_key.pem', 'rb') as private_file: 
    loaded_private_key = serialization.load_pem_private_key(
        private_file.read(), 
        password=None, 
        backend=default_backend()
    )
    
print("[+] Zakritij kluch uspeshno zagrugen iz faila private_key.pem v zapis.")

with open('public_key.pem', 'rb') as public_file: 
    loaded_public_key = serialization.load_pem_public_key(
        public_file.read(), 
        backend=default_backend()
    )
    
print("[+] Otkritij kluych uspeshno zagrugen iz faila public_key.pem v pamyat.")

print("\n[USPEH] Ves zikl sozdaniya, sohraneniya, vizualizazii i chteniya klyuchej zavershen!")