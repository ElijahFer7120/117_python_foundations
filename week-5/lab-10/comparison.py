#this task demonstrates the comparison between a dictionary list and an object instance of a class

#this one is a simple dictionary list for ease of writing and storing data which makes it the easiest and simplest styles
dictionary_list = [
    {
        "task": "watch kamen rider my-th",
        "due": "within four weeks",
        "is it done?": False
    }
]

#this one however uses a class that can encapsulate the data and uses attributes to store and access the program. 
#it's hard at first but it can be learned easily with a bit of practice and useful for larger programs.
class Task:
    def __init__(self, task, due, is_it_done):
        self.task = task
        self.due = due
        self.is_it_done = is_it_done

object_task = Task("watch kamen rider my-th", "within four weeks", False)


print("DICTIONARY LIST")
print(dictionary_list[0]["task"], "-", dictionary_list[0]["due"], "-", dictionary_list[0]["is it done?"])

print("\nOBJECT TASK")
print(object_task.task, "|", object_task.due, "|", object_task.is_it_done)