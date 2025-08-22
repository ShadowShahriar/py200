quiz = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7": "12",
    "What is the color of the sky?": "Green",
}

score = 0

for q, a in quiz.items():
    ans = input(f"{q} :\n> ").strip().lower()

    if ans == a.lower():
        print("✅ Correct")
        score += 1
    else:
        print(f"⛔ Wrong! The answer is {a}")
    print("")

print(f"Your final score: {score}/{len(quiz)}")
