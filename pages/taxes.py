import streamlit as st
import pandas as pd
import streamlit as st

data = pd.read_csv('pages/data/income.csv')
income_value = int(data['income'])

tax_amount = 0

total_income = income_value * 12
if total_income == 0:
    st.subheader("Please enter your income in the sidebar to calculate taxes.")
else:
    if total_income <= 250000:
        tax_amount = 0
    elif total_income > 250000 and total_income <= 300000:
        tax_amount = (total_income - 250000) * 0.05
    elif total_income > 300000 and total_income <= 500000:
        tax_amount = (total_income - 300000) * 0.05
    elif total_income > 500000 and total_income <= 600000:
        tax_amount = (total_income - 500000) * 0.1 + 10000
    elif total_income > 600000 and total_income <= 900000:
        tax_amount = (total_income - 600000) * 0.1 + 20000
    elif total_income > 900000 and total_income <= 1200000:
        tax_amount = (total_income - 900000) * 0.15 + 50000
    elif total_income > 1200000 and total_income <= 1500000:
        tax_amount = (total_income - 1200000) * 0.2 + 125000
    elif total_income > 1500000:
        tax_amount = (total_income - 1500000) * 0.3 + 200000

st.title("Income Tax Calculator")
st.image('assets/taxes.png')

st.markdown("""
    <div style='color: rgb(56,182,255); font-size: 25px;'>
        The Income Tax Calculator is a simple tool that allows you to calculate your income tax liability based on your annual income. It is essential to understand your tax liability to plan your finances effectively and ensure that you have enough funds to cover your tax obligations.
        
    """, unsafe_allow_html=True)
#rgb(56,182,255)

st.markdown(f"##### [Please enter your income in the finance tracker, ignore if you have already updated it.]")
st.markdown(f"## Your yearly income is: ₹{total_income}")
st.markdown(f"## Taxes to be paid: ₹{tax_amount}")

  

