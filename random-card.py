from tkinter import *
import random
from PIL import ImageTk, Image

# create window
root = Tk()
root.title("Random Card Picker")
root.geometry("400x425")
root.configure(background="green")

num_list =['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
shape_list =['spades','hearts','clubs','diamonds']
deck = []

for num in num_list:
    for shape in shape_list:
        deck.append((num, shape))

def get_image(card):
    # use 2nd image if picture card
    if card[0] in ('jack','queen','king'):
        file_name = card[0] + '_of_' + card[1] + '2.png'
    else:
        file_name = card[0] + '_of_' + card[1] + '.png'

    # find and open image
    card_img = Image.open('images/' + file_name)
    
    card_img_resized = card_img.resize((150,218))

    global out_card_img
    out_card_img = ImageTk.PhotoImage(card_img_resized)

    return out_card_img

def draw():
    card = random.choice(deck)
    deck.remove(card)

    if len(deck) > 0:
        root.title('Random Card Picker - ' + str(len(deck)) + ' cards left')
        card_frame.config(text=card[0].capitalize() + ' of ' + card[1].capitalize())

        card_img = get_image(card)
        card_label.config(image=card_img)
    else:
        text = 'No cards left!'
        card_label.config(text=text)
        root.title('Random Card Picker - ' + text)
        button.config(state=DISABLED)

    return card

root_frame = Frame(root, bg="green")
root_frame.pack(pady=20)

# frames for cards
card_frame = LabelFrame(root_frame, text='', bd=0)
card_frame.grid(row=0, column=0, ipadx=20)

# adding cards into frames
card_label = Label(card_frame, text=' ')
card_label.pack(pady=20)

# create draw card button
button = Button(root, text='Draw Card', font=('Helvetica', 14), command=draw)
button.pack(pady=20)

if __name__ == "__main__":
    # create event loop to keep GUI on
    root.mainloop()

