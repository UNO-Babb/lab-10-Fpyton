#MapPlot.py
#Name:
#Date:
#Assignment:

import slavery
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
transaction_record = slavery.get_transaction_record()
data = slavery.get_transaction_record()
first = transaction_record[0]
df = pd.DataFrame(data)



records = slavery.get_transaction_record()

dates = []
totals = []
years = []

for item in records:
    trans = item["Transaction"]

    date  = trans["Date"]
    total = trans["Number of Total Slaves Purchased"]

    # Basic validation
    if date is None or total is None:
        continue
    if total <= 0:
        continue

    # FIX: skip bad dates (like ".")
    if "/" not in date:
        continue

    # Split "month/day/year"
    parts = date.split("/")
    year_string = parts[-1]

    # Skip if year is not numbers
    if not year_string.isdigit():
        continue

    year = int(year_string)

    dates.append(date)
    totals.append(total)
    years.append(year)

# Build DataFrame using Pandas
df = pd.DataFrame({
    "Date": dates,
    "Year": years,
    "Total": totals
})

# Group by year
year_totals = df.groupby("Year")["Total"].sum()

# Plot
plt.figure(figsize=(6, 4))
year_totals.plot(kind="bar")

plt.xlabel("Year")
plt.ylabel("Total Slaves Purchased")
plt.title("Total Slaves Purchased Per Year (Cleaned Data)")

plt.tight_layout()
plt.savefig("slaves_per_year.png", dpi=300, bbox_inches="tight")
plt.show()

years = []
adult_counts = []
child_counts = []

for item in records:
    trans = item["Transaction"]

    date = trans["Date"]
    adult = trans["Number of Adult Slaves"]
    child = trans["Number of Child Slaves"]

    # BASIC cleaning -----------------------------
    if date is None or adult is None or child is None:
        continue

    if "/" not in date:      # skip bad dates like "."
        continue

    # extract the YEAR from "10/6/1856"
    parts = date.split("/")
    year_str = parts[-1]

    if not year_str.isdigit():   # skip invalid years
        continue

    year = int(year_str)

    if adult < 0 or child < 0:
        continue

    years.append(year)
    adult_counts.append(adult)
    child_counts.append(child)
adult_by_year = {}
child_by_year = {}

for i in range(len(years)):
    y = years[i]
    a = adult_counts[i]
    c = child_counts[i]

    if y not in adult_by_year:
        adult_by_year[y] = 0
        child_by_year[y] = 0

    adult_by_year[y] += a
    child_by_year[y] += c
# Convert dictionary to lists for plotting
years_sorted = sorted(adult_by_year.keys())
adult_list = [adult_by_year[y] for y in years_sorted]
child_list = [child_by_year[y] for y in years_sorted]
x = range(len(years_sorted))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 5))

bottom = np.zeros(len(x))

# Adults (red)
p1 = ax.bar(x, adult_list, width, label="Adult Slaves", color="red", bottom=bottom)
bottom += np.array(adult_list)

# Children (green)
p2 = ax.bar(x, child_list, width, label="Child Slaves", color="green", bottom=bottom)

# Labels inside bars
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')

# X-axis labels = Years
ax.set_xticks(x)
ax.set_xticklabels(years_sorted, rotation=45)

ax.set_title("Adult and Child Slaves Sold by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Slaves")
ax.legend()

ax.set_ylim(0, 5000)   # if you want max = 500

plt.tight_layout()
plt.savefig("adult_child_stacked_basic.png", dpi=300, bbox_inches="tight")
plt.show()







#print(transaction_record)