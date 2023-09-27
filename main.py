import time
from tkinter import *
from pandas import *
import random
current_card = {}
to_learn={}
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer=window.after(3000, func=english_card)



def english_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
def is_known():
    to_learn.remove(current_card)
    data=DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index=False)
    next_card()


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer=window.after(3000, func=english_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 283, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# UNKNOWN BUTTON
unknown_button_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
# KNOWN BUTTON
check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)
# French words

next_card()

# english_card()
window.mainloop()
