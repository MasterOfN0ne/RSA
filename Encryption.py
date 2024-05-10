# Bob's side of the encryption process

# This script uses the public key (n, e) to encrypt a message and the private key d to decrypt it
# The message comes in a text file called "message.txt"
# This script reads the message, encrypts it and writes the encrypted message in a file called "encrypted_message.txt"

# First, we read the message
with open("message.txt", "r") as file:
     message = file.read()

# We convert the message to a list of numbers
message = [ord(char) for char in message]

# We read the public key
with open("public_key.txt", "r") as file:
    n = int(file.readline())
    e = int(file.readline())

# We encrypt the message
encrypted_message = [pow(char, e, n) for char in message]

# We write the encrypted message in a file
with open("encrypted_message.txt", "w") as file:
    for char in encrypted_message:
        file.write(str(char) + "\n")

# The encrypted message is now in the file "encrypted_message.txt"
