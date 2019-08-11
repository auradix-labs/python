# Declare a class
class Post:
    # members - property and methods

    def __init__(self,id, msg, author,timestamp):
        #properties
        self.id=id
        self.message = msg
        self.author = author
        self.time_stamp= timestamp

    def __str__(self):
        return self.id + self.message

    # methods
    def update(self):
        print("post updated")

    def delete(self):
        print("post deleted")


