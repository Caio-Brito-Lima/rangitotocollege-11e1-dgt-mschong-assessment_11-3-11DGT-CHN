"""DGT Assessment 11, Caio's Cool Collections.

This program contains 3 mini games:

A general knowledge quiz, wordle and a hangman game.
"""
import random
from tkinter import *
from tkinter import PhotoImage
m = Tk()

global title, Game1, Game2, Game3, chosen_game
global colours, GK_highscore, w_highscore, hm_highscore
global GK_played, w_played, hm_played
title = "Caio's Cool Collections"
m.title(title)
Game1 = "Quiz"
Game2 = "Wordle"
Game3 = "Hangman"
GK_highscore, w_highscore, hm_highscore = 0, 0, 0
GK_played, w_played, hm_played = False, False, False
chosen_game = ""
colours = {"blue": "#47AAAE",
           "dblue": "#358282",
           "red": "#FF5E5B",
           "dred": "#BE514B",
           "white": "#FFFFEA",
           "grey": "#ACBCA5",
           "dgrey": "#808276",
           "yellow": "#FFED66",
           "dyellow": "#F7A160"}
m.config(bg=colours["white"])

# Setting window size
global width, height
width = 1080
height = 720
m.geometry("{}x{}".format(width, height))

# Button size
global button_width, button_height
button_width = 20
button_height = 5

# Initial Frame
global frame
frame = Frame(m)
frame.pack(pady=80)
frame.config(bg=colours["white"])

# Tutorial Functions


