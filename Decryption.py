# This script uses the private key d to decrypt the message contained in the file "encrypted_message.txt"
# The decrypted message is written in a file called "decrypted_message.txt"

# First, we read the encrypted message
with open("encrypted_message.txt", "r") as file:
    encrypted_message = [int(line) for line in file]

# We read the private key
with open("private_key.txt", "r") as file:
    d = int(file.readline())
    n = int(file.readline())

# We decrypt the message
decrypted_message = [pow(char, d, n) for char in encrypted_message]

# We convert the decrypted message to a string
decrypted_message = "".join([chr(char) for char in decrypted_message])

# We write the decrypted message in a file
with open("decrypted_message.txt", "w") as file:
    file.write(decrypted_message)

# The decrypted message is now in the file "decrypted_message.txt"
