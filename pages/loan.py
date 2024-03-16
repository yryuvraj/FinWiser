import streamlit as st
import plotly.graph_objects as go
from csv import writer
from csv import reader


st.header("Learn how your finances will be impacted if you take a new loan: ")
goal = st.text_input("Enter loan title : ")
P = st.number_input("Enter Loan amount : ")
interest = st.number_input("Enter interest rate annually :  : ")
interest = interest / 100
interest /= 12
labels = []
sizes = []
expenses = []
expenses_amt = []
emi = 0
if goal:
    st.write(f"# {goal}")
if P != 0 and goal and interest != 0:
    n = st.slider('Choose Time period in years',step = 1, max_value=30) 
    n *= 12
    if n != 0:
        emi = P * interest * (((1 + interest)**n)/(((1+interest)**n)-1))
    amt_owned = emi*n 
    butt = st.button("Calculate")
    if butt:
        st.markdown(f"###  Estimated Monthly installment : {int(emi)}")
        st.markdown(f"###  Total Amount you will owe the lender will be : {int(amt_owned)}")
        with open('pages/data/income.csv', mode ='r') as file:
            csvFile = reader(file)
            for lines in csvFile:
                    continue
            print(lines)
        lines[3] = float(lines[3])
        st.markdown(f"###  Total Amount which will be left this month : {int(lines[3]-float(emi))}")
    expenses = ['Charity', 'Clothes', 'Food','Medicine','Study Materials','Travel',"Utilities","Wants"]
    expenses_amt = [0,0,0,0,0,0,0,0]
    with open('pages/data/data  - item.csv', 'r') as f_object:
        csvFile = reader(f_object)
        for lines in csvFile:
                for i in range(0,len(expenses)):
                     print(expenses[i])
                     print(lines[2])
                     if expenses[i] == lines[1]:
                          expenses_amt[i] += int(float(lines[3]))
        print(lines)
labels = expenses
if goal:
    labels.append(goal)
sizes = expenses_amt
sizes.append(int(emi))
labels.append(goal)
for i in range(0,len(sizes)):
    if i < len(sizes) and sizes[i] == 0:
          labels.pop(i)
          sizes.pop(i)
labels2 = ['Total Monthly Budget',goal]
with open('pages/data/income.csv', mode ='r') as file:
        csvFile = reader(file)
        for lines in csvFile:
                continue
        print(lines)
        lines[3] = float(lines[3])
sizes2 = [lines[3],int(emi)]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20)
fig.update_layout(title_text='Monthly Expenses', title_font_size=24)
fig1 = go.Figure(data=[go.Pie(labels=labels2, values=sizes2)])
fig1.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20)
fig1.update_layout(title_text='Loan vs allocated monthly budget', title_font_size=24)
agree = st.checkbox("Do you want to see your monthly expense pie chart? ")
if agree:
    st.plotly_chart(fig)
    st.plotly_chart(fig1)
