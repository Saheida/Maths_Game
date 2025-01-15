import random
"""
Set the variables for the math quiz.

Variables:
- score (int): Tracks the user's correct answers, starting at 0.
- total_questions (int): Specifies the total number of questions to be asked in the quiz, which is set to 5
"""
score = 0
total_questions = 5 

"""
Generates random numbers to create a math equation in the format `a * x = b`.
Details:
- `a` (int): A random integer number between 1 and 10, representing the number that multiplies `x`.
- `b` (int): A random multiple of `a` between `a` and `20 * a`, representing the result of the equation.
- `x` (int): The correct solution to the equation, calculated as `b // a`.
"""
for i in range (total_questions) :
    a = random.randint(1, 10)  
    b = random.randint(1, 20) * a 
    # Calculate x
    x = b // a

"""
Displays the equation to the user, collects their answer and lets them know if it is correct
"""

print (f"question {i + 1}: {a} xx = {b}")
"""
Display the current question in the format `a * x = b` and ask them to input their answer for x.
"""
user_answer = int(input("What is the x?"))
"""
Check if the user's answer matches the correct value of `x`.
If correct, print "Correct!" and increment the score.
If incorrect, print the correct answer for `x`
"""
if user_answer == x:
        print ("Correct!")
        score += 1
else:
        print (f"Wrong! The correct answer is x = {x}")

"""
Displays the user's final score and provides feedback based on their performance.
Provide feedback:
   - If the user scores more than 50%, display a positive message.
   - Otherwise, encourage the user to practice more.
   Variables:
- `score` (int): The total number of correct answers given by the user.
- `total_questions` (int): The total number of questions in the quiz.
"""
print (f"\nYour total score is: {score} out of {total_questions}")
if score > total_questions / 2:
    print ("Well done! You've scored above 50%")
else:
    print ("keep practicing! You can do better next time.")