from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('N64 Games')
root.geometry('800x600')

games = [
    {
        'title': 'Super Mario 64',
        'image': 'Super_Mario_64_box_cover.jpg',
        'description': 'Super Mario 64 is a 1996 platform game developed and published by Nintendo for the Nintendo 64. It is the first Super Mario game to use three-dimensional (3D) graphics.'
    }
]

def create_game_frame(game):
    # Load the game image
    image = Image.open(game['image'])

    # Create a frame for the game
    frame = Frame(root, bg='white')
    frame.pack(fill=BOTH, padx=10, pady=10)

    # Add the game image to the frame
    photo = ImageTk.PhotoImage(image)
    label = Label(frame, image=photo, bg='white')
    label.image = photo
    label.pack(side=LEFT)

    # Add the game buttons to the frame
    exit_button = Button(frame, text='Exit', command=root.quit)
    exit_button.pack(side=RIGHT, padx=10, pady=10)

    # Add the game title and description to the frame
    title = Label(frame, text=game['title'], font=('Arial', 11, 'bold'), bg='white')
    title.pack(side=TOP, anchor=W, padx=10, pady=10)
    description = Label(frame, text=game['description'], font=('Arial', 12), bg='white', wraplength=200)
    description.pack(side=LEFT, padx=10)
    
for game in games:
    create_game_frame(game)

# Define the view_more function
def view_more(game):
    # Create a new window
    new_window = Toplevel(root)

    # Set the window title
    new_window.title(game['title'])

    # Add the game title to the window
    title_label = Label(new_window, text=game['title'], font=('Arial', 20), bg='white')
    title_label.pack(pady=10)

    # Load the image for the game and add it to the window
    image = Image.open(game['image'])
    image = image.resize((300, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label = Label(new_window, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)


root.mainloop()