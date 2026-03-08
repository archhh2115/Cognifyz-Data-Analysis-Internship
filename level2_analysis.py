import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df = pd.read_csv("data/restaurants.csv", encoding='latin-1')
print("Dataset Loaded Successfully\n")
print("------ TASK 1 : RESTAURANT RATINGS ------")
plt.figure(figsize=(8,5))
sns.histplot(df['Aggregate rating'], bins=10)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.savefig("outputs/graphs/rating_distribution.png")
plt.show()
rating_range = df['Aggregate rating'].round().value_counts().sort_values(ascending=False)
print("\nMost Common Rating Range:")
print(rating_range.head())
avg_votes = df['Votes'].mean()
print("\nAverage Votes per Restaurant:", avg_votes)
print("\n------ TASK 2 : CUISINE COMBINATIONS ------")
cuisine_data = df['Cuisines'].dropna()
cuisine_split = cuisine_data.str.split(', ')
cuisine_exploded = cuisine_split.explode()
top_cuisines = cuisine_exploded.value_counts().head(10)
print("\nTop Individual Cuisines:")
print(top_cuisines)
combo_counts = df['Cuisines'].value_counts().head(10)
print("\nMost Common Cuisine Combinations:")
print(combo_counts)
combo_ratings = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print("\nCuisine Combinations with Highest Ratings:")
print(combo_ratings.head(10))
plt.figure(figsize=(10,5))
combo_counts.head(5).plot(kind='bar')
plt.title("Top Cuisine Combinations")
plt.xlabel("Cuisine Combination")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/graphs/cuisine_combinations.png")
plt.show()
print("\n------ TASK 3 : GEOGRAPHIC ANALYSIS ------")
map_data = df[['Restaurant Name','Latitude','Longitude']].dropna()
fig = px.scatter_mapbox(
    map_data,
    lat="Latitude",
    lon="Longitude",
    hover_name="Restaurant Name",
    zoom=2,
    height=600
)
fig.update_layout(mapbox_style="open-street-map")
fig.show()
print("Restaurant location map generated.")
print("\n------ TASK 4 : RESTAURANT CHAINS ------")
restaurant_counts = df['Restaurant Name'].value_counts()
chains = restaurant_counts[restaurant_counts > 1]
print("\nRestaurant Chains (Multiple Branches):")
print(chains.head(20))
chain_ratings = df.groupby('Restaurant Name')['Aggregate rating'].mean()
print("\nTop Rated Restaurant Chains:")
print(chain_ratings.sort_values(ascending=False).head(10))
