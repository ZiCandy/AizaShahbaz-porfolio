import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Create dataset (simulated web analytics)
# -------------------------
np.random.seed(42)

df = pd.DataFrame({
    "user_id": range(1, 101),
    "sessions": np.random.randint(1, 20, 100),
    "bounce_rate": np.random.uniform(0.2, 0.9, 100),
    "conversion": np.random.randint(0, 2, 100),
    "traffic_source": np.random.choice(["Google", "Social", "Direct", "Email"], 100)
})

# -------------------------
# Cleaning
# -------------------------
df["bounce_rate"] = df["bounce_rate"].round(2)

# -------------------------
# Key Metrics
# -------------------------
avg_bounce = df["bounce_rate"].mean()
conversion_rate = df["conversion"].mean()

print("Average Bounce Rate:", avg_bounce)
print("Conversion Rate:", conversion_rate)

# -------------------------
# Traffic Source Analysis
# -------------------------
source_perf = df.groupby("traffic_source")["conversion"].mean()
print("\nConversion by Traffic Source:\n", source_perf)

# -------------------------
# Visualization
# -------------------------
source_perf.plot(kind="bar")
plt.title("Conversion Rate by Traffic Source")
plt.xlabel("Traffic Source")
plt.ylabel("Conversion Rate")
plt.show()
