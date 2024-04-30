#Lesson 4: Assignnment ] Python Loop Statemenys
#1. The Range Riddle
#Task 1. Every Other Day
Week = ["Sunday", "Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday"]
Odd_i = []
even_i = []
for i in range (len(Week)):
    if i % 2== 0:
        even_i.append(Week[i])
    else:
        Odd_i.append(Week[i])
print(even_i)
print(Odd_i)
#2 Nested Loops
#Task 1: Meal Planner
Meal = ['Pasta', 'Soup', 'Waffels', 'Sandwich']
Time = ['Breakfast', 'Lunch', 'Diner'] 
import random
for days in range(len(Week)):
    for i in range(len(Time)):
        print('Today is',Week[days],'For', Time[i],'we are having', random.choice(Meal))
#3.Loop Condition Logic
#Task1:Loop Condition Exploration
while True:
        color = input("What is your favorite color?")
        if color == 'blue': 
            break
        season = input("what is your favorite season?")
        if season == 'fall':
         break 
        print('Loop ended.')
#Task 2: Conditional Exit
i = 0
while i != 5:
     i += 1
     print('iteration', i)

#4.Python's Random Game night
# Task 1: Random Choice Game
list = [ 'chess', 'checkers', 'manopoly', 'soccer']
print('lets play a new game')
print('we are choosing a game at random')  
game = random.choice(list)
while True:
     correct = input("which Game was Chosen?")
     if correct == game:
          print('correct')
          break 
#5.Advanced Looping Techniques (Bonus)
#task1: ice Cream Bo-Go
ice_Cream = ['Vanila', 'Stawberry', 'Chery', 'Lavander', ' cookie and Cream']
for flavor in range(len(ice_Cream)):
    for i in range(len(ice_Cream)):
        print('lets try a scoop of',ice_Cream[flavor],'with a second scoop of',ice_Cream[i],'on the top')
#Task 2:Double Up!
ice_Cream = ['Vanila', 'Stawberry', 'Chery', 'Lavander', ' cookie and Cream']
for flavor in range(len(ice_Cream)):
    for i in range(len(ice_Cream)):
        if ice_Cream[flavor] == ice_Cream[i]:
            print('Double it up lets try two scoops of',ice_Cream[flavor])
        else:
            print('lets try a scoop of',ice_Cream[flavor],'with a second scoop of',ice_Cream[i],'on the top')
#Task 3 no repates
ice_Cream = ['Vanilla', 'Stawberry', 'Chery', 'Lavander', ' cookie and Cream']

for flavor in range(len(ice_Cream)):
    for i in range(flavor+1,len(ice_Cream)):
        if ice_Cream[flavor] == ice_Cream[i]:
            print('Double it up lets try two scoops of',ice_Cream[flavor])
        else:

            print('lets try a scoop of',ice_Cream[flavor],'with a second scoop of',ice_Cream[i],'on the top')
