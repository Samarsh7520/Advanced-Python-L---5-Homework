import random
import tkinter as tk
from tkinter import messagebox

def determine_winner(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result_text = f"You chose {player_choice}, computer chose {computer_choice}. "

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=result_text + result)

root = tk.Tk()
root.geometry("400x300")
root.title("Rock Paper Scissors Game")
root.config(bg="#f0f0f0")

result_label = tk.Label(
    root,
    text="Make your move to start the game!",
    font=("Arial", 12),
    bg="#f0f0f0"
)
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_button = tk.Button(
    button_frame, text="Rock", width=10,
    command=lambda: determine_winner("Rock")
)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(
    button_frame, text="Paper", width=10,
    command=lambda: determine_winner("Paper")
)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(
    button_frame, text="Scissors", width=10,
    command=lambda: determine_winner("Scissors")
)
scissors_button.grid(row=0, column=2, padx=10)

if __name__ == "__main__":
    root.mainloop()