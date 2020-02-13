
Name_A = Nicholas   #Name
Surname_A = Lazidis #Surname
year_of_birth_A = 1990  #Year of birth

Name_B = Egle   #Name
Surname_B = Vysniauskaite   #Surname
year_of_birth_B = 1992 #Year of birth

Name_C = Michael    #Name
Surname_C = Tsardakas   #Surname
year_of_birth_C = 1986  #Year of birth

#Question
user_input = str(input('Who are you?'))

#If statement that identifies your age depending on the character!

if user_input == Name_A:
    print("You're a youngster")
elif user_input == Name_B:
    print("You're a baby")
else:
    print("You're old")


