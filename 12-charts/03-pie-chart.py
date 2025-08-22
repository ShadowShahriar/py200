import matplotlib.pyplot as plt

labels = ["Coding", "Job", "Studying", "Art", "Electronics"]
sizes = [25, 45, 12, 8, 10]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    colors=["#1F5AFF", "#FF1F44", "#1FFF7C", "#FADB51", "#B916DA"],
)
plt.title("Time Management")
plt.show()
