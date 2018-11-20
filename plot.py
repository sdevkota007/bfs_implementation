import matplotlib.pyplot as plt
import json


with open('runtime.json') as f:
    data = json.load(f)

x = data["nodes"]
y = data["runtime"]

plt.plot(x, y)
plt.xlabel('Time Step')
plt.ylabel('Number of nodes')
plt.title('Dynamic Graph')
plt.legend()
plt.show()