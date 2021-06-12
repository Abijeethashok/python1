intro = input("Enter your informations")
wordcount = 1
lettercount = 0 

for i in intro:
    print(i)
    lettercount = lettercount + 1
    if i == " ":
        wordcount = wordcount + 1
print(wordcount)
print(lettercount)        