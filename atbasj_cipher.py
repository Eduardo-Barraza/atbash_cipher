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
