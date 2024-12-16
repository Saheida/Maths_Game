# Multiplication Game-README

**Program Objective**

The Multiplication Game is a program that asks you five multiplication questions. You need to work out the correct answer of x.  After each question, the program will tell you whether you have answered correctly.  After answering all five questions, it will tell you the number of questions you answered correctly and whether your score was above 50%.

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
```
5)	**Run the program** and play the game
   
•	Click on ![image](https://github.com/user-attachments/assets/be2c499e-bff1-486f-b5b3-87751b3200a6)
 icon and a new **terminal** will appear 
 
 • You can now play the **game**
 
•	Have fun! ![image](https://github.com/user-attachments/assets/d86cedc2-0c86-4397-bcfa-0b1dc60499c7)



