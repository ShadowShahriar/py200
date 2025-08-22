import matplotlib.pyplot as plt

sections = ["S1*", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]
students = [45, 30, 24, 39, 49, 41, 34, 32, 40]

plt.bar(sections, students, edgecolor="black", color="#5740DB")
plt.title("Students of Intake 53", fontweight="bold", color="#160861", fontsize="14")
plt.xlabel("Sections", color="#160861", fontsize="11")
plt.ylabel("No. of Students", color="#160861", fontsize="11")
plt.xticks(color="#100E1D")
plt.yticks(color="#100E1D", rotation=90)
plt.grid(axis="both", linestyle="--", color="#000000", alpha=0.2)
plt.show()
