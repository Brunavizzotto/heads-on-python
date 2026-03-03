color = 'blue'
guess = ''
guesses = 0

while guess != color:
    guess = input("what color am i thinking of?")
    guesses = guesses + 1
if guesses == 1:
    print("you got it in 1 guess")
else:
    print("you got it in", guesses, "guesses")


print("you got it in", guesses, "guesses")