import pdfplumber
import pandas as pd
import re
import streamlit as st

# All categories CIBC uses 
CATEGORIES = [
    "Retail and Grocery",
    "Transportation",
    "Restaurants",
    "Health and Education",
    "Hotal, Entertainment and Recreation", 
    "Personal and Household Services",
    "Professional amd Financial Services",
    "Foreign Currency Transactions",
]

def extract_transactions(pdf_path):
    full_text ="" #the entire PDF text

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
            
    return parse_transactions(full_text)

def parse_transactions(text):
    transactions = []

    #Match lines like: Jan 21 Jan22 MERCHANT NAME CATERGORY 123.45
    #Build a regex that captures the category dynamically
    categories_pattern = "|".join(re.escape(c) for c in CATEGORIES)

    # describing the shape of the text for the transactions 
    pattern = re.compile(
        r"([A-Z][a-z]{2} \d{1,2})\s+"  #Transaction date
        r"([A-Z][a-z]{2} \d{1,2})\s+"  #Post date
        r"(.+?)\s+"                     #Descrition
        r"(" + categories_pattern + r")\s" #Category
        r"([\d,]+\.\d{2})"              # Amount
    )

    # scans the entire text and loops the matches as "match"
    for match in pattern.finditer(text):
        trans_date, post_date, description, category, amount = match.groups()
        transactions.append({
            "Trans Date": trans_date,
            "Post Date": post_date,
            "Description": description.strip(),
            "Category": category, 
            "Amount": float(amount.replace(",", ""))
        })
    return transactions

def save_csv(transactions, output_path):
    df = pd.DataFrame(transactions)
    #make a new column for the months of the transaction date and extract the month from the "Trans Date"
    df["Month"] = df["Trans Date"].str.split().str[0]
    df = df[["Month", "Trans Date", "Post Date","Amount", "Description", "Category"]]
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} transactions to {output_path}")
    return df

def print_summary(df):
    print("\n===== STATEMENT SUMMARY =====")
    print(f"Total Spent:       ${df['Amount'].sum():,.2f}")
    print(f"Total Transactions: {len(df)}")
    print(f"\nSpending by Category:")
    by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    for cat, total in by_category.items():
        print(f"  {cat:<45} ${total:>8,.2f}")
    print(f"\nTop 5 Purchases:")
    top5 = df.nlargest(5, "Amount")[["Trans Date", "Description", "Amount"]]
    print(top5.to_string(index=False))


if __name__ == "__main__":
    transactions = extract_transactions("input/statement.pdf")
    df = save_csv(transactions, "output/transactions.csv")
    print_summary(df)
    