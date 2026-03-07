from termcolor import colored
import colorama
import sys 
import string
import random
from datetime import datetime

colorama.init()

class PasswordChecker:
 common_passwords = ["password", "123456", "12345678", "12345", "1234567", "1234567890",
    "password1", "password123", "qwerty", "abc123", "111111", "123123",
    "admin", "admin123", "letmein", "welcome", "monkey", "dragon",
    "master", "sunshine", "princess", "shadow", "superman", "michael",
    "football", "baseball", "soccer", "hockey", "basketball"] #list of common password

 def __init__(self,password):
  self.__password = password #private attritubute 
  self.score = 0
  self.advice =[]
 

 def show_password(self): #getter
   return(f"Password : {colored(self.__password,'red')}")
 
 def change_password(self,new_password): #setter
  if len(new_password) <= 0:
   return "Password length is too short"
  else:
   confirm = input(f"Do you want change your password to {new_password}? y/n").strip() == "y" #y to change, n to skip
   if confirm:
    self.__password = new_password
    return "Password sucessfully changed"
   else:
    return "Password remains unchanged"
 

 def check_length(self):
  password = self.__password
  #check password length:
  if len(password) >15:
   self.score += 6
  elif len(password) >10:
   self.score += 4
  elif len(password) >=7:
   self.score += 3
  elif len(password) >=5:
   self.score +=1
  else:
   self.score -=2
   self.advice.append("Increase password length")

 def check_common(self):
  password = self.__password
  if password.lower() in self.common_passwords:
   self.score -= 5
   self.advice.append("Password is too common")
  
 def check_number(self):
  if any(x.isdigit() for x in self.__password):  #True if any digit is in the password
   self.score += 2
  else:
   self.advice.append("Add a number")

 def check_upper(self):
  if any(x.isupper() for x in self.__password):
   self.score += 1
  else:
   self.advice.append("Add an upper case letter")

 def check_lower(self):
  if any(x.islower()for x in self.__password):
   self.score += 1
  else:
   self.advice.append("Add a lower case letter")

 def check_special(self):
  special = "@~#/,.()-=+!£$%^&*"  #bank of special characters
  if sum(x in special for x in self.__password) >3: #true if total > 3
   self.score += 5
  elif any(x in special for x in self.__password):
   self.score += 2
  else:
   self.advice.append("Add a special character")


 def scan(self):
  self.score = 0 
  self.advice = []
  #check for the score:
  self.check_common()
  self.check_length()
  self.check_lower()
  self.check_upper()
  self.check_number()
  self.check_special()

 def show_result(self):
  self.score = max(0,self.score)
  if self.score > 10:
   self.score = 10
  print(self.show_password())
  print(f"Password score = {colored(self.score,"red")}")
  for i in self.advice: #print all advices
   print(f"- {i}")

  match self.score: #comment on the score
   case 10:
    print(colored("Perfect password :)","green"))
   case 9:
    print("Almost perfect")
   case 8:
    print("Very strong password")
   case 7:
    print("Strong password")
   case 6:
    print("Your password is not bad!")
   case 5:
    print("Fine password")
   case _: #anything below 5
    print("WEAK password! Please make your password stronger.")

 def save_result(self):
  with open("password_history.txt","a") as file: #open a txt file
   now = datetime.now()
   file.write(now.strftime("%d/%m/%Y %H:%M:%S"))
   file.write(f" Password: {self.__password}\t")
   file.write(f"Password score: {self.score}\n") #creates new line for every password


