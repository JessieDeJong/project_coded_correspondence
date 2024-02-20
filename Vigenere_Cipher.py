#This list is called upon to know where the index of a specified letter is.
alphabet = "abcdefghijklmnopqrstuvwxyz"

#This is a coder function, where you can input a sentence and the keyword to encode it
def vigenere_code(sentence, keyword):
  sentence = sentence.lower()
  sentence_coded = ''
  keyword_sentence = ''
  keyword_index = 0

  #First we re-create the given sentence with the keyword
  for character in sentence:
      if keyword_index >= len(keyword):
        keyword_index = 0
      if character in alphabet:
        keyword_sentence += keyword[keyword_index]
        keyword_index += 1
      else:
        keyword_sentence += character

  #Next we encode the sentence with the offset of the original letter, minus the index of the keyword letter
  for i in range(len(sentence)):
      if sentence[i] in alphabet:
        index = (alphabet.find(sentence[i]) - alphabet.find(keyword_sentence[i]))
        sentence_coded += alphabet[index]
      else: 
        sentence_coded += sentence[i]
  return sentence_coded

#Example test
#print(vigenere_code('barry is the spy', 'dog'))
#Expected output: 'ymlok cp fbb ejv'

#This is the decoder function, you need the code and the keyword to decode the sentence
def vigenere_decode(code, keyword):
  code = code.lower()
  sentence_decoded = ''
  keyword_sentence = ''
  keyword_index = 0

  #First we re-create the given sentence with the keyword
  for character in code:
      if keyword_index >= len(keyword):
        keyword_index = 0
      if character in alphabet:
        keyword_sentence += keyword[keyword_index]
        keyword_index += 1
      else:
        keyword_sentence += character

  #Next we decode the sentence with the offset of the original letter, plus the index of the keyword letter
  for i in range(len(code)):
      if code[i] in alphabet:
        index = (alphabet.find(code[i]) + alphabet.find(keyword_sentence[i]))
        if index > 25:
          index = (index - 26)
        sentence_decoded += alphabet[index]
      else: 
        sentence_decoded += code[i]
  return sentence_decoded

#Example test
#print(vigenere_decode("txM srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz czA ruxzal wg zztcgcexxch!", "friends"))
#Expected output: 'you were able to decode this? nice work! you are becoming quite the expert at crytography!'
