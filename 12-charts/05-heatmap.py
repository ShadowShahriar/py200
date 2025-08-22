import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.rand(10, 10)
sns.heatmap(data, annot=True)
plt.title("Heatmap")
plt.show()
