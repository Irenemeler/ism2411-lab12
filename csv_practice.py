# ISM2411 Lab 12
# Name: Irene Meler
#
# Reflection 1:
# Python can automate the process of reading, changing, and writing large
# amounts of CSV data, which would take longer to do manually in Excel.
# Excel is useful for quickly viewing data, creating charts, and making
# changes visually without writing code.
#
# Reflection 2:
# A business could use an append-mode log file to record each time its
# sales report is generated. Append mode is useful because it keeps
# previous records instead of replacing them with new ones.

import csv
from datetime import datetime

filename = "data/sales.csv"

# Exercise 1: Open the CSV file
with open(filename, "r") as file:
    print("Sales CSV file opened successfully!")


# Exercise 2: Read and print all rows
print("\nExercise 2: All CSV Rows")

with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3: Separate the header from the data
print("\nExercise 3: Header and Data")

with open(filename, "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4: Calculate total revenue
print("\nExercise 4: Revenue Calculations")

total_revenue = 0

with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")


# Exercise 5: Write cleaned data to a new CSV file
print("\nExercise 5: Cleaned CSV File")

orders_written = 0

with open(filename, "r") as input_file:
    reader = csv.reader(input_file)
    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)

        for row in reader:
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow(row)
                orders_written += 1

print("Original orders: 12")
print(f"Orders written: {orders_written}")
print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 6: Read the CSV using DictReader
print("\nExercise 6: Using DictReader")

dict_total_revenue = 0

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

print(f"Total revenue: ${dict_total_revenue:.2f}")

# csv.reader uses column positions, which is simple for smaller files.
# csv.DictReader uses column names, making code easier to understand and maintain.


# Exercise 7: Calculate revenue by product
print("\nExercise 7: Sales Summary by Product")

sales_summary = {}

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity

        if product in sales_summary:
            sales_summary[product] += revenue
        else:
            sales_summary[product] = revenue

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# Exercise 8: Append a record to the run log
print("\nExercise 8: Run Log")

with open("data/run_log.txt", "a") as log_file:
    timestamp = datetime.now()
    log_file.write(
        f"{timestamp} - Total revenue: ${total_revenue:.2f}\n"
    )

print("Run successfully logged!")