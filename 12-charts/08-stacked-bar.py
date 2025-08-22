import matplotlib.pyplot as plt

labels = ("Python", "Java")
index = (1, 2)
usage_web = (20, 10)
usage_ds = (15, 15)
usage_game = (10, 5)

plt.bar(index, usage_web, tick_label=labels, label="Web", color="#5F33FF")
plt.bar(
    index,
    usage_ds,
    tick_label=labels,
    label="Data Science",
    bottom=usage_web,
    color="#FF3355",
)

usages_web_and_game = [usage_web[i] + usage_ds[i] for i in range(0, len(usage_web))]
plt.bar(
    index,
    usage_game,
    tick_label=labels,
    label="Games",
    bottom=usages_web_and_game,
    color="#33FF70",
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Programming Languages")
plt.legend()
plt.show()
