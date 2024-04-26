import random

def main():
    # Generate angka acak antara 1 dan 100
    target_number = random.randint(1, 100)

    # Looping tebakan pemain
    while True:
        # Menerima input dari pemain
        guess = input("Tebak angka (1-100): ")
        
        # Memeriksa validitas input
        if not guess.isdigit() or not (1 <= int(guess) <= 100):
            print("Masukkan angka antara 1 dan 100.")
            continue
        
        guess = int(guess)
        
        # Memeriksa tebakan pemain
        if guess < target_number:
            print("Tebakan terlalu rendah!")
        elif guess > target_number:
            print("Tebakan terlalu tinggi!")
        else:
            print("Selamat, Anda benar!")
            break

    # Menampilkan angka yang benar
    print(f"Angka yang benar adalah: {target_number}")

if __name__ == "__main__":
    main()
