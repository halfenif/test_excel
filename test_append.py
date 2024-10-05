from openpyxl import Workbook

# Function to append data in chunks and save periodically
def append_data_in_chunks(file_name):
    # Create a new workbook and select the active sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "ChunkedData"

    # Add header
    ws.append(["ID", "Name", "Age"])

    # Process and append data in chunks
    idx = 0
    for batch_start in range(1, 1000001):
        idx += 1
        if idx % 10000 == 0:
            wb.save(file_name)
            print(f"Data saved in {format(idx,",d")}")
        
        ws.append([idx, f"Person_{idx}", 20 + (idx % 30)])
    # End of For
    wb.save(file_name)

        

    

# Save data in chunks
append_data_in_chunks("report_excel/test_append.xlsx")
