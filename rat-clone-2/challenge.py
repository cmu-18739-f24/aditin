import time
import random
import os
import hashlib
import re
# Read the flag from flag.txt
with open('flag.txt', 'r') as f:
    flag = f.read().strip()
    
cheese_textfile = "cheese_list.txt"
hints = ["I heard that *SHA-256* is the best hash function out there!",
         "Remember Squeexy, we enjoy our cheese with exactly *2 nibbles* of *hexadecimal-character salt*!",
         "Ever heard of *rainbow tables*?",
         "I've only eaten cheeses on this list: http://www.nourishinteractive.com/healthy-living/free-nutrition-articles/110-list-cheeses"]

welcome =  """
*******************************************
***             Part 2                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************
"""


mouse_standing = """
         _   _
        (q\_/p)
         /. .\        
  ,__   =\_t_/=   
     )   /   \      
    (   ((   ))   
     \  /\) (/\    
      `-\  Y  /    
         nn^nn        
                          
"""
mouse_angry = """
         _   _
        (q\_/p)
         /.V.\        
  ,__   =\_t_/=   
     )   /   \      
    (   ((   ))   
     \  /\) (/\    
      `-\  Y  /    
         nn^nn        
                          
"""
mouse_sitting = """
   _   _
  (q\_/p)
   /. .\.-.....-.     ___,
  =\_t_/=     /  `\  (
    )\ ))__ __\   |___)
   (/-(/`  `nn---'
"""

mouse_with_cheese = """
         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))    /O_.-'  O |  
     \  /\) (/\    | o   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         
"""
mouse_with_cheese_bite1 = """
         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))      ).-'  O |  
     \  /\) (/\      )   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         
"""
mouse_with_cheese_bite2 = """
         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))        )'  O |  
     \  /\) (/\          )  o|   
      `-\  Y  /         ) O.-`  
         nn^nn        ) _.-'      
                   '--`         
"""

def munch_cheese():
    print(mouse_with_cheese)
    print("munch...")
    time.sleep(1)
    print(mouse_with_cheese_bite1)
    print("munch...")
    time.sleep(1)
    print(mouse_with_cheese_bite2)
    print("MUNCH.............\n")
    time.sleep(1)

# turn txtfile of cheeses into a list
def parse_cheeses_txt():
    with open(cheese_textfile, 'r', encoding='utf-8') as file:
        cheeses = [line.strip().lower() for line in file]  
    return cheeses

def sha256_with_salt_enc(cheese_name):
    # 2 byte salt generate
    hex_characters = '0123456789abcdef'
    salt = bytes.fromhex(''.join(random.choices(hex_characters, k=2)))
    
    salted_cheese = cheese_name.encode('utf-8') + salt
    return hashlib.sha256(salted_cheese).hexdigest()

def main():
    # parse list of cheeses
    list_of_cheeses = parse_cheeses_txt()


    # choose and encrypt the cheese we want player to guess
    actual_cheese = random.choice(list_of_cheeses).lower()
    encrypted_cheese = sha256_with_salt_enc(actual_cheese)

    # draw out scene
    print(welcome)
    print("DRAT! The evil Dr. Lacktoes Inn Tolerant's clone was able to guess the cheese last time! I guess simple ciphers aren't good hashing methods. But now I've strengthened my encryption scheme so that now ONLY SQUEEXY can guess it...\n")
    print("Here's my secret cheese -- if you're Squeexy, you'll be able to guess it: ", encrypted_cheese)

    print()
    for i in range(5):
        print("Commands: (g)uess my cheese or (h)int")
        choice = input("What would you like to do?\n")
        if choice == 'g':
            print(mouse_sitting)
            print("SQUEAK SQUEAK SQUEAK")
            time.sleep(1)
            print(mouse_standing)
            print("Is that you, Squeexy? Are you ready to GUESS...MY...CHEEEEEEESE?")
            time.sleep(1)
            print("Remember, this is my encrypted cheese: ", encrypted_cheese)
            guessed_cheese = input("So...what's my cheese?\n").lower()
            
            munch_cheese()
            if guessed_cheese == actual_cheese:
                print("YUM! MMMMmmmmMMMMmmmMMM!!! Yes...yesssss! That's my cheese!")
                print("Here's the password to the cloning room: ", flag)
            else:
                print(mouse_angry)
                print("BLEHHHHH yuck. THAT'S not my cheese. GET OUT CLONE!!!1111!!!1!!!\n")
            break
        elif choice == 'h':
            print(hints[i%len(hints)])
            print("\n")
        else:
            print("I'm not sure what you mean *squeeeeak*\n")
        print("I don't wanna talk to you too much if you're some suspicious character and not my BFF Squeexy!")
        print("You have " + str(4-i) + " more chances to prove yourself to me!\n")
        if i == 4:
            print("GET OUUUUUUUUUUT!!!")
        

if __name__ == "__main__":
    main()




