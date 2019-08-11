# Create,read , update, delete


'''to create a new post object'''
from SocialMedia.Post import Post
import datetime
from os import system, name

post_list = []


base_id = 0


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def create():
    # Take user inputs\
    global base_id
    id = base_id = base_id + 1
    message = input('Enter Message: ')
    author = input('Enter Author: ')
    # get current timestamp
    timestamp = datetime.datetime.now()
    # create a new post object
    post = Post(id, message, author, timestamp)
    # append the new object to the post_list
    post_list.append(post)


def readOne(post):
    print(str(post.id) + post.message + post.author + str(post.time_stamp))


def readAll():
    for post in post_list:
        readOne(post)


def edit():
    found = False
    edit_id = int(input('Enter the post id you want to edit: '))
    for post in post_list:
        if post.id == edit_id:
            found = True
            msg = input('Enter new post message')
            timestamp = datetime.datetime.now()
            # update the fields
            post.message = msg
            post.time_stamp = timestamp
            readOne(post)
            break
    if not found:
        print("Post with id ", edit_id, "was not found")



def search():
    search_id = int(input('Enter the post Id: '))
    for post in post_list:
        if post.id == search_id:
            return post
    return None


def delete():
    post = search()
    if post is not None:
        post_list.remove(post)



# Infinite loop
def save():
    db = open('mydb.txt','a+')
    db.write(post_list)
    db.close()


while True:
    print('1. Read All Post')
    print('2. Create New Post')
    print('3. Edit A Post')
    print('4. Delete A Post')
    print('5. Exit')
    choice = input("enter a choice: ")
    if choice == '1':
        readAll()
    elif choice == '2':
        create()
    elif choice == '3':
        edit()
    elif choice == '4':
        delete()
    elif choice == '5':
        save()
        break;

