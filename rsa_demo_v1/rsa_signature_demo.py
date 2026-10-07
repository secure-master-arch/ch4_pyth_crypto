
import json 
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import hashes, serialization 
from cryptography.hazmat.primitives.asymmetric import padding 

print("=== DEMOSTRAZIYA ZIFROVOJ PODPISI RSA-PSS (Lisitngi 5.5 и 5.6) ===\n")

print("[1] Zagruzaka kryptograficheskih klyuchej iz failof...")

try: 
    with open("private_key.pem", "rb") as f: 
        private_key = serialization.load_pem_private_key( 
            f.read(), password=None, backend=default_backend()
                                                           )
    print(" --> Zakritij klyuch (dlya Boba) uspeshno zagrugen.")
    
    with open("public_key.pem", "rb") as f: 
        public_key = serialization.load_pem_public_key(
            f.read(), backend=default_backend()
        )
except FileNotFoundError: 
    print("[-] Oshibka: faili klyuchej ne naideni! Snachala sgenerirujte kluch.")
    exit(1)
    
print("--- [SHAG BOBA]  Podpisanie soobcheniya ---")

message = b"from Bob to Alice"
print(f" Ishodnoe soobcheniye (baiti): {message}")

padding_config = padding.PSS( 
                             mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH 
                             )
signature = private_key.sign(message, padding_config, hashes.SHA256())

print(" Zifrovaya podpis uspeshno sozdana!")
print( 
      f" Fizicheskoe predstavlenie podpisi (pervie 60 bait):"
      f" {signature[:60]}...\n"
      )

signed_msg= {"message": list(message), "signature": list(signature)}
outbound_msg_to_alice = json.dumps(signed_msg)
print( 
      " (Set) Soobchenie i podpis upakovani v JSON-paket dlinoj"
      f" {len(outbound_msg_to_alice)} bait.\n"
      )
print("--- [SHAG ALISI] Poluchenie i proverka podpisi ---")

incoming_data = json.loads(outbound_msg_to_alice)
received_message = bytes(incoming_data["message"])
received_signature = bytes(incoming_data["signature"])

print((f" Alica poluchila soobchenie: {received_message}"))
print( 
      f" Alisa poluchila zifrovuyu podpis (pervie 60 bait)"
      f" {received_signature[:60]}..."
      )
print( 
      "\n Alisa vipolnyaet proverku podpisi s pomochuy otkritogo klyucha Boba..."
      )
print(" (Shag 1: vichislenie hesha soobcheniya)")
print(" (Shag 2: rashifrovka podpisi okritim klyuchom)")
print(" (Shag 3: sravnenie heshej)")

try: 
    public_key.verify(
        received_signature, 
        received_message,
        padding_config,
        hashes.SHA256(),
    )
    
    print( 
      "\n[USPEH] Podpis PODLINNAYA! Alisa moget bit uverena v dvuh vechah:"
      )
    print( 
      "  1. Soobcheniyu deistvitelno otpravil vladelez zakritogo klyucha (Bob)."
      )
    print(" 2. Soobchenij ne podverglos izmeneniem v prozese peredachi.")
    
except Exception as e:
    print(f"\n[OSHIBKA] Podpis NEDEISTVITELNA! Soobchenie poddelnoe ili provereno.")
    print(f"Detali isklyucheniya: {e}")










