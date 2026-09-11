#tasks = []
##your dictionary list. 
#tasks.append("watch Kamen rider Zetz")
#tasks.append("complete Lab-7")
#tasks.append("do the dailies in my mobile games")
#tasks.append("finishing my projects")
##the simple function below the list
#print("tasks:")
#for task in tasks:
#    print("-", task)
## this one is a pretty neat way to track tasks in a one and done situation. it simply just 
##create a simple list, add items to it, and prints the item as intended.

class tasktracker:
    def __init__(self):
        self.tasks = []
#this one creates an empty lis
    def add_task(self, task):
        self.tasks.append(task)
#this adds a task to the list
#the self-task displays the tasks
    def show_tasks(self):
        print("tasks:")
        for task in self.tasks:
            print("-", task)
#and this one belongs to each tracker object individually
tracker = tasktracker()
tracker.add_task("watch Kamen rider Zetz")
tracker.add_task("complete Lab-7")
tracker.add_task("do the dailies in my mobile games")
tracker.add_task("finishing my projects")
tracker.show_tasks()

#meanwhile this task tracker has more complex functions to it but can be reused with a different list of task without changing the code as much
