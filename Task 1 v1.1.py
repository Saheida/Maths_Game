import random
# Create the users score
score = 0
total_questions = 5 

# Create a loop and ask multiple Q's
for i in range (total_questions) :
    a = random.randint(1, 10)  
    b = random.randint(1, 20) * a 
    # Calculate x
    x = b // a

    #Display the equation
    print (f"question {i + 1}: {a} xx = {b}")
    #Display Users answer
    user_answer = int(input("What is the x?"))
    #Check if users answer is correct
    if user_answer == x:
        print ("Correct!")
        score += 1
    else:
        print (f"Wrong! The correct answer is x = {x}")
#Final result after all 5 questions have been answered
print (f"\nYour total score is: {score} out of {total_questions}")
if score > total_questions / 2:
    print ("Well done! You've scored above 50%")
else:
    print ("keep practicing! You can do better next time.")