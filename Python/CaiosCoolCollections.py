from tkinter import *
from tkinter import PhotoImage
m = Tk()

import random


global title, Game1, Game2, Game3, chosen_game
title = "Caio's Cool Collections"
m.title(title)
Game1 = "Quiz"
Game2 = "Wordle"
Game3 = "Hangman"
chosen_game = ""

#Setting window size
global width, height
width = 1080
height = 720
m.geometry("{}x{}".format(width, height))

#Button size
global button_width, button_height
button_width = 20
button_height = 5

#Initial Frame
global frame
frame = Frame(m)
frame.pack(pady=20)

#Tutorial Functions
def GK_tutorial():
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False) # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game1))
    tutorial_label = Label(tutorial_window, text="How to play: General Knowledge Quiz", font=("Arial", 16, "bold"))
    tutorial_label.pack(pady=10)
    tutorial_desc = Label(tutorial_window, text="This game is simple! You will be asked 10 randomly selected questions,\n"
    "and all you have to do is answer them correctly and you can get all the\n"
    "points!\n\nGood Luck!", font=("Arial", 12), justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Button(tutorial_window, text="OK", width=round(button_width/4), command=tutorial_window.destroy)
    ok_button.pack(pady=10)

def W_tutorial():
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False) # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game2))
    tutorial_label = Label(tutorial_window, text="How to play: Wordle", font=("Arial", 16, "bold"))
    tutorial_label.pack(pady=10)
    tutorial_desc = Label(tutorial_window, text="I'm sure you know how this goes, you will be given 6 chances to guess a 5 letter word.\n"
    "After each guess, the letters will change colour to show how close you are\n"
    "to guessing the word. green means the letter is in the correct position,\n"
    "yellow means the letter is in the word but in the wrong position,\n"
    "and grey means the letter is not in the word at all.\n\nGood Luck!", font=("Arial", 12), justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Button(tutorial_window, text="OK", width=round(button_width/4), command=tutorial_window.destroy)
    ok_button.pack(pady=10)

def HM_tutorial():
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False) # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game3))
    tutorial_label = Label(tutorial_window, text="Welcome to Hangman!", font=("Arial", 16, "bold"))
    tutorial_label.pack(pady=10)
    tutorial_desc = Label(tutorial_window, text="In this game, you will be given a word with missing letters.\n"
    "You have to guess the word by suggesting letters within a certain number of guesses.\n"
    "For each incorrect guess, a part of the hangman will be drawn.\n"
    "You have 6 incorrect guesses before the hangman is fully drawn and you lose!\n\nGood Luck!", font=("Arial", 12), justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Button(tutorial_window, text="OK", width=round(button_width/4), command=tutorial_window.destroy)
    ok_button.pack(pady=10)

#Scores Function
def Scores():
    scores_window = Toplevel(m)
    scores_window.title("Scores")
    scores_label = Label(scores_window, text="Scores", font=("Arial", 16, "bold"))
    scores_label.pack(pady=10)
    global player_name
    scores_desc = Label(scores_window, text="Welcome to Scores, {}! Here, you'll be able to see all the scores\n"
    "you've gotten throughout the three games available!".format(player_name), font=("Arial", 12), justify=LEFT)
    
    global Game1, Game2, Game3, GK_score, w_score
    #Checking scores
    if 'GK_score' in globals():
        if GK_score == 10:
            gk_colour = "green"
        else:
            gk_colour = "black"
    else:
        GK_score = 0
        gk_colour = "black"
    if 'w_score' not in globals():
        w_score = "no"
        att_txt = "attempts"
        w_colour = "black"
    else:
        w_colour = "green"
        if w_score == 1:
            att_txt = "attempt"
        else:
            att_txt = "attempts"
    
    scores_text1 = Label(scores_window, text="{}: {}/10".format(Game1, GK_score), font=("Arial", 12), fg=gk_colour, justify=CENTER)
    scores_text2 = Label(scores_window, text="{}: Solved in {} {}".format(Game2, w_score, att_txt), font=("Arial", 12), fg=w_colour, justify=CENTER)
    scores_text3 = Label(scores_window, text="{}: No scores yet!".format(Game3), font=("Arial", 12), justify=CENTER)
    ok_button = Button(scores_window, text="OK", width=round(button_width/4), command=scores_window.destroy)
    
    #Layout
    scores_desc.pack(padx=20, pady=20)
    scores_text1.pack(pady=10)
    scores_text2.pack(pady=10)
    scores_text3.pack(pady=10)
    ok_button.pack(pady=10)
#Game Functions
def GK_game():
    menu_frame.destroy()

    q_a = {
        "What is the closest planet to the sun?": "Mercury",
        "Who came up with the term 'debugbing'?": ["Grace Hopper", "Grace"],
        "What is the capital of New Zealand?": "Wellington",
        "What program was ChatGPT created on?": "Python",
        "What is the meaning of life, the universe and everything?": "42",
        "What does the acronym 'www' stand for?": "World Wide Web",
        "What is the name of the first 3D platforming video game?": "Super Mario 64",
        "What is the function to output text in Python?": "print",
        "Who is the most sassy teacher?": "Miss Chong",
        "What is the slang name for New York City?": ["The Big Apple", "Big Apple"],
        "What is a group of owls called?": ["A parliament"],
        "What is the symbol for iron on the periodic table?": "Fe",
        "What continent is the only one with land in all four hemispheres?": "Africa",
        "What is the hardest natural substance on Earth?": "Diamond",
        "What year was the official Minecraft release?": "2011",
        "What is the grass type pokemon starter from the third generation?": "Treecko",
        "What is the fire type pokemon starter from the third generation?": "Torchic",
        "What is the water type pokemon starter from the third generation?": "Mudkip",
        "What is the name of the tallest mountain in Japan?": "Mount Fuji",
        "What do you have to eat to keep the doctor away?": "An apple",
        "What is the name of the fairy in Peter Pan?": "Tinker Bell",
        "What is the name of the main character's partner in Breaking Bad?": ["Jesse Pinkman", "Jesse"],
    }

    #Collecting 10 random questions and their answers
    questions = []
    for x in range(10):
        rand_q = random.choice(list(q_a.keys()))
        while rand_q in questions:
            rand_q = random.choice(list(q_a.keys()))
        questions.append(rand_q)

    answers = []
    for question in questions:
        answers.append(q_a[question])

    global GK_frame, chosen_game
    chosen_game = "Quiz"
    GK_frame = Frame(m)
    GK_frame.pack(pady=50)

    GK_label = Label(GK_frame, text="General Knowledge Quiz", font=("Arial", 30, "bold"))

    #Function for what happens when you submit an answer
    def GK_submit():
        global answer_entry, error_mes, i, GK_score
        sub_answer = answer_entry.get()

        if len(sub_answer) > 0:
            if isinstance(answers[i], list): # For questions with multiple possible answers
                correct = False
                for ans in answers[i]:
                    if sub_answer.lower() in ans.lower():
                        correct = True
                        break
            else:
                if sub_answer.lower() == answers[i].lower():
                    correct = True
                else:
                    correct = False
            if correct:
                error_mes.destroy()
                error_mes = Label(GK_frame, text="Correct!  +1 point", font=("Arial", 16, "bold"), fg="green")
                error_mes.grid(row=4, column=0, columnspan=3)
                answer_entry.delete(0, END)
                GK_score += 1
                if i < 9:
                    GK_frame.after(1000, lambda: error_mes.config(text=""))
            else:
                error_mes.destroy()
                error_mes = Label(GK_frame, text="Incorrect!", font=("Arial", 16, "bold"), fg="red")
                error_mes.grid(row=4, column=0, columnspan=3)
                answer_entry.delete(0, END)
                if i < 9:
                    GK_frame.after(1000, lambda: error_mes.config(text=""))
            i += 1
            # Show next question
            if i < 10:
                chosen_question = questions[i]
                question_num.config(text="Question {}:".format(str(i+1)))
                question.config(text=chosen_question)
            else: # End of quiz
                error_mes.destroy()
                error_mes = Label(GK_frame, text="Quiz Over! You have completed all the questions.", font=("Arial", 18))
                error_mes.grid(row=4, column=0, columnspan=3)
                question_num.destroy()
                question.destroy()
                answer_label.destroy()
                answer_entry.destroy()
                answer_button.destroy()
                score_label = Label(GK_frame, text="Your final score is: {}/10".format(GK_score), font=("Arial", 16, "bold"))
                score_label.grid(row=5, column=0, columnspan=3, pady=20)
                if GK_score == 10:
                    result_label = Label(GK_frame, text="Perfect Score! Well done!", font=("Arial", 16, "bold"), fg="green")
                    result_label.grid(row=6, column=0, columnspan=3)
                elif GK_score >= 7:
                    result_label = Label(GK_frame, text="Great Job!", font=("Arial", 16, "bold"))
                    result_label.grid(row=6, column=0, columnspan=3)
                elif GK_score >= 4:
                    result_label = Label(GK_frame, text="Not bad, but you can do better!", font=("Arial", 16, "bold"))
                    result_label.grid(row=6, column=0, columnspan=3)
        else:
            error_mes.destroy()
            error_mes = Label(GK_frame, text="Please enter an answer before submitting.", font=("Arial", 12), fg="red")
            error_mes.grid(row=4, column=0, columnspan=3)

    global i, GK_score
    GK_score = 0
    i = 0
    chosen_question = questions[i]
    question_num = Label(GK_frame, text="Question {}:".format(str(i+1)), font=("Arial", 16))
    question = Label(GK_frame, text=chosen_question, font=("Arial", 20))
    answer_label = Label(GK_frame, text="Your Answer:", font=("Arial", 12))
    global answer_entry
    answer_entry = Entry(GK_frame, font=("Arial", 16))
    answer_button = Button(GK_frame, text="Submit", font=("Arial", 12), command=GK_submit)
    error_mes = Label(GK_frame, text="", font=("Arial", 12), fg="red")

    def on_enter_key(event):
        GK_submit()

    answer_entry.bind('<Return>', on_enter_key)

    global menu_exit
    menu_exit.config(text="Exit to Menu", command=exit_to_menu)

    #Layout
    GK_label.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=50)
    question_num.grid(row=1, column=0, columnspan=3, sticky=W+E)
    question.grid(row=2, column=0, columnspan=3, sticky=W+E)
    answer_label.grid(row=3, column=0, pady=30, sticky=E)
    answer_entry.grid(row=3, column=1, padx=10, sticky=W+E)
    answer_button.grid(row=3, column=2, sticky=W)
    error_mes.grid(row=4, column=0, columnspan=3)

