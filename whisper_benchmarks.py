import pandas as pd
import matplotlib.pyplot as plt

# Apply dark theme
plt.style.use("dark_background")

# Benchmark data for different models
data = {
    "Model": ["tiny", "base", "small", "medium", "large", "turbo"],
    "Loading Duration (s)":       [0.66, 1.72, 5.62, 19.91, 39.36, 15.69],
    "Transcription Duration (s)": [5.86, 14.37, 30.28, 103.99, 115.54, 64.29],
    "Disk Size (GB)":             [0.07, 0.14, 0.46, 1.5, 2.9, 1.6],
    "Number of Mistakes":         [93, 41, 28, 10, 7, 6],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Whisper Model Benchmarks", color="white")

# Plot Loading Duration
df.plot(kind="bar", x="Model", y="Loading Duration (s)", ax=axes[0, 0], color="skyblue", legend=False)
axes[0, 0].set_title("Loading Duration (s)", color="white")
axes[0, 0].set_ylabel("Seconds", color="white")
axes[0, 0].tick_params(axis="x", colors="white")
axes[0, 0].tick_params(axis="y", colors="white")

# Plot Transcription Duration
df.plot(kind="bar", x="Model", y="Transcription Duration (s)", ax=axes[0, 1], color="lightgreen", legend=False)
axes[0, 1].set_title("Transcription Duration (s)", color="white")
axes[0, 1].set_ylabel("Seconds", color="white")
axes[0, 1].tick_params(axis="x", colors="white")
axes[0, 1].tick_params(axis="y", colors="white")

# Plot Disk Size
df.plot(kind="bar", x="Model", y="Disk Size (GB)", ax=axes[1, 0], color="salmon", legend=False)
axes[1, 0].set_title("Disk Size (GB)", color="white")
axes[1, 0].set_ylabel("Gigabytes", color="white")
axes[1, 0].tick_params(axis="x", colors="white")
axes[1, 0].tick_params(axis="y", colors="white")

# Plot Number of Mistakes
df.plot(kind="bar", x="Model", y="Number of Mistakes", ax=axes[1, 1], color="gold", legend=False)
axes[1, 1].set_title("Number of Mistakes", color="white")
axes[1, 1].set_ylabel("Mistakes", color="white")
axes[1, 1].tick_params(axis="x", colors="white")
axes[1, 1].tick_params(axis="y", colors="white")

# Adjust layout
plt.tight_layout()

# Save the figure with transparent background
fig.savefig("whisper_benchmarks_dark.png", dpi=300, transparent=True, bbox_inches="tight")

# Show the plots (if in an interactive environment)
# plt.show()

# Apply dark theme and configure plot
plt.style.use("dark_background")
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Transcription Duration (left axis)
ax1.bar(df["Model"], df["Transcription Duration (s)"], color='skyblue', alpha=0.7, label='Duration')
ax1.set_ylabel('Transcription Duration (seconds)', color='white')
ax1.tick_params(axis='y', colors='white')

# Create second y-axis for Mistakes
ax2 = ax1.twinx()
ax2.plot(df["Model"], df["Number of Mistakes"], color='gold', marker='o', linewidth=2, label='Mistakes')
ax2.set_ylabel('Number of Mistakes', color='white')
ax2.tick_params(axis='y', colors='white')

# Add title and legend
plt.title("Transcription Performance vs Accuracy", color='white', pad=20)
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9), frameon=False)

# Set axis colors
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')

# Add value labels for mistakes
for x,y in zip(df["Model"], df["Number of Mistakes"]):
    ax2.text(x, y+0.5, str(y), ha='center', color='gold')

plt.tight_layout()
plt.savefig("transcription_performance.png", dpi=300, transparent=True)
# Show the plots (if in an interactive environment)
# plt.show()
