import tkinter as tk
import random
from tkinter import messagebox

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        
        # Generate random number between 1 and 100
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        # Configure background color to lilac
        self.root.configure(bg="#e6e6fa")  # lilac color
        
        # Guess entry and submit button
        self.label_instruction = tk.Label(root, text="Guess the number (between 1 and 100):", bg="#e6e6fa", font=("Arial", 14))
        self.label_instruction.pack(pady=10)
        
        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, bg="#800080", fg="white", font=("Arial", 12, "bold"))
        self.submit_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(root, text="", bg="#e6e6fa", font=("Arial", 14))
        self.result_label.pack(pady=10)
    
    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1
            
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid Guess", "Please enter a number between 1 and 100.")
                self.entry_guess.delete(0, tk.END)
                return
            
            if guess < self.secret_number:
                self.result_label.config(text=f"Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text=f"Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                self.submit_button.config(state=tk.DISABLED)
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            self.entry_guess.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
