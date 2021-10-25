# JARVIS is a simple and fun chatty bot for greeting the user and guessing their age.
# The bot will also test your knowledge with one simple question.  
 
# greet the new user
def greet(bot_name, birth_year):
    print()
    print('Hello! My name is ', bot_name + '. ', end="")
    print('I was created in ' + birth_year + '.')


# complement the user on his name
def remind_name():
    print('Please, remind me your name.')
    name = input("> ")
    print('What a great name you have, ' + name + '!')


# guess the age of the user
def guess_age():
    print('Let me show you a magic by guessing your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    age = (int(input("> ")) * 70 + int(input("> ")) * 21 + int(input("> ")) * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")


# count the numbers for the user
def count():
    print('Now I will prove to you that I can count to any number.')
    print('Enter any number below.')
    num = int(input("> "))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1
    print('HAHA! Told you I could count.')


# test the user
def test():
    print("Let's test your knowledge. Choose one of the options below.")
    print("Why do we use methods in programming?")
    counter = 0
    correct_answer = 2
    options = ["1. To repeat a statement multiple times.",
               "2. To decompose a program into several small subroutines.",
               "3. To determine the execution time of a program.",
               "4. To interrupt the execution of a program."]
    while counter < len(options):
        print(options[counter])
        counter += 1
    answer = int(input("> "))
    while answer != correct_answer:
        print("Please, try again!")
        answer = int(input("> "))
    print('Good Job!')


# end the program with the following lines
def end():
    print("I hope you enjoyed talking to me.")
    print('Have a nice day!')


# invoking the functions
greet('JARVIS', '2021')
remind_name()
guess_age()
count()
test()
end()
