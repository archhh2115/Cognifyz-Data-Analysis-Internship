import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/restaurants.csv", encoding='latin-1')
print("Level 3 Dataset Loaded Successfully")
print("\n===== TASK 3 : PRICE RANGE VS SERVICES =====")
delivery_table = pd.crosstab(df['Price range'], df['Has Online delivery'])
print("\nPrice Range vs Online Delivery")
print(delivery_table)
table_booking_table = pd.crosstab(df['Price range'], df['Has Table booking'])
print("\nPrice Range vs Table Booking")
print(table_booking_table)
plt.figure(figsize=(8,5))
sns.countplot(x='Price range', hue='Has Online delivery', data=df)
plt.title("Price Range vs Online Delivery")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.savefig("outputs/graphs/price_range_delivery.png")
print("\nLevel 3 Analysis Completed Successfully")
plt.show()

