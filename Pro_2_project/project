
import tkinter as tk
from tkinter import messagebox


class Quiz:

    def __init__(self):
        self.questions = {
            "What is the capital of Sweden?": "Stockholm",
            "What is the capital of Sudan?": "Khartoum",
            "What is the capital of Mongolia?": "Ulanbator",
            
        }

        self.question_list = list(self.questions.keys())
        self.index = 0
        self.score = 0

    def current_question(self):
        return self.question_list[self.index]

    def check_answer(self, answer):

        correct_answer = self.questions[self.current_question()]

        if answer.strip().lower() == correct_answer.lower():
            self.score += 1
            return True

        return False

    def next_question(self):

        self.index += 1

        if self.index >= len(self.question_list):
            return False

        return True


quiz = Quiz()


def save_score():

    try:
        with open("score.txt", "a") as file:
            file.write(f"Score: {quiz.score}\n")

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not save file: {e}"
        )


def submit_answer():

    try:

        answer = answer_entry.get()

        if quiz.check_answer(answer):
            messagebox.showinfo(
                "Correct",
                "Correct answer!"
            )

        else:
            messagebox.showinfo(
                "Wrong",
                "Wrong answer!"
            )

        answer_entry.delete(0, tk.END)

        if quiz.next_question():

            question_label.config(
                text=quiz.current_question()
            )

        else:

            save_score()

            messagebox.showinfo(
                "Finished",
                f"Your score is {quiz.score}"
            )

            window.destroy()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


window = tk.Tk()

window.title("Quiz Program - Yalaltbatt och Rahman (Pro_2_project)")
window.geometry("600x300")

question_label = tk.Label(
    window,
    text=quiz.current_question(),
    font=("Arial", 12)
)

question_label.pack(pady=10)

answer_entry = tk.Entry(
    window,
    width=30
)

answer_entry.pack(pady=10)

submit_button = tk.Button(
    window,
    text="Submit",
    command=submit_answer
)

submit_button.pack(pady=10)

window.mainloop()
