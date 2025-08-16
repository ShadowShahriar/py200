from tkinter.messagebox import askretrycancel

answer = askretrycancel(
    title="Skill Issue",
    message="You are not there yet. You wanna retry?",
)

print(answer)
