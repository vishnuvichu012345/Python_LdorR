import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('users.csv')

# Drop rows with missing values
cleaned_df = df.dropna()

# Output the cleaned data to a new CSV file
cleaned_df.to_csv('cleaned_users.csv', index=False)

def get_top_users_over_age(df, age_threshold=30):
    return df[df['age'] > age_threshold].head(5)

print("Cleaned data saved to 'cleaned_users.csv'.")

top_users = get_top_users_over_age(cleaned_df)
print("Top users over age 30:\n", top_users)


plt.figure(figsize=(10, 5))
plt.hist(cleaned_df['age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of User Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()



mean_age = np.mean(cleaned_df['age'])
median_age = np.median(cleaned_df['age'])
std_dev_age = np.std(cleaned_df['age'])

print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Standard Deviation of Age: {std_dev_age}")