class PasswordGenerator: 
 bank = ["!","£","$","%","^","&","*","(",")","-","_","+","@","#"] #list of special characters

 def __init__(self,length,is_upper,is_lower,is_number,is_special):
  self._length = length
  self.is_upper = is_upper
  self.is_lower = is_lower
  self.is_number = is_number
  self.is_special = is_special
  self.passwd = []

 @property
 def length(self):
  return self._length
 
 @length.setter
 def length(self,new_length):
  if new_length.isdigit() and new_length >0:
   self._length = new_length
   return "password length changed sucessfully"
  else:
   return "Password too short or is not a digit"


 def upper(self):
  length = self._length//sum([self.is_upper,self.is_lower,self.is_number,self.is_special])
  for i in range(length):
   random_upper = random.choice(string.ascii_uppercase)
   self.passwd.append(random_upper)

 def lower(self):
  length = self._length//sum([self.is_upper,self.is_lower,self.is_number,self.is_special])
  for i in range(length):
   random_lower = random.choice(string.ascii_lowercase)
   self.passwd.append(random_lower)

 def number(self):
  length = self._length//sum([self.is_upper,self.is_lower,self.is_number,self.is_special])
  for i in range(length):
   random_number = random.randint(0,9)
   self.passwd.append(str(random_number))
  
 def special(self):
  length = self._length//sum([self.is_upper,self.is_lower,self.is_number,self.is_special])
  for i in range(length):
   random_special = random.choice(PasswordGenerator.bank) 
   self.passwd.append(random_special)

 def fill_missing(self):
  difference = self._length - len(self.passwd)
  if difference != 0:
   if self.is_upper:
    self.passwd.append(random.choice(string.ascii_uppercase)) 
   elif self.is_lower:
    self.passwd.append(random.choice(string.ascii_lowercase))
   elif self.is_number:
    self.passwd.append(str(random.randint(0,9)))
   else:
    self.passwd.append(random.choice(PasswordGenerator.bank)) #the list created at the start

 def generate(self):
  if self.is_upper:
   self.upper()
  if self.is_lower:
   self.lower()
  if self.is_number:
   self.number()
  if self.is_special:
   self.special()
  self.fill_missing()
  random.shuffle(self.passwd)
 
 def display(self):
  return(f"Random_password: {colored("".join(self.passwd),"red")}")
  
 def get_passwd(self):
  return "".join(self.passwd)

def main():
 print("----------------------------------")
 print(colored("Welcome to Password Strength checker/generator","yellow"))
 while True:
  style = input("Enter '1' to check password strength, '2' to generate password")
  if style not in ['1','2']:
   print("Invalid input")
   continue
  if style == '1':#check password strength
   while True:
    user_password = input("Please enter your password:  ").strip()
    if not user_password: #make sure password is entered
     print("Password cannot be none")
     continue
    check = PasswordChecker(user_password) #create a "check" object
    check.scan() #check strength
    check.show_result() #display result
    check.save_result() #save result into a file
    print("----------------------------------")
    while True:
     mode = input(colored(f"Enter '1' to change your password, '2' to see your password, '3' to enter a new password, '4' to exit, '5' to switch mode")).strip()
     if mode not in ["1","2","3","4","5"]: #check if input is valid
      print("Invalid input, please try again")
      continue
     match mode: # match the user's input
      case "1":
       new = input("Enter new password: ")
       print(check.change_password(new))
       check.scan()
       check.show_result()
       check.save_result()
      case "2":
       print(check.show_password()) 
      case "3":
       pass #the while loop will run over again
      case "4":
       print("Bye!")
       sys.exit() #exit the program 
      case "5":
       main()
 
  else: #generate password
   while True:

    passwd_length = input("Length of password: ")

    try:
     passwd_length = int(passwd_length) #check if input is a number
    except ValueError:
     print("Please Enter a number")
     continue

    include_upper = input("Do you want to inculde upper case? [y/n]").strip() == "y"
    include_lower = input("Do you want to include lower case? [y/n]").strip() == "y"
    include_number = input("Do you want to include number? [y/n]").strip() == "y"
    include_special = input("Do you want to include special characters? [y/n]").strip() == "y"
    if not any([include_lower,include_upper,include_special,include_number]):
     print("You must select at least one option")
     continue

    generator = PasswordGenerator(passwd_length,include_upper,include_lower,include_number,include_special)
    generator.generate()  
    print(generator.display())
    while True:
     print("----------------------------------")
     options = input("Enter '1' to continue generating passwords,'2' to switch mode, '3' to check password strength")
     if options not in ["1","2","3"]:
      print("Invalid input, please try again")
      continue
     match options:
      case "1":
       break
      case "2":
       main()
      case "3":
       passwd = generator.get_passwd()
       check = PasswordChecker(passwd) #create a "check" object
       check.scan() #check strength
       check.show_result() #display result
       check.save_result() #save result into a file

if __name__ == "__main__":
 main()


