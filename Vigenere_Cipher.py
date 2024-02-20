#This list is called upon to know where the index of a specified letter is.
alphabet = "abcdefghijklmnopqrstuvwxyz"

#This is a coder function, where you can input a sentence and the keyword to encode it
def vigenere_code(sentence, keyword):
  sentence = sentence.lower()
  sentence_coded = ''
  keyword_sentence = ''
  keyword_index = 0

  for character in sentence:
      if keyword_index >= len(keyword):
        keyword_index = 0
      if character in alphabet:
        keyword_sentence += keyword[keyword_index]
        keyword_index += 1
      else:
        keyword_sentence += character
        
  for i in range(len(sentence)):
      if sentence[i] in alphabet:
        index = (alphabet.find(sentence[i]) - alphabet.find(keyword_sentence[i]))
        sentence_coded += alphabet[index]
      else: 
        sentence_coded += sentence[i]
  return sentence_coded

#Example test
print(vigenere_code('barry is the spy', 'dog'))
#Expected output: 'ymlok cp fbb ejv'
