from tkinter import *
import random

# create window
root = Tk()
root.title("Random Card Picker")
root.geometry("900x500")
root.configure(background="green")

num_list =['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
shape_list =['spades','hearts','clubs','diamonds']
deck = []

for num in num_list:
    for shape in shape_list:
        deck.append((num, shape))

def draw():
    # num = random.choice(num_list)
    # shape = random.choice(shape_list)
    # card = num + '_of_' + shape
    # return card
    card = random.choice(deck)
    deck.remove(card)

    root.title('Random Card Picker - ' + str(len(deck)) + ' cards left')
    card_frame.config(text=card)
    card_label.config(text=card)

    return card

root_frame = Frame(root, bg="green")
root_frame.pack(pady=20)

# frames for cards
card_frame = LabelFrame(root_frame, text="", bd=0)
card_frame.grid(row=0, column=0, ipadx=20)

# adding cards into frames
card_label = Label(card_frame, text=' ')
card_label.pack(pady=20)

# create draw card button
button = Button(root, text='Draw Card', font=('Helvetica', 14), command=draw)
button.pack(pady=20)

# two step, define then put on screen
# myLabel = Label(root, text="hello world")

# pack - put on screen (shove at the first available spot)
# myLabel.pack()

# use grid system
# myLabel.grid(row=0, column=5)

# button
# myButton = Button(root, text="Draw Card", padx=50, pady=50)
# myButton.grid(row=0, column=0)

if __name__ == "__main__":
    # create event loop to keep GUI on
    root.mainloop()

