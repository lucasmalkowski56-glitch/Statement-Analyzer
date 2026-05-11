import streamlit as st
import pandas as pd
import plotly.express as px

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

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

df = st.session_state["df"]

st.title("Chart Visualisations")

st.dataframe(df)

# BAR CHART BY MONTH 

df["Month Year"] = df["Month"] + " " + df["Year"].astype(str)
df["Month Year"] = pd.Categorical(df["Month Year"], categories=by_month["Month Year"], ordered=True)
df = df.sort_values("Month Year")
fig = px.bar(df, x="Month Year", y="Amount", color="Trans Date", title="Spending by Month")
for _, row in by_month.iterrows():
    fig.add_annotation(
        x=row["Month Year"],
        y=row["Amount"],
        text=f"${row['Amount']:,.2f}",
        font=dict(
            family="Courier New",
            size=12,
            color="#000000"
        ),
        yshift=10,
        yanchor="bottom",
        showarrow=False
    )
st.plotly_chart(fig)

#st.bar_chart(df, x="Month", y="Amount")

# BAR CHART BY CATEGORIES
st.bar_chart(by_category)

