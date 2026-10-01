File Name: wk09d02ex03_guess_colors.py 
Short Description: A rainbow color guessing quiz with a main sequence, arrays, loops, and selection. 
Author: Pascua, Gaea Nikolaev B. 
Date: 2026-09-28 

print("Hello, dear user! I am Flowy, your friendly Flowgorithm teacher. Today, we'll have a quiz about the 
colors of the rainbow! Oh- but before that, what's your name?") 
userName = input() 
print("What a wonderful name! Let's start the quiz, shall we?") 
rainbowColors = [""] * (7) 
userGuesses = [""] * (7) 

rainbowColors[0] = "Red" 
rainbowColors[1] = "Orange" 
rainbowColors[2] = "Yellow" 
rainbowColors[3] = "Green" 
rainbowColors[4] = "Blue" 
rainbowColors[5] = "Indigo" 
rainbowColors[6] = "Violet" 
for i in range(0, 6 + 1, 1): 
    print("Please enter color " + str(i + 1) + " of the rainbow!") 
    userGuesses[i] = input() 
    correctCount = 0 
for i in range(0, 6 + 1, 1): 
    if userGuesses[i] == rainbowColors[i]: 
        correctCount = correctCount + 1 
print("Dear user, you got " + str(correctCount) + " correct answers.") 
if correctCount >= 6: 
    print("Congratulations, " + userName + "! Your grade is excellent!") 
else: 
    if correctCount >= 3: 
        print("Good job, " + userName + "! Your grade is average!") 
    else: 
        print("Oh no- your grade is poor. But don't worry! You can do better next time!")
