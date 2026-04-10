Summary of ceasarCipher.py:

This Python script implements a Caesar Cipher, a simple encryption technique that shifts letters in the alphabet by a given key while keeping spaces and non-letter characters unchanged.

Key Features:

Defines alphabets for lowercase ('a-z') and uppercase ('A-Z').
encrypt(text, key): Shifts each letter forward by the key (mod 26 to wrap around).
decrypt(text, key): Shifts each letter backward by the key (handles wrap-around).
Interactive menu: User chooses mode ('e' for encrypt, 'd' for decrypt), inputs text and key.
Outputs the result (ciphertext or plaintext).
How it works:
User runs the script, selects mode, enters plaintext/ciphertext and shift key. It processes letter-by-letter using ASCII checks and index shifting in alphabet strings, preserving case and non-letters.

Example: Encrypt "Hello" with key 3 → "Khoor".

Total words: 98
