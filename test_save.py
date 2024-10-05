from openpyxl import Workbook

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Set the title of the active sheet
ws.title = "SampleSheet"

# Add data to the worksheet
data = [
    ["ID", "Name", "Age"],
    [1, "Alice", 30],
    [2, "Bob", 25],
    [3, "Charlie", 35]
]

# Write data to the worksheet
for row in data:
    ws.append(row)

# Save the workbook
wb.save("report_excel/test_save.xlsx")
