# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:04:55 2026

@author: hborgic
"""

import random

def roll_2_dice():
    total = ""
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    total = die1 + die2
    if die1 + die2 == 2:
        print("You rolled a 1 and a 1. You lose!")
        total = 2
        return total
    if die1 + die2 == 12:
        total = 24
        print(f"You rolled a {die1} and a {die2}. Points earned: {total}")
        return total
    else:
        print(f"You rolled a {die1} and a {die2}. Points earned: {total}")
        return total

 

def play_pig():
    total = 0
    playerinp = ""
    playerlist = []
    while playerinp != "STOP":
        roll = roll_2_dice()
        if roll == 2:
            playerinp = "STOP"
            break
        total += roll
        playerlist += [roll]
        
        print(f"Your total is {total}.")
        if total >= 100:
            break
        playerinp = input("If you'd like to roll again press enter and if you'd like to forfeit enter STOP: ")
        playerinp = playerinp.upper()
        if playerinp == "STOP":
            break
    if total >= 100:
        print("You made it past 100!!!!")
        return playerlist
    if playerinp == "STOP":             #If player rolls 1 & 1 or stops
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ,0 ,0 ,0, 0]
list1 = []
list2 = []
player_num = 0

print("Hello, welcome to Play Pig Multiplayer")

player_num = int(input("How many players are there? "))
while player_num <=1:
    print("*There must be atleast 2 players*")
    player_num = int(input("How many players are there? "))

for number in range(player_num):
    name = str(input(f"Please enter the name of Player {number + 1}: "))
    list1 += [name]             #List1 is the store of players names

for player in list1:
    print(f"\n{player}, it's your turn!\n")
    player = play_pig()
    list2.append(player)        #adds list of the player's roles to a list in the order the players rolled
    

new_list1 = list1
new_list2 = list2
newest_list2 = list2
temp_value = []
winner_by_rolls = 0
newer_list2 = []


print("\nRESULTS:")
while new_list1 != []:
    print(new_list1[0], end= "")
    if new_list2[0] == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
        print(":\tDid not win.")       #long list was needed to ensure a losing player didn't win/probably a better way
    else:
        print(":\t", end= "")
        print(new_list2[0])
    new_list1 = new_list1[1:]       #removes the first element in the list / the 1: part
    new_list2 = new_list2[1:]

while list2 != []:
    newer_list2.append(len(list2[0]))   #take first term of roll list and converts it to its length
    list2 = list2[1:]                  #removes the first element in the list / the 1: part


this = min(newer_list2)
winner_by_number = []
winner_by_number += [int(newer_list2.index(min(newer_list2)))]   #find the location of min value in newer_list2



if min(newer_list2) == 37:                  #everyone loses
    print("\nEVERYBODY LOSES!!!!")
    this = 1000
    winner_by_number = []
x = 1

newer_list2.remove(min(newer_list2))
if min(newer_list2) == this:    #Tie condition
    while min(newer_list2) == this:
        winner_by_number += [int((newer_list2.index(min(newer_list2))) + x)]
        x += 1
        newer_list2.remove(min(newer_list2)) #removes min
        newer_list2.append(100)
        
    if len(winner_by_number) > 1:
        
        print("\nIt was a tie between ",end = "")
        while len(winner_by_number) > 1:
            print(f"{list1[winner_by_number[0]]}", end = ", ")
            winner_by_number = winner_by_number[1:]
        print(f"and {list1[winner_by_number[0]]}.")
    print(f"\nIn {this} rolls!")
    winner_by_number = []
if len(winner_by_number) == 1:                      #a singular winner
    print(f"\nIt looks like {list1[winner_by_number[0]]} won in {this} rolls!")
    
    
    
    
    
    
    
    
    