import pandas as pd
from fpdf import FPDF
from PyPDF2 import PdfMerger
from datetime import datetime
import os

# Function to read order data from CSV
def load_order_data(csv_file):
    return pd.read_csv(csv_file)

# Function to create individual PDF invoices for each order
def create_invoice_pdf(order, output_dir):
    # Extract order details
    order_id = order['Order ID']
    customer_name = order['Customer Name']
    product_name = order['Product Name']
    quantity = order['Quantity']
    unit_price = order['Unit Price']
    total_amount = quantity * unit_price
    date_of_purchase = datetime.now().strftime("%Y-%m-%d")

    # Create a PDF file for the invoice
    pdf_filename = f"{output_dir}/{order_id}.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Write invoice details
    pdf.cell(200, 10, txt=f"Invoice Number: {order_id}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Date of Purchase: {date_of_purchase}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Product Name: {product_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Quantity: {quantity}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Unit Price: ${unit_price:.2f}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Total Amount: ${total_amount:.2f}", ln=True, align='L')

    # Save the PDF file
    pdf.output(pdf_filename)
    return pdf_filename

def merge_pdfs(pdf_files, output_pdf):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()

# Main function
def main():
    csv_file = "orders.csv"
    output_dir = "invoices"  # Directory to store the invoices
    output_pdf = f"{output_dir}/all_invoices.pdf"  # Merged PDF will also be in the invoices directory

    # Create the output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Load order data
    orders = load_order_data(csv_file)

    # Generate individual PDF invoices and collect their filenames
    pdf_files = []
    for index, order in orders.iterrows():
        pdf_filename = create_invoice_pdf(order, output_dir)
        pdf_files.append(pdf_filename)

    # Merge all the PDF invoices into a single PDF file
    merge_pdfs(pdf_files, output_pdf)

    print(f"All invoices have been generated and merged into {output_pdf}")

if __name__ == "__main__":
    main()

