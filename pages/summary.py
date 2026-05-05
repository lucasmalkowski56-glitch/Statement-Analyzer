import streamlit as st
import pandas as pd
from main import extract_transactions, save_csv
import plotly.express as px


if "df" not in st.session_state:
    st.warning("Please upload statements on the Home page first.")
    st.stop()
elif "by_month" not in st.session_state:
    st.warning("by_month not in session_state")
    st.stop()
elif "by_category" not in st.session_state:
    st.warning("by_month not in session_state")
    st.stop()

df = st.session_state["df"]
by_month = st.session_state["by_month"]
by_category = st.session_state["by_category"]

# Summary table
top_month_idx = by_month["Amount"].idxmax()
top_month_name = by_month.loc[top_month_idx, "Month"]
top_month_amount = by_month.loc[top_month_idx, "Amount"]

#most expensive transaction
top_trans_idx = df["Amount"].idxmax() 
top_trans = df.loc[top_trans_idx, "Amount"]

# most transactions in a month
top_purchases_idx = by_month["Purchases"].idxmax()
top_purchases = by_month.loc[top_purchases_idx, "Purchases"]


for _, row in by_month.iterrows():
    # row["Month"] the month name
    # row["Amount"] the total amount
    # row["Purchases"] the amount of purchases
    month_df = df[df["Month"] == row["Month"]]

    #most expensive purchase for current month
    trans_idx = month_df["Amount"].idxmax() 
    purchase = month_df.loc[trans_idx, "Amount"]


    # col a is to indicate if it was the most expensive month or jus the month name
    # col b is to indicate the total of all transactions that month
    # col c is to indicate the most expensive transactions that month
    # col d is to indicate the number of transactions that month
    # each column should have a delta indicating the difference from the top version
    a, b, c, d = st.columns(4)
    if top_month_name == row["Month"]:
        a.metric("Most Expensive Month", top_month_name)
        b.metric("Total Purchased", value=f"${top_month_amount}", delta=0, delta_color="off")
        c.metric("Top Purchase", value=f"${purchase}", delta=round(purchase-top_trans, 2))
        d.metric("Number of Purchases", row["Purchases"], delta= round(row["Purchases"] - top_purchases, 2))
    else: 
        a.metric("Months Name", row["Month"])
        b.metric("Total Purchased", value=f"${row['Amount']:,.2f}", delta=round(row["Amount"] - top_month_amount, 2))
        c.metric("Top Purchase", value=f"${purchase}", delta=round(purchase - top_trans, 2))
        d.metric("Number of Purchases", row["Purchases"], delta=round(row["Purchases"] - top_purchases, 2))

