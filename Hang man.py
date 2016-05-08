import random
print("Welcome to WORK!")
print("By Koala Industries")

def WORK():
    wordlist=["donkey", "frog", "fiona","squirtle", "beach", "hunting", "near", "shrek", "tom", "work", "Pigeon", "Juice", "Blow","angry", "Cone"]
    word=random.choice(wordlist)
    gameloop=True
    guess=0
    guess2=0
    guessed=""
    guess3=0
    word3=""
    word3=word
    wordlegnth=len(word3)
    name=input("Enter Your Name: ")
    print("The word has: ", wordlegnth, "Letters" )
    while gameloop==True:
        letter=input("enter a letter to guess: ")
        if len(letter)==1:
            long=len(word3)
            if letter in word:
                print("Good")
                guessed=guessed+letter
                word2=word.replace(letter, "")
                word=word2
                guess3=guess3+1
                print("These are the correct guesses: ",guessed )
                guess2=guess2+1
                if long==guess2:
                    print(name, "You got the word", word3)
                    print(name, "It took you: ", guess3, "tries")
                    gameloop=False
                else:
                    print("")
                    

            else:
                guess=guess+1
                print("GET BACK TO WORK")
                print(guess, "Tries")
                if guess == 11:
                    print("You have failed")
                    print("The word was", word3)
                    gameloop=False


        else:
            print("Only one letter")


WORK()
