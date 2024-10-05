import pandas as pd

# Sample data to create a DataFrame
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Export the DataFrame to an Excel file using openpyxl engine
df.to_excel("report_excel/test_pandas.xlsx", index=False, engine="openpyxl")


