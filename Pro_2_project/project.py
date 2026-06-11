
# ==================================================
# IMPORTERA BIBLIOTEK
# ==================================================

# Tkinter används för att skapa ett grafiskt gränssnitt (GUI)
import tkinter as tk
from tkinter import messagebox


# ==================================================
# QUIZ-KLASS
# ==================================================

# Klassen Quiz hanterar frågor, svar och poäng
class Quiz:

    def __init__(self):

        # Dictionary som innehåller frågor och korrekta svar
        self.questions = {
            "What is the capital of Sweden?": "Stockholm",
            "What is the capital of Sudan?": "Khartoum",
            "What is the capital of Mongolia?": "Ulaanbaatar",
        }

        # Skapar en lista med alla frågor
        self.question_list = list(self.questions.keys())

        # Håller reda på vilken fråga som visas
        self.index = 0

        # Spelarens poäng
        self.score = 0

    # Returnerar den aktuella frågan
    def current_question(self):
        return self.question_list[self.index]

    # Kontrollerar om användarens svar är korrekt
    def check_answer(self, answer):

        correct_answer = self.questions[self.current_question()]

        if answer.strip().lower() == correct_answer.lower():
            self.score += 1
            return True

        return False

    # Går vidare till nästa fråga
    def next_question(self):

        self.index += 1

        if self.index >= len(self.question_list):
            return False

        return True


# Skapar ett Quiz-objekt
quiz = Quiz()


# ==================================================
# FILHANTERING
# ==================================================

# Sparar spelarens poäng i en textfil
def save_score():

    try:
        with open("score.txt", "a") as file:
            file.write(f"Score: {quiz.score}\n")

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not save file: {e}"
        )


# ==================================================
# SVARSHANTERING
# ==================================================

# Funktionen körs när användaren klickar på Submit
def submit_answer():

    try:

        # Hämtar text från inmatningsfältet
        answer = answer_entry.get()

        # Kontrollerar svaret
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

        # Tömmer inmatningsfältet
        answer_entry.delete(0, tk.END)

        # Visar nästa fråga
        if quiz.next_question():

            question_label.config(
                text=quiz.current_question()
            )

        else:

            # Sparar poängen när quizet är slut
            save_score()

            messagebox.showinfo(
                "Finished",
                f"Your score is {quiz.score}"
            )

            # Stänger programmet
            window.destroy()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# ==================================================
# SKAPA GUI-FÖNSTRET
# ==================================================

window = tk.Tk()

# Titel på fönstret
window.title(
    "Quiz Program - Yalaltbatt och Rahman (Pro_2_project)"
)

# Fönstrets storlek
window.geometry("600x300")


# ==================================================
# FRÅGETEXT
# ==================================================

question_label = tk.Label(
    window,
    text=quiz.current_question(),
    font=("Arial", 12)
)

question_label.pack(pady=10)


# ==================================================
# INMATNINGSFÄLT
# ==================================================

answer_entry = tk.Entry(
    window,
    width=30
)

answer_entry.pack(pady=10)


# ==================================================
# SUBMIT-KNAPP
# ==================================================

submit_button = tk.Button(
    window,
    text="Submit",
    command=submit_answer
)

submit_button.pack(pady=10)


# ==================================================
# STARTA PROGRAMMET
# ==================================================

window.mainloop()

