#This list is called upon to know where the index of a specified letter is.
alphabet = "abcdefghijklmnopqrstuvwxyz"

#This is a decoder function to use, you need the code and the known offset of it.
def caesar_decode(code, offset):
    sentence_decoded = ''
    for letter in code.lower():
        if letter in alphabet:
            index = alphabet.find(letter)
            if index > (25 - offset) :
                new_index = int(index) + offset - 26
                sentence_decoded += alphabet[new_index]
            else:
                sentence_decoded += alphabet[index + offset]
        else:
            sentence_decoded += letter
    return sentence_decoded

#Example test
#print(caesar_decode('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14))

#This is a coder funtion, where you can input a sentence and an offset of your choice to decode it.
def caesar_code(sentence, offset):
  sentence_decoded = ''#
  for letter in sentence.lower():
      if letter in alphabet:
          index = alphabet.find(letter)
          sentence_decoded += alphabet[index - offset]
      else:
          sentence_decoded += letter
  return sentence_decoded

#Example test
#print(caesar_code('performing multiple caesar ciphers to code your messages is even more secure!', 14))

#This code if for when you need to decipher a sentence but you don't know the offset that is used.
#Note that is uses the previous caesar_decode function
def caesar_decode_without_offset(code):
  for num in range(len(alphabet)):
    print(f"Offset: {num + 1}")
    print(caesar_decode(code, num))
    print("~~~~~~~~~~")

#Example test
#print(caesar_decode_without_offset("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."))
