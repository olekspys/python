import pandas as pd

# Assuming the Excel file is named 'table.xlsx' and the sheet is 'Sheet1'
file_path = 'Book1.xlsx'

# Load Excel file
df = pd.read_excel(file_path, header=None)

# Reshape data into a single column
column_data = df.values.flatten()

# Create a new DataFrame
df_transformed = pd.DataFrame(column_data, columns=["Values"])

# Save the transformed data back to Excel
df_transformed.to_excel("transformed_table.xlsx", index=False)

print("Data has been transformed and saved to 'transformed_table.xlsx'.")