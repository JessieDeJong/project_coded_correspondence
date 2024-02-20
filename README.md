# project_coded_correspondence
## Caesar Cipher
📝 **Description:** 

The Caesar cipher is an encryption technique.</br>
The action of a Caesar cipher is to replace each plaintext letter witht a different one, a fixed number of places down the alphabet.

> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Caesar_cipher_left_shift_of_3.svg/640px-Caesar_cipher_left_shift_of_3.svg.png" style="height: 150px; width:300px;"/>

🪄 **Features:** 

I created a simple Ceasar Cipher code, to encode and decode a string with a given offset.</br>
It also has a decoder for when you don't know the offset.

## Vigenere Cipher
📝 **Description:** 

The Vigenère cipher is a method of encrypting messages by using a series of different Caesar ciphers based on the letters of a particular keyword. The Vigenère cipher is more powerful than a single Caesar cipher and is much harder to crack. </br>
> Suppose we wish to encrypt the plaintext message `Attack at dawn`, using the keyword `king`.
>
> Begin by writing the keyword, repeated as many times as necessary, above the plaintext message. To derive the ciphertext using the table above, for each letter in the plaintext, find the intersection of the row given by the corresponding keyword letter and the column given by the plaintext letter itself to pick out the ciphertext letter
> > Plaintext: `Attack at dawn` </br>
> > Keyword: `kingki ng king` </br>
> > Ciphertext: `qlgusc nn tsjh`

🪄 **Features:** 

I created a simple Vigenère cipher code, to encode and decode a string with a given keyword.
