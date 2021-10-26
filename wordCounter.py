input = input("name your file: ")
file = open(input)
fileTxt = file.read()
splitTxt = fileTxt.split()
wordCount=0

for i in splitTxt:
    wordCount+=1

print(wordCount)