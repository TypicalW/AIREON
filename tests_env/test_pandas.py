import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

# Simulate node energy dropping
energy = 100
energy_log = []

for t in tqdm(range(50)):
    energy -= np.random.rand() * 2
    energy_log.append(energy)

df = pd.DataFrame({"time": range(50), "energy": energy_log})
print(df.head())

plt.plot(df["time"], df["energy"])
plt.title("AIREON Environment Test")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.show()