def W_Game():
    menu_frame.destroy()

    #Resizing window
    global width, height
    m.geometry("{}x{}".format(width, round(height*1.2)))

    global w_frame, chosen_game, w_score, w_desc, num
    w_score = 0
    num = 0
    chosen_game = "Wordle"
    w_frame = Frame(m)
    w_frame.pack(pady=35)
    
    w_label = Label(w_frame, text="Wordle", font=("Arial", 30, "bold"))
    w_desc = Label(w_frame, text="Guess the 5-letter word:", font=("Arial", 16))
    

    #words list (45 5-letter words)
    words = ["blade", "crane", "flint", "grape", "house", "jumpy", "knock", "light", "mango", "night", 
    "ocean", "plant", "queen", "river", "stone", "table", "under", "vivid", "whale", "zesty", "pinky", 
    "cloud", "brave", "charm", "dwarf", "eagle", "frost", "glove", "honey", "ivory", "jewel", "lunar",
    "magic", "noble", "orbit", "pearl", "quest", "royal", "sugar", "tiger", "urban", "vapor", "waltz",
    "crash", "drink"]

    #Function for what happens when you submit a word
    def w_submit():
        global w_entry, error_mes, attempts, attempts_label, w_desc, answer_button, num
        sub_word = w_entry.get()
        if len(sub_word) != 5:
            error_mes.destroy()
            error_mes = Label(w_frame, text="Please enter a 5-letter word.", font=("Arial", 12), fg="red")
            error_mes.grid(row=3, column=0, columnspan=2)
            w_frame.after(2000, lambda: error_mes.config(text=""))
        elif not sub_word.isalpha():
            error_mes.destroy()
            error_mes = Label(w_frame, text="Please enter only letters.", font=("Arial", 12), fg="red")
            error_mes.grid(row=3, column=0, columnspan=2)
            w_frame.after(2000, lambda: error_mes.config(text=""))
        else:
            sub_word = sub_word.lower()
            if sub_word == chosen_word:
                attempts -= 1
                error_mes.destroy()
                w_desc.destroy()
                answer_button.destroy()
                w_entry.destroy()
                error_mes = Label(w_frame, text="Congratulations! You've guessed the word!", font=("Arial", 16, "bold"), fg="green")
                error_mes.grid(row=3, column=0, columnspan=2)
                attempts_label.destroy()
                global w_score
                w_score = start_attempts - attempts
                if w_score == 1:
                    att_txt = "attempt"
                else:
                    att_txt = "attempts"
                if w_score == 6:
                    extra_text = "Phew!"
                else:
                    extra_text = "Great job!"
                score_label = Label(w_frame, text="You found the word in {} {}!\n{}".format(w_score, att_txt, extra_text), font=("Arial", 16, "bold"))
                score_label.grid(row=4, column=0, columnspan=3, pady=20)
            elif attempts > 1:
                attempts -= 1
                attempts_label.destroy()
                attempts_label = Label(w_frame, text="Attemps: {}".format(attempts), font=("Arial", 12))
                attempts_label.grid(row=4, column=0, columnspan=3, pady=10)
                w_entry.delete(0, END)
            else:
                error_mes.destroy()
                error_mes = Label(w_frame, text=f"Game Over! The word was '{chosen_word}'.", font=("Arial", 16, "bold"))
                error_mes.grid(row=3, column=0, columnspan=2, pady=10)
                w_desc.destroy()
                w_entry.destroy()
                answer_button.destroy()
                attempts_label.destroy()
            
            #Displaying the guessed letters with colours
            display_col = []
            for i in range(5):
                letter = sub_word[i]
                correct_letter = chosen_word[i]
                if letter == correct_letter:
                    display_col.append("green")
                elif letter in chosen_word:
                    if sub_word.count(letter) > chosen_word.count(letter):

                        for j in range(5):
                            d_letter = sub_word[j]
                            if d_letter == letter and j != i:
                                if d_letter == correct_letter:
                                    display_col.append("grey")
                                else:
                                    if j < i:
                                        display_col.append("grey")
                                    else:
                                        display_col.append("orange")
                    else:
                        display_col.append("orange")
                else:
                    display_col.append("grey")

            #Displaying the guessed letters
            i = 0
            def show_delayed_letters(num, sub_word, display_col):
                nonlocal i
                if i < 5:
                    letter_label = Label(word_frame, text=sub_word[i].upper(), font=("Arial", 20), width=4, height=2, bg=display_col[i], fg="white")
                    letter_label.grid(row=num, column=i, padx=2, pady=2)
                    w_frame.after(100, lambda: show_delayed_letters(num, sub_word, display_col))
                    i += 1
            show_delayed_letters(num, sub_word, display_col)
            num += 1

    chosen_word = random.choice(words)
    print(chosen_word) #For testing purposes, to be removed later
    global w_entry, answer_button, error_mes, attempts, attempts_label
    start_attempts = 6 # Number of attempts
    attempts = 6
    w_entry = Entry(w_frame, font=("Arial", 16))
    answer_button = Button(w_frame, text="Submit", font=("Arial", 12), command=w_submit)
    error_mes = Label(w_frame, text="", font=("Arial", 12), fg="red")
    attempts_label = Label(w_frame, text="Attemps: {}".format(attempts), font=("Arial", 12))
    
    #Layout
    w_label.grid(row=0, column=0, columnspan=2, sticky=W+E, pady=20)
    w_desc.grid(row=1, column=0, columnspan=2, sticky=W+E)    
    w_entry.grid(row=2, column=0, pady=10)
    answer_button.grid(row=2, column=1, pady=10, padx=10, sticky=W)
    error_mes.grid(row=3, column=0, columnspan=2)
    attempts_label.grid(row=4, column=0, columnspan=2, pady=10)

    def on_enter_key(event):
        w_submit()
    w_entry.bind('<Return>', on_enter_key)

    word_frame = Frame(w_frame)
    word_frame.grid(row=5, column=0, columnspan=2)
    for i in range(6):
        for j in range(5):
            letter_label = Label(word_frame, text="", font=("Arial", 20), width=4, height=2, bg="#3B3B3B")
            letter_label.grid(row=i, column=j, padx=2, pady=2)

    global menu_exit
    menu_exit.config(text="Exit to Menu", command=exit_to_menu)

