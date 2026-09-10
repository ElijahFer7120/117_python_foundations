""" 
Week 2 Demo 1: the Elsa Rank check

Purpose:
Show how a program chooses between multiple branches.

developer notes:
i named it "elsa" for a dumb pun
"""
#Scenario: imagine you're beating a level in a video game and you just finish a level. this shows your final results in that level

#i picked a game's rating system because i more relate to it than grades. Plus, both rating are related in some ways
#because the game ratings were adopted from japanese school grading systems.

print("You have passed this Level")
score = 1500
#now, if i ever get a higher score than 1500. i would get a better rank
print("final_results:", score)

if score >= 2000:
    print("Rank: S")
elif score >= 1500:
    print("Rank: A")
elif score >= 1000:
    print("Rank: B")
elif score >= 550:
    print("Rank: C")
elif score >= 500:
    print("Rank: D")
elif score >= 450:
    print("Rank: F")
#if possible, put in crappy music when achieving F