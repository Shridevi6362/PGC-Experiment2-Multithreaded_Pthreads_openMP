import matplotlib.pyplot as plt

threads = [1, 2, 3, 4, 6, 16]

speedup = [0.485, 0.878, 1.146, 1.695, 2.279, 3.726]

efficiency = [48.49, 43.90, 38.21, 42.38, 37.99, 23.29]

# Speedup Graph
plt.figure(figsize=(8, 5))
plt.plot(threads, speedup, marker='o')
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("OpenMP Speedup vs Number of Threads")
plt.grid(True)
plt.savefig("speedup_graph.png", dpi=300, bbox_inches="tight")
plt.show()

# Efficiency Graph
plt.figure(figsize=(8, 5))
plt.plot(threads, efficiency, marker='o')
plt.xlabel("Number of Threads")
plt.ylabel("Efficiency (%)")
plt.title("OpenMP Efficiency vs Number of Threads")
plt.grid(True)
plt.savefig("efficiency_graph.png", dpi=300, bbox_inches="tight")
plt.show()
