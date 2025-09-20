import time

# Password to guess
password = "Ec2@"

# Alphabet with lowercase, uppercase, digits, and symbols
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

start = time.time()
tries = 0

# 1 character
for a in alphabet:
    guess = a
    tries += 1
    if guess == password:
        print("Password found:", guess)
        print("Tries:", tries)
        print("Time:", round(time.time() - start, 4), "seconds")
        quit()

# 2 characters
for a in alphabet:
    for b in alphabet:
        guess = a + b
        tries += 1
        if guess == password:
            print("Password found:", guess)
            print("Tries:", tries)
            print("Time:", round(time.time() - start, 4), "seconds")
            quit()

# 3 characters
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            guess = a + b + c
            tries += 1
            if guess == password:
                print("Password found:", guess)
                print("Tries:", tries)
                print("Time:", round(time.time() - start, 4), "seconds")
                quit()

# 4 characters
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                guess = a + b + c + d
                tries += 1
                if guess == password:
                    print("Password found:", guess)
                    print("Tries:", tries)
                    print("Time:", round(time.time() - start, 4), "seconds")
                    quit()