def HM_Game():
    menu_frame.destroy()
    global chosen_game, hm_frame, content_frame, hm_entry, hm_score
    chosen_game = "Hangman"
    hm_frame = Frame(m)
    hm_frame.pack(pady=(40,10))
    content_frame = Frame(m)
    hm_score = 6

    #Words list 30 words
    words = ["python", "javascript", "hangman", "programming", "developer", "function",
            "variable", "Photo", "testing", "collections", "challenge", "interface",
            "stickman", "wizard", "puzzle", "mystery", "adventure", "treasure",
            "dragon", "castle", "forest", "mountain", "river", "ocean", "island",
            "extreme", "intergalactic", "fantasy", "galaxy", "supercalifragilistic"]
    chosen_word = random.choice(words)
    print(chosen_word) #For testing purposes, to be removed later

    #Function for what happens when you submit a letter
    def hm_submit():
        global hm_entry, error_mes, hm_submit_button, hidden_word, img_level, img
        global stickman_label, used_letters_label, hm_score, wrong_letters, used_letters_desc, hm_desc
        sub_letter = hm_entry.get()
        sub_letter = sub_letter.lower()
        if len(sub_letter) != 1:
            error_mes.destroy()
            error_mes = Label(hm_frame, text="Please enter a single letter.", font=("Arial", 12), fg="red")
            error_mes.grid(row=3, column=0, columnspan=2)
            hm_frame.after(2000, lambda: error_mes.config(text=""))
        elif not sub_letter.isalpha():
            error_mes.destroy()
            error_mes = Label(hm_frame, text="Please enter a letter (a-z).", font=("Arial", 12), fg="red")
            error_mes.grid(row=3, column=0, columnspan=2)
            hm_frame.after(2000, lambda: error_mes.config(text=""))
        elif sub_letter in hidden_word or sub_letter in wrong_letters:
            error_mes.destroy()
            error_mes = Label(hm_frame, text="You've already guessed that letter.", font=("Arial", 12), fg="red")
            error_mes.grid(row=3, column=0, columnspan=2)
            hm_frame.after(2000, lambda: error_mes.config(text=""))
        else:
            if sub_letter in chosen_word:
                for i, letter in enumerate(chosen_word):
                    if letter == sub_letter:
                        sub_letter = sub_letter.upper()
                        hidden_word[i] = sub_letter
                hm_entry.delete(0, END)
                error_mes.destroy()
                error_mes = Label(hm_frame, text="Correct!", font=("Arial", 12, "bold"), fg="green")
                error_mes.grid(row=3, column=0, columnspan=2)
                hm_frame.after(1000, lambda: error_mes.config(text=""))
                hm_word_label.config(text=" ".join(hidden_word))
                if "_" not in hidden_word:
                    error_mes.destroy()
                    error_mes = Label(hm_frame, text="Congratulations! You've guessed the word!", font=("Arial", 16, "bold"), fg="green")
                    error_mes.grid(row=3, column=0, columnspan=2)
                    hm_entry.destroy()
                    hm_submit_button.destroy()
                    hm_desc.destroy()
            else:
                sub_letter = sub_letter.upper()
                wrong_letters.append(sub_letter)
                used_letters_desc.config(text=wrong_letters)
                hm_entry.delete(0, END)
                error_mes.destroy()
                error_mes = Label(hm_frame, text="Incorrect!", font=("Arial", 12), fg="red")
                error_mes.grid(row=3, column=0, columnspan=2)
                hm_frame.after(1000, lambda: error_mes.config(text=""))
                hm_score -= 1
                img_level += 1
                img_path = "Stickman{}.png".format(img_level)
                img = PhotoImage(file=img_path)
                stickman_label.config(image=img)
                stickman_label.image = img
                if hm_score == 0:
                    error_mes.destroy()
                    error_mes = Label(hm_frame, text="Game Over! The word was '{}'.".format(chosen_word), font=("Arial", 16, "bold"))
                    error_mes.grid(row=3, column=0, columnspan=2)
                    hm_entry.destroy()
                    hm_submit_button.destroy()

    global hm_desc, hm_entry, hm_submit_button, error_mes
    hm_label = Label(hm_frame, text="Hangman", font=("Arial", 30, "bold"))
    hm_desc = Label(hm_frame, text="Enter a letter to guess the word:", font=("Arial", 16))
    hm_entry = Entry(hm_frame, font=("Arial", 16), width=5)
    hm_submit_button = Button(hm_frame, text="Submit", font=("Arial", 12), command=hm_submit)
    error_mes = Label(hm_frame, text="", font=("Arial", 12), fg="red")
    
    global hidden_word, img_level, img, stickman_label, used_letters_label, wrong_letters, used_letters_desc
    
    # Content: Hidden word (left), Stickman (right)
    wrong_letters = []
    hidden_word = ["_"] * len(chosen_word)
    hm_word_label = Label(content_frame, text=" ".join(hidden_word), font=("Arial", 24))
    used_letters_label = Label(content_frame, text="Wrong letters:", font=("Arial", 12), justify=CENTER)
    used_letters_desc = Label(content_frame, text=wrong_letters, font=("Arial", 12), justify=CENTER)
    
    img_level = 0 #Stickman image level
    img_path = "Stickman{}.png".format(img_level) #Initial stickman image
    img = PhotoImage(file=img_path) 
    stickman_label = Label(content_frame, image=img, width=200, height=350)
    stickman_label.image = img

    #Layout
    hm_label.grid(row=0, column=0, columnspan=2, sticky=W+E, pady=30)
    hm_desc.grid(row=1, column=0, columnspan=2, sticky=W+E)
    hm_entry.grid(row=2, column=0, pady=5, sticky=E)
    hm_submit_button.grid(row=2, column=1, pady=5, sticky=W, padx=10)
    error_mes.grid(row=3, column=0, columnspan=2)
    content_frame.pack()

    hm_word_label.grid(row=0, column=0, sticky=W+E, padx=50)
    stickman_label.grid(row=0, rowspan=3, column=1, sticky=E)
    used_letters_label.grid(row=1, column=0, sticky=W+E)
    used_letters_desc.grid(row=2, column=0, sticky=W+E)
    
    global menu_exit
    menu_exit.config(text="Exit to Menu", command=exit_to_menu)

