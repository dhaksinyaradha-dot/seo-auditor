import json
import pandas as pd

with open("data/results.json", "r", encoding="utf-8") as file:
    results = json.load(file)

df = pd.DataFrame(results)


print(df)
df.to_csv("data/report.csv", index=False)
print("Report saved to data/report.csv")