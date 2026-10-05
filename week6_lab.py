# week6_lab.py
# Author: Zenobia Thomas

records = [
    {
        "id": 1,
        "name": "Taylor",
        "category": "Travel",
        "amount": 1200,
        "status": "pending",
    },
    {
        "id": 2,
        "name": "Jordan",
        "category": "Equipment",
        "amount": 450,
        "status": "pending",
    },
    {
        "id": 3,
        "name": "Morgan",
        "category": "Software",
        "amount": 3500,
        "status": "Approved",
    },
    {"id": 4, "name": "Riley", "category": "Travel", "amount": 89, "status": "pending"},
    {
        "id": 5,
        "name": "Alex",
        "category": "Equipment",
        "amount": 2200,
        "status": "pending",
    },
]

for rec in records:
    if rec["status"] == "pending":
        print(f"{rec['name']}: ${rec['amount']:,.2f}")

LIMIT = 1000
HIGH = 2000
total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "pending":
        total += rec["amount"]
    if rec["amount"] > LIMIT:
        flagged.append(rec)
    if rec["amount"] > HIGH:
        high_value.append(rec)

import os

os.makedirs("data", exist_ok=True)

lines = [
    f"pending total:  ${total:,.2f}",
    f"Needs review:   {len(flagged)}",
    f"High-value:   {len(high_value)}",
]
for line in lines:
    print(line)

with open("data/week6_summary.txt", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\nRecords needing review:")
for r in flagged:
    print(f"  ID {r['id']}: {r['name']} - ${r['amount']:,.2f}")
