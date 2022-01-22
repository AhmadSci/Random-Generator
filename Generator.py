import random
import string
from os import system
system("title " + "@c9zd - ListGen")
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)

print("""
  _____                 _                   _      _     _      _____            
 |  __ \               | |                 | |    (_)   | |    / ____|           
 | |__) |__ _ _ __   __| | ___  _ __ ___   | |     _ ___| |_  | |  __  ___ _ __  
 |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \  | |    | / __| __| | | |_ |/ _ \ '_ \ 
 | | \ \ (_| | | | | (_| | (_) | | | | | | | |____| \__ \ |_  | |__| |  __/ | | |
 |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_| |______|_|___/\__|  \_____|\___|_| |_|
""")
print(Fore.RED+"""
Cᴏᴅᴇᴅ Bʏ Aʜᴍᴇᴅ Iɴsᴛᴀ: @c9zd
""")
while 1:
    try:
        user_len = int(input("Length: ")) #variable input from user to know the length of the username
    except:
        print("Input Must Be Numerical!?")
        continue
    else:
        break

if user_len == 2:
    num_q = input("Want Numbers? "+ "(y/n) ").lower()
    thing_q = input("Want \"_\"? "+ "(y/n) ").lower()
    name_of_folder = input("File Name: ")
else :
    num_q = input("Want Numbers? "+ "(y/n) ").lower()
    if num_q != "y" and num_q != "n":
        print("Input Must Be y/n!?")
        num_q = input("Want Numbers? "+ "(y/n) ").lower()

    thing_q = input("Want Punctuations? "+ "(y/n) ").lower()
    if thing_q != "y" and thing_q != "n":
        print("Input Must Be y/n!?")
        thing_q = input("Want Punctuations? "+ "(y/n) ").lower()
    name_of_folder = input("File Name: ")



while 1:
    try:
        user_count = int(input("List Length: ")) #another variablr input to know how many useres he wants to generate
    except:
        print("Input Must Be Numerical!?")
        continue
    else:
        break

things = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"

if ".txt" in name_of_folder:
    folder = open(name_of_folder, "w+")
else:
    folder = open(name_of_folder+ ".txt", "w+")

def all_gen():
    for user in range(1):
            le = 1
            while le <= user_count:
                le += 1
                user = random.choice(things) + random.choice(things) + random.choice(things) + string.ascii_lowercase + string.digits + string.digits + string.digits + random.choice(things) + random.choice(things) + random.choice(things)
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
    folder.close()
    print("Done!")

def user_only_gen():
    for user in range(1):
            le = 1
            while le <= user_count:
                le += 1
                user = string.ascii_lowercase
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
    folder.close()
    print("Done!")

def twos_user___gen():
    for user in range(1):
            le = 1
            while le <= user_count:
                le += 1
                user = string.ascii_lowercase + random.choice(things)
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
    folder.close()
    print("Done!")

def user_num_gen():
    for user in range(1):
            le = 1
            while le <= user_count:
                le += 1
                user = string.ascii_lowercase + string.digits 
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
    folder.close()
    print("Done!")

def user_punc_gen():
    for user in range(1):
            le = 1
            while le <= user_count:
                le += 1
                user = string.ascii_lowercase  + random.choice(things) + random.choice(things) + random.choice(things) + random.choice(things)
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
    folder.close()
    print("Done!")

if user_len == 2:
    if num_q =="n" and thing_q == "n":
        user_only_gen()
    elif num_q == "y" and thing_q == "n":
        user_num_gen()
    elif num_q == "y" and thing_q == "y":
        all_gen()
    elif num_q == "n" and thing_q == "y":
        twos_user___gen()
else:
    if num_q =="n" and thing_q == "n":
        user_only_gen()
    elif num_q == "y" and thing_q == "n":
        user_num_gen()
    elif num_q == "y" and thing_q == "y":
        all_gen()
    elif num_q == "n" and thing_q == "y":
        user_punc_gen()
    

while 1:
    q = input("Want another list? "+ "(y/n) ").lower()
    if q == "y":
        while 1:
            try:
                user_len = int(input("Length: "))
            except:
                print("Input Must Be Numerical!?")
                continue
            else:
                break
        if user_len == 2:
            num_q = input("Want Numbers? "+ "(y/n) ").lower()
            thing_q = input("Want \"_\"? "+ "(y/n) ").lower()
            name_of_folder = input("File Name: ")
        else :
            num_q = input("Want Numbers? "+ "(y/n) ").lower()
            thing_q = input("Want Punctuations? "+ "(y/n) ").lower()
            name_of_folder = input("File Name: ")
        while 1:
            try:
                user_count = int(input("List Length: "))
            except:
                print("Input Must Be Numerical!?")
                continue
            else:
                break
        if ".txt" in name_of_folder:
            folder = open(name_of_folder, "w+")
        else:
            folder = open(name_of_folder+ ".txt", "w+")
        if user_len == 2:
            if num_q =="n" and thing_q == "n":
                user_only_gen()
            elif num_q == "y" and thing_q == "n":
                user_num_gen()
            elif num_q == "y" and thing_q == "y":
                all_gen()
            elif num_q == "n" and thing_q == "y":
                twos_user___gen()
        else:
            if num_q =="n" and thing_q == "n":
                user_only_gen()
            elif num_q == "y" and thing_q == "n":
                user_num_gen()
            elif num_q == "y" and thing_q == "y":
                all_gen()
            elif num_q == "n" and thing_q == "y":
                user_punc_gen()
    else:
        print("Closing in 3 Seconds")
        time.sleep(3)
        break
