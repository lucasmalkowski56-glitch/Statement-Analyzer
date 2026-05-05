import streamlit as st
import pandas as pd
from main import extract_transactions, save_csv

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

if "trans_list" not in st.session_state:
    st.session_state["trans_list"] = []
if "seen_files" not in st.session_state:
    st.session_state["seen_files"] = []

st.title("Credit Card Statement Analyser")
files = st.file_uploader("Please insert your statment here", "pdf", accept_multiple_files=True)
trans_list = st.session_state["trans_list"]
seen_files = st.session_state["seen_files"] # tracks if a file has already been uploaded
for file in files:
    if file.name not in seen_files:
        seen_files.append(file.name)
        st.toast(f"Uploaded {file.name}", icon="✅", duration="short")
        transactions = extract_transactions(file)
        trans_list.extend(transactions)
    else:
        st.warning(f"{file.name} has already been uploaded")
        
        

if trans_list: 
    df = save_csv(trans_list, "output/transactions.csv")
    st.session_state["df"] = df
    st.success("Statements processed! Head to the Charts page.")

    by_month = df.groupby(["Month", "Year"])["Amount"].agg(Amount="sum", Purchases="count").reset_index()

    #order and sort the months
    by_month["Month"] = pd.Categorical(by_month["Month"], categories=month_order, ordered=True)
    by_month = by_month.sort_values(["Year", "Month"])
    #adds a new column to by_month that has the Month and year together
    by_month["Month Year"] = by_month["Month"].astype(str) + " " + by_month["Year"].astype(str)

    by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    st.session_state["by_month"] = by_month
    st.session_state["by_category"] = by_category