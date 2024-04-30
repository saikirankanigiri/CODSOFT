import tkinter as tk
import random as rnd

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    global user_score, computer_score, rounds_left
    user_choice = user_input.get().lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        result_text.set("Invalid choice. Please choose rock, paper, or scissors.")
        return
    computer_choice = rnd.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    result_text.set(result)
    user_choice_text.set("You chose: " + user_choice)
    computer_choice_text.set("Computer chose: " + computer_choice)
    if 'win!' in result:
        user_score += 1
    elif 'wins' in result:
        computer_score += 1
    rounds_left -= 1
    user_score_text.set("Your score: " + str(user_score))
    computer_score_text.set("Computer's score: " + str(computer_score))
    if rounds_left == 0:
        play_button.config(state=tk.DISABLED)
        play_again_button.config(state=tk.NORMAL)
        user_input.config(state=tk.DISABLED)

def play_again():
    global user_score, computer_score, rounds_left
    user_score = 0
    computer_score = 0
    rounds_left = int(rounds_input.get())
    play_button.config(state=tk.NORMAL)
    play_again_button.config(state=tk.DISABLED)
    user_input.config(state=tk.NORMAL)
    result_text.set("")
    user_choice_text.set("")
    computer_choice_text.set("")
    user_score_text.set("")
    computer_score_text.set("")

root = tk.Tk()
root.title("Rock, Paper, Scissors")
user_score = 0
computer_score = 0
rounds_left = 0

rounds_label = tk.Label(root, text="Enter number of rounds:")
rounds_label.pack()
rounds_input = tk.Entry(root, width=50)
rounds_input.pack()

play_button = tk.Button(root, text="Start Playing", command=play_again)
play_button.pack()

user_input = tk.Entry(root, width=100)
user_input.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again, state=tk.DISABLED)
play_again_button.pack()

user_choice_text = tk.StringVar()
computer_choice_text = tk.StringVar()
result_text = tk.StringVar()
user_score_text = tk.StringVar()
computer_score_text = tk.StringVar()

user_choice_label = tk.Label(root, textvariable=user_choice_text)
user_choice_label.pack()

computer_choice_label = tk.Label(root, textvariable=computer_choice_text)
computer_choice_label.pack()

result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

user_score_label = tk.Label(root, textvariable=user_score_text)
user_score_label.pack()

computer_score_label = tk.Label(root, textvariable=computer_score_text)
computer_score_label.pack()

root.mainloop()
