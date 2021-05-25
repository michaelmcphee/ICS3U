#Michael McPhee, 04/12/21, program that counts letters in a string

string = input("Enter sentence: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
num = 0

#for loop counting letters
for i in range(26):
    num = string.lower().count(alphabet[i])
    if num != 0:
        print(alphabet[i],":",num)