import pandas as pd
data = pd.read_csv(r"C:\Users\lesli\github-classroom\CodeYou-Data-Jan2024\wine-reviews-exercise-lesliehughes0921\winemag-data-130k-v2.csv")
data = data.groupby('country').agg({'title': 'count', 'points': 'mean'}).reset_index()
data["points"] = data["points"].round(1)
data.columns = ["country", "count", "points"]
data.to_csv("reviews-per-country.csv", index=None)