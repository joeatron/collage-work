#Selection
sky = input("Is the sky blue or green: ")   #asks the user if the "sky is blue or green" and stores that in sky
if sky == blue:                             #reads sky and checks if the answer is blue
    print("You are correct")                #prints "you are correct"
elif sky == green:                          #reads sky and checks if the answer is green
    print("Lets hope you are colour blind for your sake")   #prints a joke
else:                                       #failsafe for if the answer is none of the abouth
    print("You monster thats not an answer. I am going to assume that it was a mistake on your part")   #prints a joke
    