def gk_tutorial():
    """Tutorial window for General Knowledge Quiz."""
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False)  # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game1))
    tutorial_label = Label(tutorial_window, text="How to play:"
                           "\nGeneral Knowledge Quiz",
                           font=("Arial", 16, "bold"), justify=CENTER)
    tutorial_label.pack(pady=(40, 20))
    tutorial_desc = Label(tutorial_window, text="This game is simple!\n"
                          "You will be asked 10 randomly selected questions, "
                          "and all you have to do is answer them correctly"
                          "and you can get all the points!\n\nGood Luck!",
                          font=("Arial", 12),
                          justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Label(tutorial_window, text="OK", font=("Arial", 12, "bold"))
    ok_button.bind('<Button-1>', lambda e: tutorial_window.destroy())
    ok_button.pack(fill=Y, side=BOTTOM, pady=20, padx=button_width*5)

    # Colour config
    tutorial_window.config(bg=colours["white"])
    tutorial_label.config(bg=colours["white"], fg="black")
    tutorial_desc.config(bg=colours["white"], fg=colours["dblue"],
                         wraplength=400)
    ok_button.config(bg=colours['red'], fg='white',
                     width=round(button_width/2),
                     height=2, bd=3, relief="solid")


def w_tutorial():
    """Tutorial window for Wordle."""
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False)  # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game2))
    tutorial_label = Label(tutorial_window, text="How to play:\nWordle",
                           font=("Arial", 16, "bold"), justify=CENTER)
    tutorial_label.pack(pady=(40, 20))
    tutorial_desc = Label(tutorial_window, text="I'm sure you know how this "
                          "goes, you will be given 6 chances to guess a 5 "
                          "letter word. After each guess, the letters "
                          "will change colour to show how close you are "
                          "to guessing the word. blue means the letter"
                          "is in the correct position, yellow means the"
                          " letter is in the word but in the wrong "
                          "position, and grey means the letter is not"
                          " in the word at all.\n\nGood Luck!",
                          font=("Arial", 12), justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Label(tutorial_window, text="OK", font=("Arial", 12, "bold"))
    ok_button.bind('<Button-1>', lambda e: tutorial_window.destroy())
    ok_button.pack(fill=Y, side=BOTTOM, pady=20, padx=button_width*5)

    # Colour config
    tutorial_window.config(bg=colours["white"])
    tutorial_label.config(bg=colours["white"], fg="black")
    tutorial_desc.config(bg=colours["white"], fg=colours["dblue"],
                         wraplength=400)
    ok_button.config(bg=colours['red'], fg='white',
                     width=round(button_width/2),
                     height=2, bd=3, relief="solid")


def hm_tutorial():
    """Tutorial window for Hangman."""
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False)  # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game3))
    tutorial_label = Label(tutorial_window, text="How to play:\nHangman",
                           font=("Arial", 16, "bold"))
    tutorial_label.pack(pady=(40, 20))
    tutorial_desc = Label(tutorial_window, text="In this game, you will "
                          "be given a word with missing letters. You have to"
                          " guess the word by suggesting letters within a"
                          " certain number of guesses. For each incorrect"
                          " guess, a part of the hangman will be drawn."
                          " You have 6 incorrect guesses before the "
                          "hangman is fully drawn and you lose!\n\nGood "
                          "Luck!", font=("Arial", 12),
                          justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Label(tutorial_window, text="OK", font=("Arial", 12, "bold"))
    ok_button.bind('<Button-1>', lambda e: tutorial_window.destroy())
    ok_button.pack(fill=Y, side=BOTTOM, pady=20, padx=button_width*5)

    # Colour config
    tutorial_window.config(bg=colours["white"])
    tutorial_label.config(bg=colours["white"], fg="black")
    tutorial_desc.config(bg=colours["white"], fg=colours["dblue"],
                         wraplength=400)
    ok_button.config(bg=colours['red'], fg='white',
                     width=round(button_width/2),
                     height=2, bd=3, relief="solid")

# Scores Function


def scores():
    """Highscores window."""
    scores_window = Toplevel(m)
    scores_window.geometry("500x420")
    scores_window.title("Highscores")
    scores_label = Label(scores_window, text="Highscores",
                         font=("Arial", 20, "bold"))
    scores_label.pack(pady=(40, 10))
    global player_name
    scores_desc = Label(scores_window, text="Welcome to Highscores, {}! "
                        "Here, you'll be able to see all the highscores "
                        "you've gotten throughout the three games "
                        "available!".format(player_name),
                        font=("Arial", 12), justify=LEFT)

    global Game1, Game2, Game3
    global GK_highscore, w_highscore, hm_highscore, hm_played

    # Checking quiz score
    if 'GK_score' in globals():
        global GK_score
        if GK_highscore > 8:
            gk_colour = colours["dblue"]
        else:
            gk_colour = "black"
    else:
        GK_score = 0
        gk_colour = "black"
    # Checking wordle score
    if 'w_score' not in globals():
        global w_score
        w_score = 0
        att_txt = "attempts"
        w_colour = "black"
    else:
        if w_highscore > 0:
            w_colour = colours["dblue"]
        else:
            w_colour = "black"
        if w_highscore == 1:
            att_txt = "attempt"
        else:
            att_txt = "attempts"
    # Checking hangman score
    if 'hm_score' in globals() and 'hm_played' in globals():
        global hm_score
        if hm_played is True:
            hm_colour = colours["dblue"]
            if hm_highscore == 1:
                letters_txt = "letter"
            else:
                letters_txt = "letters"
        else:
            hm_colour = "black"
            letters_txt = "letters"
    else:
        hm_score = 0
        letters_txt = "letters"
        hm_colour = "black"

    scores_text1 = Label(scores_window, text="{}: {}/10".format(Game1,
                                                                GK_highscore),
                         font=("Arial", 12, "bold"), fg=gk_colour,
                         justify=CENTER)
    scores_text2 = Label(scores_window, text="{}: Solved "
                                             "in {} {}".format(Game2,
                                                               w_highscore,
                                                               att_txt),
                         font=("Arial", 12, "bold"), fg=w_colour,
                         justify=CENTER)
    scores_text3 = Label(scores_window, text="{}: Solved with {} "
                                             "{}".format(Game3,
                                                         hm_highscore,
                                                         "wrong "
                                                         ""+letters_txt),
                         font=("Arial", 12, "bold"), fg=hm_colour,
                         justify=CENTER)
    ok_button = Label(scores_window, text="OK", font=("Arial", 12, "bold"))
    ok_button.bind('<Button-1>', lambda e: scores_window.destroy())

    # Layout
    scores_desc.pack(padx=20, pady=20)
    scores_text1.pack(pady=10)
    scores_text2.pack(pady=10)
    scores_text3.pack(pady=10)
    ok_button.pack(fill=Y, side=BOTTOM, pady=20, padx=button_width*5)

    # Colour config
    scores_window.config(bg=colours["white"])
    scores_label.config(bg=colours["white"], fg="black")
    scores_desc.config(bg=colours["white"], fg=colours["dblue"],
                       wraplength=400)
    scores_text1.config(bg=colours["white"])
    scores_text2.config(bg=colours["white"])
    scores_text3.config(bg=colours["white"])
    ok_button.config(bg=colours['red'], fg='white',
                     width=round(button_width/2),
                     height=round(button_height/2), bd=3, relief="solid")

# Game Functions


def gk_game():
    """General Knowledge Quiz game function."""
    menu_frame.destroy()

    q_a = {
        "What is the closest planet to the sun?": "Mercury",
        "Who came up with the term 'debugbing'?": ["Grace Hopper", "Grace"],
        "What is the capital of New Zealand?": "Wellington",
        "What program was ChatGPT created on?": "Python",
        "What is the meaning of life, the universe and everything?": "42",
        "What does the acronym 'www' stand for?": "World Wide Web",
        "What is the name of the first 3D "
        "platforming video game?": "Super Mario 64",
        "What is the function to output text in Python?": "print",
        "Who is the most sassy teacher?": "Miss Chong",
        "What is the slang name for New York City?": ["The Big Apple",
                                                      "Big Apple"],
        "What is a group of owls called?": ["A parliament", "Parliament"],
        "What is the symbol for iron on the periodic table?": "Fe",
        "What continent is the only one "
        "with land in all four hemispheres?": "Africa",
        "What is the hardest natural substance on Earth?": "Diamond",
        "What year was the official Minecraft release?": "2011",
        "What is the largest mammal in the world?": "Blue Whale",
        "What are the first 6 digits of pi?": "3.14159",
        "True or False: Have you eaten an onion today?": ["True", "False"],
        "What is the name of the tallest mountain in Japan?": "Mount Fuji",
        "What do you have to eat to keep the doctor away?": ["An apple",
                                                             "Apple"],
        "What is the name of the fairy in Peter Pan?": "Tinker Bell",
        "What is the name of the main character's partner in Breaking Bad?":
        ["Jesse Pinkman", "Jesse"],
    }

    # Collecting 10 random questions and their answers
    questions = []
    for x in range(10):
        rand_q = random.choice(list(q_a.keys()))
        while rand_q in questions:
            rand_q = random.choice(list(q_a.keys()))
        questions.append(rand_q)

    answers = []
    for question in questions:
        answers.append(q_a[question])

    global gk_frame, chosen_game, colours, help_label

    # Help label
    help_label = Label(m, text="?", font=("Arial", 12))
    help_label.bind('<Button-1>', lambda e: gk_tutorial())
    help_label.pack(fill=Y, side=TOP, pady=10, padx=10,
                    anchor=W)
    help_label.config(bg=colours["yellow"], fg="black",
                      width=4, height=2, bd=2, relief="solid")

    chosen_game = "Quiz"
    gk_frame = Frame(m)
    gk_frame.pack(pady=10)

    gk_label = Label(gk_frame, text="General Knowledge Quiz",
                     font=("Arial", 30, "bold"))
    # Function for what happens when you submit an answer

    def gk_submit():
        """Submit function for General Knowledge Quiz."""
        global answer_entry, error_mes, i, GK_score
        sub_answer = answer_entry.get()

        if len(sub_answer) > 0:
            if isinstance(answers[i], list):
                # For questions with multiple possible answers
                correct = False
                for ans in answers[i]:
                    if sub_answer.lower() == ans.lower():
                        correct = True
                        break
            else:
                if sub_answer.lower() == answers[i].lower():
                    correct = True
                else:
                    correct = False
            if correct:
                error_mes.destroy()
                error_mes = Label(gk_frame, text="Correct!",
                                  font=("Arial", 16, "bold"))
                error_mes.grid(row=4, column=0, columnspan=3)
                error_mes.config(bg=colours["white"], fg=colours["blue"])
                answer_entry.delete(0, END)
                GK_score += 1
                if i < 9:
                    gk_frame.after(1000, lambda: error_mes.config(text=""))
            else:
                error_mes.destroy()
                error_mes = Label(gk_frame, text="Incorrect!",
                                  font=("Arial", 16, "bold"))
                error_mes.grid(row=4, column=0, columnspan=3)
                error_mes.config(bg=colours["white"], fg=colours["red"])
                answer_entry.delete(0, END)
                if i < 9:
                    gk_frame.after(1000, lambda: error_mes.config(text=""))
            i += 1
            # Show next question
            if i < 10:
                chosen_question = questions[i]
                question_num.config(text="Question {}:".format(str(i+1)))
                question.config(text=chosen_question)
            else:  # End of quiz
                error_mes.destroy()
                error_mes = Label(gk_frame,
                                  text="Quiz Over! You have "
                                       "completed all the questions.",
                                       font=("Arial", 18))
                error_mes.grid(row=4, column=0, columnspan=3)
                error_mes.config(bg=colours["white"], fg="black")
                question_num.destroy()
                question.destroy()
                answer_label.destroy()
                answer_entry.destroy()
                answer_button.destroy()
                score_label = Label(gk_frame, text="Your final score is: "
                                    "{}/10".format(GK_score),
                                    font=("Arial", 16, "bold"))
                score_label.grid(row=5, column=0, columnspan=3, pady=20)
                score_label.config(bg=colours["white"], fg="black")
                if GK_score == 10:
                    result_label = Label(gk_frame, text="Perfect Score!"
                                         " Well done!",
                                         font=("Arial", 16, "bold"))
                    result_label.grid(row=6, column=0, columnspan=3)
                    result_label.config(bg=colours["white"],
                                        fg=colours["blue"])
                elif GK_score >= 7:
                    result_label = Label(gk_frame, text="Great Job!",
                                         font=("Arial", 16, "bold"))
                    result_label.grid(row=6, column=0, columnspan=3)
                    result_label.config(bg=colours["white"],
                                        fg=colours["dblue"])
                elif GK_score >= 4:
                    result_label = Label(gk_frame, text="Not bad, but "
                                         "you can do better!",
                                         font=("Arial", 16, "bold"))
                    result_label.grid(row=6, column=0, columnspan=3)
                    result_label.config(bg=colours["white"], fg="black")
                # highscore
                global GK_highscore, GK_played
                if GK_played is False:
                    GK_highscore = GK_score
                    high_score_label = Label(gk_frame,
                                             text="New Highscore!",
                                             font=("Arial", 16, "bold"))
                    high_score_label.grid(row=7, column=0, columnspan=3)
                    high_score_label.config(bg=colours["white"],
                                            fg=colours["dblue"])
                else:
                    if GK_score > GK_highscore:
                        GK_highscore = GK_score
                        high_score_label = Label(gk_frame,
                                                 text="New Highscore!",
                                                 font=("Arial", 16, "bold"))
                        high_score_label.grid(row=7, column=0, columnspan=3)
                        high_score_label.config(bg=colours["white"],
                                                fg=colours["dblue"])
                GK_played = True
        else:
            error_mes.destroy()
            error_mes = Label(gk_frame,
                              text="Please enter an answer "
                                   "before submitting.",
                                   font=("Arial", 12))
            error_mes.grid(row=4, column=0, columnspan=3)
            error_mes.config(bg=colours["white"], fg=colours["red"])

    global i, GK_score
    GK_score = 0
    i = 0
    chosen_question = questions[i]
    question_num = Label(gk_frame, text="Question {}:".format(str(i+1)),
                         font=("Arial", 16))
    question = Label(gk_frame, text=chosen_question,
                     font=("Arial", 20, "bold"))
    answer_label = Label(gk_frame, text="Answer:", font=("Arial", 12, "bold"))
    global answer_entry
    answer_entry = Entry(gk_frame, font=("Arial", 16))
    answer_button = Label(gk_frame, text="Submit", font=("Arial", 12, "bold"),
                          bd=2, relief="solid")
    answer_button.bind('<Button-1>', lambda e: gk_submit())
    error_mes = Label(gk_frame, text="", font=("Arial", 12))


    def on_enter_key(event):
        """Move on when pressing enter"""
        gk_submit()
    answer_entry.bind('<Return>', on_enter_key)

    global menu_exit
    menu_exit.config(text="Exit to Menu")
    menu_exit.bind('<Button-1>', lambda event: exit_to_menu())

    # Layout
    gk_label.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=50)
    question_num.grid(row=1, column=0, columnspan=3, sticky=W+E)
    question.grid(row=2, column=0, columnspan=3, sticky=W+E)
    answer_label.grid(row=3, column=0, pady=30, sticky=E)
    answer_entry.grid(row=3, column=1, padx=10, sticky=W+E)
    answer_button.grid(row=3, column=2, sticky=W)
    error_mes.grid(row=4, column=0, columnspan=3)

    # Colour config
    gk_frame.config(bg=colours["white"])
    gk_label.config(bg=colours["white"], fg="black")
    question_num.config(bg=colours["white"], fg=colours["dblue"])
    question.config(bg=colours["white"], fg="black", wraplength=800)
    answer_label.config(bg=colours["white"], fg="black")
    answer_entry.config(bg=colours["yellow"], fg="black", bd=3,
                        relief="solid",
                        highlightthickness=0, insertbackground="black")
    answer_button.config(bg=colours['blue'], fg='white',
                         width=round(button_width/2),
                         height=round(1.5), bd=3, relief="solid")
    error_mes.config(bg=colours["white"])


