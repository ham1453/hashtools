import hashlib 
import colorama
from hashlib import *
colorama.init(autoreset=True)
style = '''\033[31m


██╗░░██╗░█████╗░░██████╗██╗░░██╗ ████████╗░█████╗░░█████╗░██╗░░░░░██████╗░
██║░░██║██╔══██╗██╔════╝██║░░██║ ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗
███████║███████║╚█████╗░███████║ ░░░██║░░░██║░░██║██║░░██║██║░░░░░██║░░██║
██╔══██║██╔══██║░╚═══██╗██╔══██║ ░░░██║░░░██║░░██║██║░░██║██║░░░░░██║░░██║
██║░░██║██║░░██║██████╔╝██║░░██║ ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░

   0x096R Hack 
              hashing Tools 
              mail:0x096r@gmail.com
              f...0x096R 
'''
print(style)
print("========================================================================================")
print("\033[33m 1]- hash Chacker  \n 2]- hash length \n 3]- hash type \n 4]- MD5 Encrypt \n 5]- MD5 Decrypt \033[37m")
print("========================================================================================")

choose = input("Please choose option : ") 
if choose == '1': 
        print("This option For Hash chacker")
        hash1 = input("Enter hash [1] : ") 
        hash2 = input("Enter hash [2] : ") 
        if hash1 == hash2 : 
                print("The hash is clean ")
        else:  
                print("The hash is virus")
if choose == '2': 
       print("This option For length hash ")
       length = input("Enter your Hash :  ")
       print("Length Hash is : " , len(length))
if choose == '3':
       print("This option For know Hash type")
       hash = input("Enter the hash : ")
       length = len (hash)
       if length == 32 : 
              print ("The hash is [MD5]")
       if length == 40 :
              print("The hash is [sha1]")
       if length == 64 :
              print("The hash is [sha256]")
if choose == '4': 
       print("This option For text to MD5")
       word = input("Enter your text : ")
       md5  = hashlib.md5(word.encode())
       print(md5.hexdigest())
if choose == '5':
       print("This option For decryption")
       hash = input("Enter your hash : ")
       file = input("Write file name : ")
       with open(file , mode='r') as f : 
           for line in f : 
                line = line.strip()
                if md5(line.encode()).hexdigest() == hash : 
                    print("[-] password Found : " +line)





















