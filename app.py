import streamlit as st
import pandas as pd
from main import extract_transactions, save_csv
import plotly.express as px

pg = st.navigation([
    st.Page("pages/home.py", title="Home"), 
    st.Page("pages/charts.py", title="Charts"), 
    st.Page("pages/summary.py",title="Summary"),
    st.Page("pages/predictions.py", title="Next Month's Predictions")
    ])
pg.run()

#month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# st.title("Credit Card Statement Analyser")
# files = st.file_uploader("Please insert your statment here", "pdf", accept_multiple_files=True)
# trans_list = []
# seen_files = [] # tracks if a file has already been uploaded
# for file in files:
#     if file is not None and file.name not in seen_files:
#          seen_files.append(file.name)
#          st.toast(f"Uploaded {file.name}", icon="✅", duration="short")
#          transactions = extract_transactions(file)
#          trans_list.extend(transactions)
#     else:
#         st.warning(f"{file.name} has already been uploaded")
# if trans_list: 
#     df = save_csv(trans_list, "output/transactions.csv")
    # if df is not None:
    #     st.dataframe(df)

    #     # BAR CHART BY MONTH 
    #     by_month = df.groupby(["Month", "Year"])["Amount"].agg(Amount="sum", Purchases="count").reset_index()

    #     #order and sort the months
    #     by_month["Month"] = pd.Categorical(by_month["Month"], categories=month_order, ordered=True)
    #     by_month = by_month.sort_values(["Year", "Month"])
    #     #adds a new column to by_month that has the Month and year together
    #     by_month["Month Year"] = by_month["Month"].astype(str) + " " + by_month["Year"].astype(str)
    #     df["Month Year"] = df["Month"] + " " + df["Year"].astype(str)
    #     df["Month Year"] = pd.Categorical(df["Month Year"], categories=by_month["Month Year"], ordered=True)
    #     df = df.sort_values("Month Year")
    #     fig = px.bar(df, x="Month Year", y="Amount", color="Trans Date", title="Spending by Month")
    #     for _, row in by_month.iterrows():
    #         fig.add_annotation(
    #             x=row["Month Year"],
    #             y=row["Amount"],
    #             text=f"${row['Amount']:,.2f}",
    #             font=dict(
    #                 family="Courier New",
    #                 size=12,
    #                 color="#000000"
    #             ),
    #             yshift=5,
    #             showarrow=False
    #         )
    #     st.plotly_chart(fig)

    #     #st.bar_chart(df, x="Month", y="Amount")

    #     # BAR CHART BY CATEGORIES
    #     by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    #     st.bar_chart(by_category)

    #     # Summary table
    #     top_month_idx = by_month["Amount"].idxmax()
    #     top_month_name = by_month.loc[top_month_idx, "Month"]
    #     top_month_amount = by_month.loc[top_month_idx, "Amount"]

    #     #most expensive transaction
    #     top_trans_idx = df["Amount"].idxmax() 
    #     top_trans = df.loc[top_trans_idx, "Amount"]

    #     # most transactions in a month
    #     top_purchases_idx = by_month["Purchases"].idxmax()
    #     top_purchases = by_month.loc[top_purchases_idx, "Purchases"]
        
        
    #     for _, row in by_month.iterrows():
    #         # row["Month"] the month name
    #         # row["Amount"] the total amount
    #         # row["Purchases"] the amount of purchases
    #         month_df = df[df["Month"] == row["Month"]]

    #         #most expensive purchase for current month
    #         trans_idx = month_df["Amount"].idxmax() 
    #         purchase = month_df.loc[trans_idx, "Amount"]


    #         # col a is to indicate if it was the most expensive month or jus the month name
    #         # col b is to indicate the total of all transactions that month
    #         # col c is to indicate the most expensive transactions that month
    #         # col d is to indicate the number of transactions that month
    #         # each column should have a delta indicating the difference from the top version
    #         a, b, c, d = st.columns(4)
    #         if top_month_name == row["Month"]:
    #             a.metric("Most Expensive Month", top_month_name)
    #             b.metric("Total Purchased", value=f"${top_month_amount}", delta=0, delta_color="off")
    #             c.metric("Top Purchase", value=f"${purchase}", delta=round(purchase-top_trans, 2))
    #             d.metric("Number of Purchases", row["Purchases"], delta= round(row["Purchases"] - top_purchases, 2))
    #         else: 
    #             a.metric("Months Name", row["Month"])
    #             b.metric("Total Purchased", value=f"${row['Amount']:,.2f}", delta=round(row["Amount"] - top_month_amount, 2))
    #             c.metric("Top Purchase", value=f"${purchase}", delta=round(purchase - top_trans, 2))
    #             d.metric("Number of Purchases", row["Purchases"], delta=round(row["Purchases"] - top_purchases, 2))


