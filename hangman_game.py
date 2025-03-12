import random


words=["pyramid","colosseum","petra","zeus","machu","babylon","lighthouse","chichen","tajmahal","redeemer","rhodes","greatWall","halicarnassus","ephesus","giza"]

sel_word=random.choice(words)
display=['_' for _ in sel_word] #Create an list of underscore
#print(display)
attempts=8

print("Hangman Game")
print("Guess the word related to 7 Wonders of the World\n")

while attempts>0 and '_' in display:
    print("\n"+" ".join(display)) 
    guess=input("Guess a letter : ").lower()
    if guess in sel_word:
        for index,letter in enumerate(sel_word):
            if letter==guess:
                display[index]=guess #Reveal letter
    else:
        print("Your Guess is wrong :( \n")
        attempts-=1
    if attempts>0:
        print(f"You are left with {attempts} attempts")

if '_' not in display:
    print("You guessed the word,Hurrayyyy :)\n")
    print(' '.join(display))
    print("You survived....\n")
else:
    print("You ran out of attempts. The word was: "+ sel_word)
    print("You lost....\n")
