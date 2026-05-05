import streamlit as st
import pandas as pd
from main import extract_transactions, save_csv
import plotly.express as px


st.title("Credit Card Statement Analyser")
file = st.file_uploader("Please insert your statment here", "pdf")
if file is not None:
    st.success("Uploaded")
    transactions = extract_transactions(file)
    df = save_csv(transactions, "output/transactions.csv")
    if df is not None:
        st.dataframe(df)
        by_month = df.groupby("Month")["Amount"].sum().reset_index()
        fig = px.bar(df, x="Month", y="Amount", color="Trans Date", title="Spending by Month")
        for _, row in by_month.iterrows():
            fig.add_annotation(
                x=row["Month"],
                y=row["Amount"],
                text=f"${row['Amount']:,.2f}",
                font=dict(
                    family="Courier New",
                    size=12,
                    color="#000000"
                ),
                yshift=5,
                showarrow=False
            )
        st.plotly_chart(fig)

        #st.bar_chart(df, x="Month", y="Amount")
        by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
        st.bar_chart(by_category)
