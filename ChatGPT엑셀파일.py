import random
from openpyxl import Workbook

# Initialize workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Product Sales Data"

# Column headers
ws.append(["Product ID", "Product Name", "Quantity", "Price"])

# Product data lists
product_names = ["Laptop", "Smartphone", "Tablet", "Headphones", "Camera", "Smartwatch", "Speaker", "Monitor", "Keyboard", "Mouse"]

# Generate 100 rows of product data
for i in range(1, 101):
    product_id = f"P{i:03d}"  # Product ID in the format P001, P002, etc.
    product_name = random.choice(product_names)  # Randomly choose a product name
    quantity = random.randint(1, 20)  # Random quantity between 1 and 20
    price = round(random.uniform(50, 1500), 2)  # Random price between 50 and 1500
    ws.append([product_id, product_name, quantity, price])

# Save the workbook to a file
file_path = "c:\\work\products.xlsx"
wb.save(file_path)

file_path
