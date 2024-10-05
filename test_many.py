from openpyxl import Workbook

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Set the title of the worksheet
ws.title = "LargeDataset"

# Create a large dataset to append (for example: 10000 rows of data)
data = [
    ["ID", "Name", "Age"]
]

# Generate sample data for many rows
for i in range(1, 10001):
    row = [i, f"Person_{i}", 20 + (i % 30)]
    data.append(row)

# Append the data row by row
for row in data:
    ws.append(row)

# Save the workbook
wb.save("large_data_workbook.xlsx")

print("Workbook with large dataset saved as large_data_workbook.xlsx")
