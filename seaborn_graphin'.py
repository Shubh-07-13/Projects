import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

print(df.head())

df = df.dropna()
print(df.info())

print(df.describe())

print(df['species'].unique())

print(df['island'].unique())

sns.histplot(data=df, x='body_mass_g', bins=10, color='steelblue')
plt.title('Distribution of Penguin Body Mass')
plt.xlabel('Body Mass (grams)')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill='True')
plt.title("Flipper Length Shape by Species")
plt.xlabel("Flipper Length (mm)")
plt.show()

sns.histplot(data=df, x='flipper_length_mm', kde=True, color='orange')
plt.title("Flipper Length")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Count")
plt.show()

sns.scatterplot(data=df, x='bill_length_mm', y='body_mass_g', hue='species')
plt.title('Bill Length vs Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel("Body Mass (grams)")
plt.show()

corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, cmap="coolwarm")
plt.title('Correlation Heatmap - Penguin Measurements')
plt.show()

