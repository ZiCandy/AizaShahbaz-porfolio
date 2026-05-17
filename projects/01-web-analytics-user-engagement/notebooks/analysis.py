import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET
df = pd.read_csv(r"C:\Users\aizas\Downloads\archive\bank.csv")

print(df.head())
# -----------------------------
# BASIC LOOK
# -----------------------------
print("First 5 rows:")
print(df.head())

print("\nInfo:")
print(df.info())

# -----------------------------
# CLEANING
# -----------------------------
df = df.dropna()

# -----------------------------
# KEY KPI ANALYSIS
# -----------------------------

# conversion rate (deposit yes/no)
conversion_rate = df["deposit"].value_counts(normalize=True) * 100
print("\nConversion Rate (%):")
print(conversion_rate)

# job analysis
job_counts = df["job"].value_counts()
print("\nTop Jobs:")
print(job_counts.head(10))

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.figure(figsize=(10,5))

plt.xticks(rotation=45)

job_counts.head(10).plot(kind="bar")

plt.title("Top Customer Jobs")
plt.xlabel("Job Type")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("job_chart.png")
plt.show()
