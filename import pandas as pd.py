import pandas as pd
import matplotlib.pyplot as plt

# 测试 pandas
data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(data)

# 测试 matplotlib
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Plot")
plt.show()