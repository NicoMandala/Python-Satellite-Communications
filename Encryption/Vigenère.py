



"""Vigenère cipher is the second interesting alphabetic cipher that I've found after Caesar cipher which is child's play.
Input: String, Key
Output: Encrypted String
Comments: The value of each character(from ascii table) is added repetitively over the length of the string.
            Easy to implement| Easy to decipher by people who recognize them| Used only to encrypt alphabet

Example: "The fox is red.", "abc" => The fox is red --> The ascii values are added and the result is generated as the output.
              String         key     abcabcabcabcab
               


Caesar cipher(legacy cipher): Add a constant number 3 to every value alphabet
ex: ABC --> DEF
This code can be modified to a similar idea by giving a single character such as "a" to be the key.

"""

 # step 1 
def generateKey(string, key): 
  key = list(key)                           # turns the string to a list
  if len(string) == len(key):               # if the length of the string is equal to key then there's no need of repeating the key phrase
    return(key) 
  else: 
    for i in range(len(string) -len(key)):  # for 0,1,2,3.....difference between length
      key.append(key[i % len(key)])         # for every such i divide it by the length of key, the remainder will be the index of the digit to be added. add that character to the list
  return("" . join(key))                    # Join all elements of the list into a string



# step 2
def encryption(string, key): 
  encrypt_text = []                          # start with an empty list
  key = generateKey(string,key)              # use the function to generate a key of sufficient length
  for i in range(len(string)):               # for each character of the string
    x = (ord(string[i]) + ord(key[i])) % 26  # Meant for alphabet using a modulo function to place the alphabet
    x += ord('A')                            # start from A and add the modulus to calculate the resulting letter
    encrypt_text.append(chr(x))              # add each character
  return("" . join(encrypt_text))            # list 2 string


# step 3
def decryption(encrypt_text, key): 
  orig_text = []                                      # start with the empty list
  key = generateKey(string,key)                       # generate key
  for i in range(len(encrypt_text)):                  # through the encrypted text
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26 # find the exact value of letter after subtraction
    x += ord('A')                                     # add the resulting value to A, so that we start from A
    orig_text.append(chr(x))                          # resulting list
  return("" . join(orig_text))                        # list 2 string



# use case
encrpyted_text = encryption("Thisissecret","qwdf")