vowels=0
word= "engineering"
for char in word:
    if char.lower() in "aeiou":
         vowels+=1
         print(char, end=" ")
print(vowels)