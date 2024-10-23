def encryptor(a,b):
    with open("WordReplacer.txt","r") as f:
        content=f.read()
    ContentNew=content.replace(a,b)
    with open("WordReplacer.txt","w") as f:
        f.write(ContentNew)
    
    with open("WordReplacer.txt","r") as f:
        reader=f.read()
        print(reader)



word =input("Enter the string to br encrypted:\t")
word2=input("Enter the string you want to encrypt the word: \t")

encryptor(word,word2)
