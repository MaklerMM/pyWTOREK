sentence = "Maja ma kota Zindi, a kot ma Panią Maje."

# oczysc zdanie ze znakow interpunkcyjnych

sentence = sentence.replace(",","")
sentence = sentence.replace(".","")
print(sentence)

# zapisz wszystkie slowa osobno

words = sentence.split(" ")
print(words)