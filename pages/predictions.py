import streamlit as st
import model as m
import datetime as dt
from dateutil.relativedelta import relativedelta
import plotly.express as px

#get df, by_month, and by_category from session state
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

#Extract the monthly totals in order
montly_totals = by_month["Amount"].tolist()

#train the model with the totals and train it once then store in session state
if "model" not in st.session_state:
    model, X_max = m.train_model(montly_totals)
    st.session_state["model"] = model
    st.session_state["X_max"] = X_max
model = st.session_state["model"]
X_max = st.session_state["X_max"]

#predict the next month
prediction = m.predict_next_month(model, montly_totals[-3:], X_max)
prediction = round(max(0,prediction),2)

#find what month and year it is predicting
last_row = by_month.iloc[-1] #gets the last row of the dataframe
last_month = last_row["Month"] #gets the "month" value from that frame, ex:"Feb"
last_year = int(last_row["Year"]) #gets the "Year" value, ex: 2026

date = dt.datetime.strptime(f"{last_month} {last_year}", "%b %Y")

next_month = date + relativedelta(months=1)

# next month string
month = next_month.strftime("%B")

#display info
st.title("Next Months Predicted Spending")
a, b, c = st.columns(3)

a.metric("Year", next_month.year)
b.metric("Month", month)
c.metric("Prediction", prediction)



# ============================ BUDGET RECOMMENDATION ============================

# calculate each category's percentage of total historical spending 
category_pct = by_category / by_category.sum() 

# get the suggested budget per category
category_bdg = category_pct * prediction #currently a pandas series

# convert to DataFrame
category_bdg = category_bdg.reset_index()
category_bdg.columns = ["Category", "Amount"]
category_bdg["Amount"] = category_bdg["Amount"].round(2)

#make pie chart
fig = px.pie(category_bdg, names="Category", values="Amount", title="Budget Recommendation by Categories")
st.plotly_chart(fig)

st.dataframe(category_bdg)