def w_game():
    """Wordle game function."""
    menu_frame.destroy()

    # Resizing window
    global width, height
    m.geometry("{}x{}".format(width, round(height*1.2)))

    global w_frame, chosen_game, w_desc, num, help_label

    # Help label
    help_label = Label(m, text="?", font=("Arial", 12))
    help_label.bind('<Button-1>', lambda e: w_tutorial())
    help_label.pack(fill=Y, side=TOP, pady=10, padx=10,
                    anchor=W)
    help_label.config(bg=colours["yellow"], fg="black",
                      width=4, height=2, bd=2, relief="solid")
    num = 0
    chosen_game = "Wordle"
    w_frame = Frame(m)
    w_frame.pack()

    w_label = Label(w_frame, text="Wordle", font=("Arial", 30, "bold"))
    w_desc = Label(w_frame, text="Guess the 5-letter word:",
                   font=("Arial", 16))

    # words list (45 5-letter words)
    words = ["blade", "crane", "flint", "grape", "house", "jumpy", "knock",
             "light", "mango", "night", "ocean", "plant", "queen", "river",
             "stone", "table", "under", "vivid", "whale", "zesty", "pinky",
             "cloud", "brave", "charm", "dwarf", "eagle", "frost", "glove",
             "honey", "grace", "jewel", "lunar", "magic", "noble", "orbit",
             "pearl", "quest", "royal", "sugar", "tiger", "urban", "races",
             "waltz", "crash", "drink"]
    # Function for what happens when you submit a word

    def w_submit():
        """Submit word function for Wordle."""
        global w_entry, error_mes, attempts, attempts_label, w_desc
        global answer_button, num
        sub_word = w_entry.get()
        for letter in sub_word.lower():
            if sub_word.count(letter) > 2:
                error_mes.destroy()
                error_mes = Label(w_frame, text="What are you doing?",
                                  font=("Arial", 12))
                error_mes.grid(row=3, column=0, columnspan=2)
                error_mes.config(bg=colours["white"], fg=colours["red"])
                w_frame.after(2000, lambda: error_mes.config(text=""))
                return
        if len(sub_word) != 5:
            error_mes.destroy()
            error_mes = Label(w_frame, text="Please enter a 5-letter word.",
                              font=("Arial", 12))
            error_mes.grid(row=3, column=0, columnspan=2)
            error_mes.config(bg=colours["white"], fg=colours["red"])
            w_frame.after(2000, lambda: error_mes.config(text=""))
        elif not sub_word.isalpha():
            error_mes.destroy()
            error_mes = Label(w_frame, text="Please enter only letters.",
                              font=("Arial", 12))
            error_mes.grid(row=3, column=0, columnspan=2)
            error_mes.config(bg=colours["white"], fg=colours["red"])
            w_frame.after(2000, lambda: error_mes.config(text=""))
        else:
            sub_word = sub_word.lower()
            if sub_word == chosen_word:
                attempts -= 1
                error_mes.destroy()
                w_desc.destroy()
                answer_button.destroy()
                w_entry.destroy()
                error_mes = Label(w_frame, text="Congratulations! "
                                  "You've guessed the word!",
                                  font=("Arial", 16, "bold"))
                error_mes.grid(row=3, column=0, columnspan=2)
                error_mes.config(bg=colours["white"], fg=colours["blue"])
                attempts_label.destroy()
                global w_score
                w_score = start_attempts - attempts
                if w_score == 6:
                    extra_text = "Phew!"
                else:
                    extra_text = "Great job!"
                score_label = Label(w_frame, text=extra_text,
                                    font=("Arial", 16, "bold"))
                score_label.grid(row=4, column=0, columnspan=3, pady=10)
                score_label.config(bg=colours["white"], fg=colours["blue"])
                # highscore
                global w_highscore, w_played
                if w_played is False:
                    w_highscore = w_score
                    high_score_label = Label(w_frame, text="New Highscore!",
                                             font=("Arial", 16, "bold"))
                    high_score_label.grid(row=5, column=0,
                                          columnspan=3, pady=(0, 10))
                    high_score_label.config(bg=colours["white"],
                                            fg=colours["dblue"])
                else:
                    if w_score < w_highscore:
                        w_highscore = w_score
                        high_score_label = Label(w_frame,
                                                 text="New Highscore!",
                                                 font=("Arial", 16, "bold"))
                        high_score_label.grid(row=5, column=0,
                                              columnspan=3, pady=(0, 10))
                        high_score_label.config(bg=colours["white"],
                                                fg=colours["dblue"])
                w_played = True

            elif attempts > 1:
                attempts -= 1
                attempts_label.destroy()
                attempts_label = Label(w_frame,
                                       text="Attempts: "
                                            "{}".format(attempts),
                                       font=("Arial", 12))
                attempts_label.grid(row=4, column=0, columnspan=3, pady=10)
                attempts_label.config(bg=colours["white"],
                                      fg=colours["dgrey"])
                w_entry.delete(0, END)
            else:
                error_mes.destroy()
                error_mes = Label(w_frame, text=f"Game Over! The word "
                                  "was '{chosen_word}'.",
                                  font=("Arial", 16, "bold"))
                error_mes.grid(row=3, column=0, columnspan=2, pady=10)
                error_mes.config(bg=colours["white"], fg=colours["red"])
                w_desc.destroy()
                w_entry.destroy()
                answer_button.destroy()
                attempts_label.destroy()

            # Displaying the guessed letters with colours
            display_col = []
            for index in range(5):
                letter = sub_word[index]
                correct_letter = chosen_word[index]
                if letter == correct_letter:
                    display_col.append(colours["blue"])
                elif letter in chosen_word:
                    if sub_word.count(letter) > chosen_word.count(letter):
                        # Handling duplicate submitted letters
                        for double in range(5):
                            d_letter = sub_word[double]
                            if d_letter == letter and double != index:
                                if d_letter == chosen_word[double]:
                                    display_col.append(colours["dgrey"])
                                else:
                                    if double < i:
                                        display_col.append(colours["dgrey"])
                                    else:
                                        display_col.append(colours["dyellow"])
                    else:
                        display_col.append(colours["dyellow"])
                else:
                    display_col.append(colours["dgrey"])
            # Displaying the guessed letters
            let_i = 0

            def show_delayed_letters(num, sub_word, display_col):
                """Show letters with delay for Wordle."""
                nonlocal let_i
                if let_i < 5:
                    letter_label = Label(word_frame,
                                         text=sub_word[let_i].upper(),
                                         font=("Arial", 20),
                                         width=4, height=2,
                                         bg=display_col[let_i], fg="white")
                    letter_label.grid(row=num, column=let_i, padx=2, pady=2)
                    letter_label.config(bd=3, relief="solid")
                    w_frame.after(100, lambda:
                                  show_delayed_letters(num, sub_word,
                                                       display_col))
                    let_i += 1
            show_delayed_letters(num, sub_word, display_col)
            num += 1

    chosen_word = random.choice(words)
    print(chosen_word)  # For testing purposes, to be removed later
    global w_entry, answer_button, error_mes, attempts, attempts_label
    start_attempts = 6  # Number of attempts
    attempts = 6
    w_entry = Entry(w_frame, font=("Arial", 16))
    answer_button = Label(w_frame, text="Submit", font=("Arial", 12))
    answer_button.bind('<Button-1>', lambda e: w_submit())
    error_mes = Label(w_frame, text="", font=("Arial", 12), fg="red")
    attempts_label = Label(w_frame, text="Attempts: {}".format(attempts),
                           font=("Arial", 12, "bold"))

    # Layout
    w_label.grid(row=0, column=0, columnspan=2, sticky=W+E, pady=20)
    w_desc.grid(row=1, column=0, columnspan=2, sticky=W+E)
    w_entry.grid(row=2, column=0, pady=10)
    answer_button.grid(row=2, column=1, pady=10, padx=10, sticky=W)
    error_mes.grid(row=3, column=0, columnspan=2)
    attempts_label.grid(row=4, column=0, columnspan=2, pady=10)


    def on_enter_key(event):
        """Move on when pressing enter"""
        w_submit()
    w_entry.bind('<Return>', on_enter_key)

    word_frame = Frame(w_frame)
    word_frame.grid(row=6, column=0, columnspan=2)
    for rows in range(6):
        for columns in range(5):
            letter_label = Label(word_frame, text="", font=("Arial", 20),
                                 width=4, height=2,
                                 bg=colours["grey"])
            letter_label.grid(row=rows, column=columns, padx=2, pady=2)

    # Colour Config
    w_frame.config(bg=colours["white"])
    w_label.config(bg=colours["white"], fg="black")
    w_desc.config(bg=colours["white"], fg=colours["dblue"])
    w_entry.config(bg=colours["yellow"], fg="black", bd=3, relief="solid",
                    highlightthickness=0, insertbackground="black")
    answer_button.config(bg=colours['blue'], fg='white',
                         width=round(button_width/2),
                         height=round(1.5), bd=3, relief="solid")
    error_mes.config(bg=colours["white"])
    attempts_label.config(bg=colours["white"], fg=colours["dgrey"])
    word_frame.config(bg=colours["white"])


    global menu_exit
    menu_exit.config(text="Exit to Menu")
    menu_exit.bind('<Button-1>', lambda event: exit_to_menu())


