"""
Cài đặt thuật toán AES (Advanced Encryption Standard)
Sinh viên: k235480106062-alt
Môn: An toàn và bảo mật thông tin
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import time

def aes_encrypt(plaintext, key):
    """Mã hóa bằng AES-256-CBC"""
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return iv + ciphertext

def aes_decrypt(ciphertext, key):
    """Giải mã bằng AES-256-CBC"""
    iv = ciphertext[:16]
    encrypted_data = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(encrypted_data)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode('utf-8')

def main():
    print("=" * 60)
    print("CÀI ĐẶT THUẬT TOÁN AES-256-CBC")
    print("Sinh viên: k235480106062-alt")
    print("=" * 60)
    
    # Key 256-bit (32 bytes)
    key = os.urandom(32)
    print(f"\n[+] Key (256-bit): {key.hex()}")
    
    # Plaintext
    plaintext = "Hello World! Đây là bài tập AES của tôi."
    print(f"[+] Plaintext: {plaintext}")
    
    # Mã hóa
    start_time = time.time()
    ciphertext = aes_encrypt(plaintext, key)
    encrypt_time = time.time() - start_time
    print(f"[+] Ciphertext (hex): {ciphertext.hex()}")
    print(f"[+] Thời gian mã hóa: {encrypt_time:.6f} giây")
    
    # Giải mã
    start_time = time.time()
    decrypted_text = aes_decrypt(ciphertext, key)
    decrypt_time = time.time() - start_time
    print(f"[+] Decrypted text: {decrypted_text}")
    print(f"[+] Thời gian giải mã: {decrypt_time:.6f} giây")
    
    # So sánh với RSA
    print("\n" + "=" * 60)
    print("SO SÁNH AES VỚI RSA")
    print("=" * 60)
    print("AES (đối xứng):")
    print("  - Tốc độ mã hóa/giải mã: NHANH")
    print("  - Phù hợp cho dữ liệu lớn")
    print("  - Key size: 128/192/256 bits")
    print("\nRSA (bất đối xứng):")
    print("  - Tốc độ mã hóa/giải mã: CHẬM hơn AES ~1000 lần")
    print("  - Phù hợp cho mã hóa key, chữ ký số")
    print("  - Key size: 2048/4096 bits")
    print("\nKết hợp RSA + AES (Hybrid Cryptosystem):")
    print("  1. Dùng RSA để mã hóa khóa AES")
    print("  2. Dùng AES để mã hóa dữ liệu thực tế")
    print("  3. Kết hợp tốc độ của AES + bảo mật của RSA")

if __name__ == "__main__":
    main()