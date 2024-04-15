#GAME TEBAK KATA
import random


nama = input("Siapa nama anda? ")

print("Selamat, ",nama,'. Semoga beruntung ')

katakata = ["macan",'harimau',"singa","kancil","kuda","monyet","jerapah","naga","buaya","menjangan","rusa","simpanse","sapi"]

kata = random.choice(katakata)

print("Tebak sebuah kata : ")

guesses = ''

turns = 12

while turns > 0:
 
    # counts the number of times a user fails
    failed = 0
 
    # all characters from the input
    # word taking one at a time.
    for char in kata:
 
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end=" ")
 
        else:
            print("_")
 
            # for every failure 1 will be
            # incremented in failure
            failed += 1
 
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")
 
        # this print the correct kata
        print("The kata is: ", kata)
        break
 
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("guess a character:")
 
    # every input character will be stored in guesses
    guesses += guess
 
    # check input with the character in kata
    if guess not in kata:
 
        turns -= 1
 
        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")
 
        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')
 
        if turns == 0:
            print("You Loose")