def hm_game():
    """Hangman game function."""
    menu_frame.destroy()
    global chosen_game, hm_frame, content_frame, hm_entry
    global hm_attempts, help_label

    # Help label
    help_label = Label(m, text="?", font=("Arial", 12))
    help_label.bind('<Button-1>', lambda e: hm_tutorial())
    help_label.pack(fill=Y, side=TOP, pady=10, padx=10,
                    anchor=W)
    help_label.config(bg=colours["yellow"], fg="black",
                      width=4, height=2, bd=2, relief="solid")

    chosen_game = "Hangman"
    hm_frame = Frame(m)
    hm_frame.pack(pady=(0, 10))
    content_frame = Frame(m)
    hm_attempts = 6

    # Words list 30 words
    words = ["python", "javascript", "hangman", "programming", "developer",
             "function", "variable", "Photo", "testing", "collections",
             "challenge", "interface", "stickman", "wizard", "puzzle",
             "mystery", "adventure", "treasure", "dragon", "castle",
             "forest", "mountain", "river", "ocean", "island",
             "extreme", "intergalactic", "fantasy", "galaxy",
             "supercalifragilistic"]
    chosen_word = random.choice(words)
    print(chosen_word)  # For testing purposes, to be removed later
    # Function for what happens when you submit a letter

    def hm_submit():
        """Submit letter function for Hangman."""
        global hm_entry, error_mes, hm_submit_button, hidden_word, img_level
        global stickman_label, used_letters_label, hm_score, wrong_letters
        global hm_played, hm_attempts, hm_desc, img
        sub_letter = hm_entry.get()
        sub_letter = sub_letter.upper()
        if len(sub_letter) != 1:
            error_mes.destroy()
            error_mes = Label(hm_frame, text="Please enter a single letter.",
                              font=error_font)
            error_mes.grid(row=3, column=0, columnspan=2, pady=(10, 0))
            error_mes.config(bg=colours["white"], fg=colours["red"])
            hm_entry.delete(0, END)
            hm_frame.after(2000, lambda: error_mes.config(text=""))
        elif not sub_letter.isalpha():
            error_mes.destroy()
            error_mes = Label(hm_frame, text="Please enter a letter (a-z).",
                              font=error_font)
            error_mes.grid(row=3, column=0, columnspan=2, pady=(10, 0))
            error_mes.config(bg=colours["white"], fg=colours["red"])
            hm_entry.delete(0, END)
            hm_frame.after(2000, lambda: error_mes.config(text=""))
        elif sub_letter in hidden_word or sub_letter in wrong_letters:
            error_mes.destroy()
            error_mes = Label(hm_frame, text="You've already "
                                             "guessed that letter.",
                              font=error_font)
            error_mes.grid(row=3, column=0, columnspan=2, pady=(10, 0))
            error_mes.config(bg=colours["white"], fg=colours["red"])
            hm_entry.delete(0, END)
            hm_frame.after(2000, lambda: error_mes.config(text=""))
        else:
            if sub_letter.lower() in chosen_word:
                for i in range(len(chosen_word)):
                    letter = chosen_word[i]
                    if letter == sub_letter.lower():
                        sub_letter = sub_letter.upper()
                        hidden_word[i] = sub_letter
                hm_entry.delete(0, END)
                hm_word_label.config(text=" ".join(hidden_word))

                if "_" not in hidden_word:
                    win_mes = Label(hm_frame, text="Congratulations! You've"
                                    " guessed the word!",
                                    font=("Arial", 16, "bold"))
                    win_mes.grid(row=3, column=0, columnspan=2)
                    win_mes.config(bg=colours["white"], fg=colours["blue"])
                    hm_entry.destroy()
                    hm_submit_button.destroy()
                    hm_desc.destroy()
                    # highscore
                    global hm_score, hm_highscore
                    if hm_played is False:
                        hm_score = len(wrong_letters.split())
                        hm_highscore = hm_score
                        high_score_label = Label(hm_frame,
                                                 text="New High Score!",
                                                 font=("Arial", 14, "bold"))
                        high_score_label.grid(row=4, column=0, columnspan=2)
                        high_score_label.config(bg=colours["white"],
                                                fg=colours["dblue"])
                    else:
                        if len(wrong_letters.split()) < hm_highscore:
                            hm_score = len(wrong_letters.split())
                            hm_highscore = hm_score
                            high_score_label = Label(hm_frame,
                                                     text="New High Score!",
                                                     font=("Arial", 14,
                                                           "bold"))
                            high_score_label.grid(row=4, column=0,
                                                  columnspan=2)
                            high_score_label.config(bg=colours["white"],
                                                    fg=colours["dblue"])
                    hm_played = True
                elif "_" in hidden_word:
                    error_mes.destroy()
                    error_mes = Label(hm_frame, text="Correct!",
                                      font=error_font)
                    error_mes.grid(row=3, column=0, columnspan=2,
                                   pady=(10, 0))
                    error_mes.config(bg=colours["white"], fg=colours["blue"])
                    hm_frame.after(1000, lambda: error_mes.config(text=""))
            else:
                sub_letter = sub_letter.upper()
                if len(wrong_letters) > 0:
                    wrong_letters += " "+sub_letter
                else:
                    wrong_letters += sub_letter
                used_letters_label.config(
                    text="Wrong letters:\n\n{}".format(wrong_letters))
                hm_entry.delete(0, END)
                hm_attempts -= 1
                img_level += 1
                img_path = "Stickman{}.png".format(img_level)
                img = PhotoImage(file=img_path)
                stickman_label.config(image=img)
                stickman_label.image = img
                if hm_attempts == 0:
                    lose_mes = Label(hm_frame,
                                     text="Game Over! The word "
                                          "was '{}'.".format(chosen_word),
                                     font=("Arial", 16, "bold"))
                    lose_mes.grid(row=3, column=0, columnspan=2)
                    lose_mes.config(bg=colours["white"], fg=colours["red"])
                    hm_entry.destroy()
                    hm_submit_button.destroy()
                    hm_desc.destroy()
                elif hm_attempts > 0:
                    error_mes.destroy()
                    error_mes = Label(hm_frame, text="Incorrect!",
                                      font=error_font)
                    error_mes.grid(row=3, column=0, columnspan=2,
                                   pady=(10, 0))
                    error_mes.config(bg=colours["white"], fg=colours["red"])
                    hm_frame.after(1000, lambda: error_mes.config(text=""))

    global hm_desc, hm_entry, hm_submit_button, error_mes
    hm_label = Label(hm_frame, text="Hangman", font=("Arial", 30, "bold"))
    hm_desc = Label(hm_frame, text="Enter a letter to guess the word:",
                    font=("Arial", 16))
    hm_entry = Entry(hm_frame, font=("Arial", 16), width=5)
    hm_submit_button = Label(hm_frame, text="Submit", font=("Arial", 12))
    hm_submit_button.bind('<Button-1>', lambda e: hm_submit())
    error_font = ("Arial", 14, "bold")
    error_mes = Label(hm_frame, text="", font=("Arial", 14, "bold"))

    global hidden_word, img_level, img, stickman_label
    global used_letters_label, wrong_letters

    # Content: Hidden word (left), Stickman (right)
    wrong_letters = ""
    hidden_word = ["_"] * len(chosen_word)
    hm_word_label = Label(content_frame, text=" ".join(hidden_word),
                          font=("Arial", 24, "bold"))
    used_letters_label = Label(content_frame,
                               text="Wrong "
                                    "letters:\n\n{}".format(wrong_letters),
                               font=("Arial", 12), justify=CENTER)

    img_level = 0  # Stickman image level
    img_path = "Stickman{}.png".format(img_level)  # Initial stickman image
    img = PhotoImage(file=img_path)
    stickman_label = Label(content_frame, image=img, width=200, height=350)
    stickman_label.image = img

    # Layout
    hm_label.grid(row=0, column=0, columnspan=2, sticky=W+E, pady=15)
    hm_desc.grid(row=1, column=0, columnspan=2, sticky=W+E, pady=(0, 10))
    hm_entry.grid(row=2, column=0, pady=5, sticky=E)
    hm_submit_button.grid(row=2, column=1, pady=5, sticky=W, padx=10)
    error_mes.grid(row=3, column=0, columnspan=2, pady=(10, 0))
    content_frame.pack()

    hm_word_label.grid(row=0, column=0, sticky=W+E, padx=50)
    stickman_label.grid(row=0, rowspan=2, column=1, sticky=E)
    used_letters_label.grid(row=1, column=0, sticky=W+E)

    # Colour Config
    hm_frame.config(bg=colours["white"])
    content_frame.config(bg=colours["white"])
    hm_label.config(bg=colours["white"], fg="black")
    hm_desc.config(bg=colours["white"], fg=colours["dblue"])
    hm_entry.config(bg=colours["yellow"], fg="black", bd=3, relief="solid",
                    highlightthickness=0, insertbackground="black")
    hm_submit_button.config(bg=colours['blue'], fg='white',
                            width=round(button_width/2),
                            height=2, bd=3, relief="solid")
    error_mes.config(bg=colours["white"])
    hm_word_label.config(bg=colours["white"], fg="black")
    used_letters_label.config(bg=colours["white"], fg="black")
    stickman_label.config(bg=colours["white"])

    global menu_exit
    menu_exit.config(text="Exit to Menu")
    menu_exit.bind('<Button-1>', lambda event: exit_to_menu())


    def on_enter_key(event):
        """Move on when pressing enter"""
        hm_submit()
    hm_entry.bind('<Return>', on_enter_key)


