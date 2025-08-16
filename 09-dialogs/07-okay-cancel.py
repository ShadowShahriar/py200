from tkinter.messagebox import askokcancel

answer = askokcancel(
    title="Confirmation",
    message="This will format your SSD. Don't mess it up!",
    detail="Space Free: 33.53 GB",
    icon="warning",
)

print(answer)
