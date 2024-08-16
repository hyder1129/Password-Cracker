from random import *
import os
user_pwd = input("Enter the password:")
pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

pw = ""
while(pw!=user_pwd):
    pw=""
    for letter in range(len(user_pwd)):
        guess_pwd=pwd[randint(0,35)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking password...please wait!")
        os.system("cls")
print("Your password Is: ",pw)
