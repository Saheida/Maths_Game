# Multiplication Game
This is a technical and user documentation for the Multiplication Game for a user who is new to Python. It will guide you through the process of installing and running the program as well as provide technical information on how the game works. 

## <ins>User Guidance</ins>

**Program Objective**

The Multiplication Game is a program that asks five multiplication questions. You need to work out the correct answer of x.  After each question, the program will tell you whether you have answered correctly.  After answering all five questions, it will tell you the number of questions you answered correctly and whether your score was above 50%.  The game will help you to practice basic multiplication skills.

**How to use the program**

The game is a python program, and you will need to install python to play the game.  To do this, complete the following

**Step 1 – Install Python**
1)	Go to the [Python website](https://www.python.org/)
2)	Click on **Downloads** and download **Python 3.13.1**
3)	After the download is completed, run the **Installer**
4)	In the Installation wizard, click on the **Add Python to PATH** and **select “Install Now”**

**Step 2 – How to get the Program file using Visual Studio Code (VS Code)**
1)	**Install VS code:** go to the [Visual Studio Code website](https://code.visualstudio.com/) and download VS code
2)	Open **VS code** and click **File – New File.**
   
   ![image](https://github.com/user-attachments/assets/c0a447dc-7e82-4971-b2ac-3cc06f51bfee)

3)	Save the file by clicking **File – Save As** and name it `maths_game.py`

   ![image](https://github.com/user-attachments/assets/b971e706-26d5-49de-b3a9-c3bdc20cab62)

4)	**Copy** the program code below and **paste** it into the `maths_game.py` file in the VS code window

```import random
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
```

5)	**Run the program** and play the game
   
•	Click on ![image](https://github.com/user-attachments/assets/be2c499e-bff1-486f-b5b3-87751b3200a6)
 icon and a new **terminal** will appear 
 
 • You can now play the **game**
 
•	Have fun! ![image](https://github.com/user-attachments/assets/d86cedc2-0c86-4397-bcfa-0b1dc60499c7)

## <ins>Technical Guidance</ins>
This is a simple maths game which generates random multiplication equations where the user is asked to solve x.  The program tracks the score of the user and provides feedback after each question. It starts with a score of zero and asks 5 questions and after all 5 have been answered it will tell the user if they have scored above 50%.

**System requirements**
* Python 3.x installed on the system

**How the program works**
* The program uses the module `random` to generate two random numbers
* It multiplies the two numbers to create an equation such as `5 xx = 50`
* The user is asked to answer the question `what is x?`
* The correct answer x is calculated by dividing the two numbers
* If the answer is correct, the program responds with `correct!`.  If it is incorrect it will display `Wrong! The correct answer is x = {x}`
* After answering all five questions, the program displays the total score.
* It calculates whether the users overall score was above 50% and displays `Well done! You've scored above 50%` or `keep practicing! You can do better next time.` 

**Code Breakdown**

The key elements of the program includes:

**Import Random Module**
```import random
score = 0  # Keeps track of the user's score
total_questions = 5  # Number of questions
```

**Creating the questions**
```# Create a loop and ask multiple Q's
for i in range (total_questions) :
    a = random.randint(1, 10)  
    b = random.randint(1, 20) * a 
    # Calculate x
    x = b // a
```

**Ask the user and check the answers**
```# Display the equation
    print (f"question {i + 1}: {a} xx = {b}")
    #Display Users answer
    user_answer = int(input("What is the x?"))
    #Check if users answer is correct
    if user_answer == x:
        print ("Correct!")
        score += 1
    else:
        print (f"Wrong! The correct answer is x = {x}")
```  

**Displaying the final score**
```#Final result after all 5 questions have been answered
print (f"\nYour total score is: {score} out of {total_questions}")
if score > total_questions / 2:
    print ("Well done! You've scored above 50%")
else:
    print ("keep practicing! You can do better next time.")
```

**Enhancing the game**

The multiplication game can be enhanced and difficulty levels increased by
* Changing the number of questions by modifying the ```total_questions``` variable
* Alter the difficulty level by changning the ranges in ```random_randit()``` to make the equations harder

**Licence**

This project is licenced under the MIT Licence.

**Copy the Respository**

```bash
git clone https://github.com/Saheida/Maths_Game
```

