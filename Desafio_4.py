
# coding: utf-8

# In[28]:



#Determines if a word (its sum) ist prime or not; To check type paprima('word') and execute




paprima = (lambda word: ((lambda num: all(num % d for d in range(2, int(num ** 0.5) + 1))) (sum(map( (lambda letter: (ord(letter) - (38 if letter.isupper() else 96))), list(word))))))








paprima('Trustcode')







