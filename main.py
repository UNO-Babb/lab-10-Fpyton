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

# Build Data import slavery

# using Pandas
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



# Clean Data
years = ('1856', '1857', '1858', '1859', '1860', '1861')

adult = np.array([770, 3209, 2859, 3940, 2801, 995])
child = np.array([128, 488, 503, 552, 415, 161])

width = 0.6  # bar width

fig, ax = plt.subplots(figsize=(10, 6))

bottom = np.zeros(len(years))

# Plot Adult first (red)
p1 = ax.bar(years, adult, width, label='Adult Slaves', color='red', bottom=bottom)
bottom += adult

# Plot Child on top (green)
p2 = ax.bar(years, child, width, label='Child Slaves', color='green', bottom=bottom)

# Labels inside bars
ax.bar_label(p1, label_type='center', color='white', fontsize=10)
ax.bar_label(p2, label_type='center', color='white', fontsize=10)

# Titles and labels
ax.set_title('Number of Adult and Child Slaves Sold by Year', fontsize=14)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Slaves')
ax.legend()

# Y-axis limit
ax.set_ylim(0, 4600)

plt.tight_layout()
plt.savefig("adult_child_stacked_final.png", dpi=300, bbox_inches="tight")
plt.show()

names = []

for item in records:
    slave = item["Slave"]
    name = slave["Name"]

    if name is not None:
        names.append(name)
#print(names)
#print(transaction_record)