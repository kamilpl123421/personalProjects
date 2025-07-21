import time

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def hello():
    while True:
        for letter in alphabet:
            time.sleep(0.05)
            print(letter)
            if letter == "h":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"h{letter}")
            if letter == "e":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"he{letter}")
            if letter == "l":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"hel{letter}")
            if letter == "l":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"hell{letter}")
            if letter == "o":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"hello {letter}")
            if letter == "w":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"hello w{letter}")
            if letter == "o":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"hello wo{letter}")
            if letter == "r":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"hello wor{letter}")
            if letter == "l":
                break
        for letter in alphabet:
            time.sleep(0.05)
            print(f"hello worl{letter}")
            if letter == "d":
                break
        break

while True:
    choice = input("Wanna see a fancy hello world animation? (yes/no): ").lower()
    if choice == "yes":
        hello()
        break
    elif choice == "no":
        print("Fuck you then")
        break
    else:
        print("Just say yes or no retard")