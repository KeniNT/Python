import os
import pandas as pd

# Function to read all CSV files in the given directory and its subdirectories
def read_sales_data(directory):
    sales_data = pd.DataFrame()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv") and 'product_names' not in file:
                file_path = os.path.join(root, file)
                data = pd.read_csv(file_path, encoding='ISO-8859-1')
                sales_data = pd.concat([sales_data, data], ignore_index=True)
    return sales_data

# Function to calculate total and average sales per product
def calculate_sales_summary(sales_data, product_names):
    # Calculate total sales (quantity sold) for each product
    total_sales = sales_data.groupby('Product ID')['Quantity_sold'].sum().reset_index()
    
    # Merge with product names
    sales_summary = pd.merge(total_sales, product_names, on='Product ID', how='left')
    
    # Calculate average sales per month (based on unique months in the sales data)
    sales_data['Year-Month'] = pd.to_datetime(sales_data['Date'], format='%d-%m-%Y').dt.to_period('M')
    months_count = sales_data['Year-Month'].nunique()
    sales_summary['Average Quantity Sold per Month'] = sales_summary['Quantity_sold'] / months_count
    
    # Sort by total sales and get the top 5 best-selling products
    top_5_products = sales_summary.nlargest(5, 'Quantity_sold')
    
    return sales_summary, top_5_products

# Directory path containing sales data
directory_path = 'C:\\sem5\\Adv_Python_Lab\\'

# Read product names
product_names = pd.read_csv('C:\\sem5\\Adv_Python_Lab\\product_names.csv')

# Read sales data
sales_data = read_sales_data(directory_path)

# Calculate sales summary and top 5 products
sales_summary, top_5_products = calculate_sales_summary(sales_data, product_names)

# Write sales summary to a new CSV file
sales_summary.to_csv('sales_summary.csv', index=False)

# Display the top 5 best-selling products
print(top_5_products)

