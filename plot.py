import matplotlib.pyplot as plt
import json


with open('runtime.json') as f:
    data = json.load(f)

x = data["nodes"]
y = data["runtime"]

print "\n\nPlotting Performance Validation graph for large n"
plt.plot(x, y)
plt.xlabel('Number of nodes')
plt.ylabel('Time(in seconds)')
plt.title('Runtime')
plt.legend()
plt.show()