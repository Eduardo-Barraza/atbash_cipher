Atbash Cipher is a simple substitution cipher where the letters of the alphabet are reversed. For example, 'A' is substituted with 'Z', 'B' with 'Y', and so on.

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(155 - ord(char))
            else:
                result += chr(219 - ord(char))
        else:
            result += char
    return result

# Example usage
text = "HELLO, World!"
encrypted = atbash_cipher(text)
decrypted = atbash_cipher(encrypted)  # Atbash is symmetric

print(f"Original text: {text}")
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")

Explanation of the Atbash Cipher Code
Letter Reversal:

The ASCII values of the characters are adjusted to reverse their position in the alphabet.
Symmetric Encryption and Decryption:

The Atbash Cipher is symmetric, meaning the same function can be used for both encryption and decryption.
These alternative ciphers, Vigenère and Atbash, provide different levels of complexity and security compared to the Caesar Cipher and can be fun and educational to implement.
