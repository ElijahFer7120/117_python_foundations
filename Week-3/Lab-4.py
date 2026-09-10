"""
Week 3 assignment 1

Purpose:
Show that functions can separate responsibilities in a small program.

developer notes
i'm going for a video game style system to make it more relatable for myself. 
"""



def calculate_average(score_1, score_2, score_3):
    total = score_1 + score_2 + score_3
    average = total / 3
    return average

def get_status(average):
    if average >= 1500:
        return "Accepted"
    else:
        return "Rejected"
    
def show_results(player_name, average, status):
    print("Player:", player_name)
    print("Average Score:", average)
    print("Status:", status)
    

name = "Nitrozeus"
average_score = calculate_average(1500, 1600, 1700)
student_status = get_status(average_score)
show_results(name, average_score, student_status)
