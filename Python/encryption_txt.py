from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from getpass import getpass
import os

def generate_key(password: bytes, salt: bytes) -> bytes:
    """Generiert einen AES-256-Schlüssel aus dem Passwort mit PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

def encrypt_file(input_path: str, output_path: str, password: str):
    """Verschlüsselt eine Datei mit AES-256-CBC."""
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = generate_key(password.encode(), salt)

    with open(input_path, "rb") as f:
        plaintext = f.read()

    # Padding hinzufügen
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Verschlüsseln
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Salt + IV + verschlüsselte Daten speichern
    with open(output_path, "wb") as f:
        f.write(salt + iv + ciphertext)

def decrypt_file(input_path: str, output_path: str, password: str):
    """Entschlüsselt eine Datei mit AES-256-CBC."""
    with open(input_path, "rb") as f:
        data = f.read()
    
    salt, iv, ciphertext = data[:16], data[16:32], data[32:]
    key = generate_key(password.encode(), salt)

    # Entschlüsseln
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Padding entfernen
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

    with open(output_path, "wb") as f:
        f.write(decrypted_data)

def main():
    print("=== AES-256 Dateiverschlüsselung ===")
    
    # Passworteingabe
    password = getpass("Gib ein sicheres Passwort ein: ")
    password_confirm = getpass("Passwort bestätigen: ")
    
    if password != password_confirm:
        print("Fehler: Passwörter stimmen nicht überein!")
        return

    input_file = r"C:\Users\juanc\Documents\Ausbildung_Informatik\1_Praktikum\Praktikum_Daten-_und_Prozessanalyse\Python\wallet.txt"
    encrypted_file = r"C:\Users\juanc\Documents\Ausbildung_Informatik\1_Praktikum\Praktikum_Daten-_und_Prozessanalyse\Python\wallet.enc"
    decrypted_file = r"C:\Users\juanc\Documents\Ausbildung_Informatik\1_Praktikum\Praktikum_Daten-_und_Prozessanalyse\Python\wallet_dec.txt"

    # Verschlüsseln
    encrypt_file(input_file, encrypted_file, password)
    print(f"\n Datei '{input_file}' wurde verschlüsselt als '{encrypted_file}' gespeichert.")

    # Entschlüsseln
    test_password = getpass("\nGib das Passwort zur Entschlüsselung ein: ")
    try:
        decrypt_file(encrypted_file, decrypted_file, test_password)
        print(f"Datei '{encrypted_file}' wurde entschlüsselt als '{decrypted_file}' gespeichert.")
        
        # Überprüfung
        with open(input_file, "rb") as f1, open(decrypted_file, "rb") as f2:
            if f1.read() == f2.read():
                print("Test erfolgreich: Original und entschlüsselte Datei sind identisch!")
            else:
                print("Warnung: Entschlüsselte Datei stimmt nicht mit dem Original überein!")
    except Exception as e:
        print(f"Fehler bei der Entschlüsselung: {str(e)}")
        print("Mögliche Ursachen: Falsches Passwort oder beschädigte Datei.")

if __name__ == "__main__":
    main()