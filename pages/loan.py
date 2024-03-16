import streamlit as st
import matplotlib.pyplot as plt 
st.header("Learn how your finances will be impacted if you take a new loan: ")
goal = st.text_input("Enter loan title : ")
P = st.number_input("Enter Loan amount : ")
interest = st.number_input("Enter interest rate annually :  : ")
interest = interest / 100
interest /= 12
emi = 0
if goal:
    st.write(f"# {goal}")
if P != 0 and goal and interest != 0:
    n = st.slider('Choose Time period in years',step = 1, max_value=30) 
    n *= 12
    if n != 0:
        emi = P * interest * (((1 + interest)**n)/(((1+interest)**n)-1))
    amt_owned = emi + P
    st.markdown(f"###  Estimated Monthly installment : {int(emi)}")
    st.markdown(f"###  Total Amount you will owe the lender will be : {int(amt_owned)}")

fig, ax  = plt.subplots()
fig.set_size_inches(10,10,forward=True)
labels = ['Home','Electricity','Groceries']
font = {'weight' : 'normal',
        'size'   : 22}

plt.rc('font', **font)
labels.append(goal)
sizes = [30000, 1000, 5000, emi]
plt.style.use('dark_background')
ax.set_facecolor("black")
# Create a pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
 
# Display the plot in Streamlit
agree = st.checkbox("Do you want to see your monthly expense pie chart? ")
if agree:
    st.pyplot(fig)