def exit_to_menu():
    global chosen_game
    if chosen_game == "Quiz":
        GK_frame.destroy()
    elif chosen_game == "Wordle":
        w_frame.destroy()
    elif chosen_game == "Hangman":
        hm_frame.destroy()
        content_frame.destroy()
    menu_exit.destroy()
    open_menu()

#Prgram Menu
def tutorial_menu():
    menu = Menu(m)
    m.config(menu=menu)
    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Tutorial", menu=help_menu)
    help_menu.add_command(label="How to play: {}".format(Game1), command=GK_tutorial)
    help_menu.add_command(label="How to play: {}".format(Game2), command=W_tutorial)
    help_menu.add_command(label="How to play: {}".format(Game3), command=HM_tutorial)

#Open Menu function
def open_menu():
    tutorial_menu()
        
    frame.destroy()
    global menu_frame, Game1, Game2, Game3, player_name
    menu_frame = Frame(m)
    menu_frame.pack(pady=20)

    global width, height
    m.geometry("{}x{}".format(width, height))

    #Program Title
    if "Caio" in player_name.title():
        text = "Welcome, Creator!"
    elif "Chong" in player_name.title():
        text = "Welcome, miss!"
    elif "Ethan" in player_name.title():
        text = "Get out of my program, Ethan."
    else:
        text = "Welcome, {}!".format(player_name)
    welcome_label = Label(menu_frame, text=text, font=("Arial", 18))
    label = Label(menu_frame, text="Caio's Cool Collections", font=("Arial", 35))

    #Menu Buttons
    menu_button1 = Button(menu_frame, text=Game1, width=button_width, height=button_height, command=GK_game)
    menu_button2 = Button(menu_frame, text=Game2, width=button_width, height=button_height, command=W_Game)
    menu_button3 = Button(menu_frame, text=Game3, width=button_width, height=button_height, command=HM_Game)
    scores_button = Button(menu_frame, text="Scores", width=button_width, height=round(button_height/1.5), command=Scores)
    global menu_exit
    menu_exit = Button(m, text="Exit Program", command=m.quit, width=button_width, height=round(button_height/2))

    #program layout
    welcome_label.grid(row=0, column=0, columnspan=3, sticky=W+E)
    label.grid(row=1, column=0, columnspan=3, sticky=W+E, pady=20)
    menu_button1.grid(row=2, column=0, pady=30)
    menu_button2.grid(row=2, column=1, padx=40)
    menu_button3.grid(row=2, column=2)
    scores_button.grid(row=3, column=0, columnspan=3, pady=30, sticky=W+E)
    menu_exit.pack(fill=Y, side=BOTTOM, pady=20, padx=button_width*5)


#Menu function
def menu():
    global player_name, name_entry
    player_name = name_entry.get()
    player_name = player_name.title()
    
    if name_entry.get() == "":
        global error_mes
        error_mes.config(text="Please enter a name to continue.")
        frame.after(2000, lambda: error_mes.config(text=""))
    else:
        open_menu()

#Beginning message

title = Label(frame, text="Welcome to Caio's Cool Collections!", font=("Arial", 30), justify=CENTER)
subtext = Label(frame, text="Before we begin, please enter your name below:", font=("Arial", 18), justify=CENTER)
title.pack(pady=(50,20))
subtext.pack(pady=(20,50))
global name_entry
name_entry = Entry(frame, font=("Arial", 16))
enter_button = Button(frame, text="Enter", font=("Arial", 12), command=menu)
error_mes = Label(frame, text="", font=("Arial", 12), fg="red")
error_mes.pack(pady=10)
name_entry.pack()
enter_button.pack(pady=20)

def on_enter_key(event):
    menu()
name_entry.bind('<Return>', on_enter_key)

m.mainloop()