def exit_to_menu():
    """Delete current game frame and return to main menu."""
    global chosen_game, help_label
    if chosen_game == "Quiz":
        gk_frame.destroy()
        help_label.destroy()
    elif chosen_game == "Wordle":
        w_frame.destroy()
        help_label.destroy()
    elif chosen_game == "Hangman":
        hm_frame.destroy()
        help_label.destroy()
        content_frame.destroy()
    menu_exit.destroy()
    open_menu()
# Program Menu


def tutorial_menu():
    """Menu for game tutorials."""
    menu = Menu(m)
    m.config(menu=menu)
    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="How to Play", menu=help_menu)
    help_menu.add_command(label="How to play: {}".format(Game1),
                          command=gk_tutorial)
    help_menu.add_command(label="How to play: {}".format(Game2),
                          command=w_tutorial)
    help_menu.add_command(label="How to play: {}".format(Game3),
                          command=hm_tutorial)
# Open Menu function


def open_menu():
    """Open menu with all game options."""
    tutorial_menu()
    frame.destroy()
    global menu_frame, Game1, Game2, Game3, player_name, colours
    menu_frame = Frame(m)
    menu_frame.pack(pady=(50, 0))

    global width, height
    m.geometry("{}x{}".format(width, height))

    # Program Title
    if "Caio" in player_name.title():
        text = "Welcome, Creator!"
    elif "Chong" in player_name.title():
        text = "Welcome, miss!"
    elif "Ethan" in player_name.title():
        text = "Get out of my program, Ethan."
    else:
        text = "Welcome, {}!".format(player_name)
    welcome_label = Label(menu_frame, text=text, font=("Arial", 18))
    label = Label(menu_frame, text="Caio's Cool Collections",
                  font=("Arial", 35, "bold"))

    # Menu Buttons
    menu_button1 = Label(menu_frame, text=Game1, font=("Arial", 12, "bold"))
    menu_button1.bind('<Button-1>', lambda e: gk_game())
    menu_button2 = Label(menu_frame, text=Game2, font=("Arial", 12, "bold"))
    menu_button2.bind('<Button-1>', lambda e: w_game())
    menu_button3 = Label(menu_frame, text=Game3, font=("Arial", 12, "bold"))
    menu_button3.bind('<Button-1>', lambda e: hm_game())
    scores_button = Label(menu_frame, text="Highscores",
                          font=("Arial", 12, "bold"))
    scores_button.bind('<Button-1>', lambda e: scores())
    global menu_exit
    menu_exit = Label(m, text="Exit", font=("Arial", 12, "bold"))
    menu_exit.bind('<Button-1>', lambda e: m.quit())

    # program layout
    welcome_label.grid(row=0, column=0, columnspan=3, sticky=W+E)
    label.grid(row=1, column=0, columnspan=3, sticky=W+E, pady=20)
    menu_button1.grid(row=2, column=0, pady=30)
    menu_button2.grid(row=2, column=1, padx=40)
    menu_button3.grid(row=2, column=2)
    scores_button.grid(row=3, column=0, columnspan=3, pady=30, sticky=W+E)
    menu_exit.pack(fill=Y, side=BOTTOM, pady=20, padx=button_width*5)

    # Colour config
    menu_frame.config(bg=colours["white"])
    welcome_label.config(bg=colours["white"], fg=colours["blue"])
    label.config(bg=colours["white"], fg="black")
    menu_button1.config(bg=colours['yellow'], fg='black',
                        width=button_width, height=button_height, bd=3,
                        relief="solid")
    menu_button2.config(bg=colours['yellow'], fg='black',
                        width=button_width, height=button_height, bd=3,
                        relief="solid")
    menu_button3.config(bg=colours['yellow'], fg='black',
                        width=button_width, height=button_height, bd=3,
                        relief="solid")
    scores_button.config(bg=colours['blue'], fg='white',
                         width=round(button_width*1.5),
                         height=round(button_height/1.5), bd=3,
                         relief="solid")
    menu_exit.config(bg=colours['red'], fg='white',
                     width=round(button_width*1.5),
                     height=round(button_height/2), bd=3,
                     relief="solid")
# Menu function


def menu():
    """Open Beginning Menu before entering name."""
    global player_name, name_entry
    player_name = name_entry.get()
    player_name = player_name.title()

    if name_entry.get() == "":
        global error_mes
        error_mes.config(text="Please enter a name to continue.")
        frame.after(2000, lambda: error_mes.config(text=""))
    else:
        open_menu()


# Beginning message
title = Label(frame, text="Welcome to Caio's Cool Collections!",
              font=("Arial", 30, "bold"), justify=CENTER)
subtext = Label(frame, text="Before we begin, please enter your name below:",
                font=("Arial", 18), justify=CENTER)
title.pack(pady=20)
subtext.pack(pady=20)
global name_entry
name_entry = Entry(frame, font=("Arial", 16))
enter_label = Label(frame, text="Enter", font=("Arial", 12, "bold"))
enter_label.bind('<Button-1>', lambda e: menu())
error_mes = Label(frame, text="", font=("Arial", 12), fg=colours["red"])
error_mes.pack(pady=20)
name_entry.pack()
enter_label.pack(pady=20)

# colour config
title.config(bg=colours["white"], fg="black")
subtext.config(bg=colours["white"], fg=colours["blue"])
name_entry.config(bg=colours["yellow"], fg="black",
                  bd=3, insertbackground="black", relief="solid",
                  highlightthickness=0)
enter_label.config(bg=colours['blue'], fg='white',
                   width=8, height=2, bd=3, relief="solid")
error_mes.config(bg=colours["white"])


def on_enter_key(event):
    """Move on when pressing enter."""
    menu()


name_entry.bind('<Return>', on_enter_key)

m.mainloop()
