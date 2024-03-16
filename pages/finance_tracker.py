import streamlit as st
from pages.finance_tracker_data.finance import PersonalFinance
import pages.finance_tracker_data.markdown as md
from csv import writer
from csv import reader
from datetime import datetime
df = PersonalFinance()
 
PAGE_CONFIG = {"page_title":"Personal Finance", 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)   
months = [31,29,31,30,31,30,31,31,30,31,30,31]
st.sidebar.markdown("## Options")
sidebar_main = st.sidebar.selectbox('Navigation', ['Home', 'See Finances', 'Edit Monthly Income'])
 
if sidebar_main == 'Home' : 
    st.title('Personal Finance Dashboard')

    banner = md.headerSection()
    st.markdown(banner,unsafe_allow_html=True)
    
    st.markdown("""
    ## Enter Expense :  
    """)
    #item_date = st.date_input("Enter date of expense : ")
    now = datetime.now()
    item_date = now.strftime("%m/%d/%Y")
    day = now.strftime("%d")
    month = now.strftime('%m')
    print("month is : ",month)
    print("day:", day)
    print(item_date)
    
    option = st.selectbox(
     'Choose type of expense: ',
     ('Charity', 'Clothes', 'Food','Medicine','Study Materials','Travel',"Utilities","Wants"))
    item_title = st.text_input("Enter name of expense : ")
    if item_title == '':
        st.warning('Please enter the name of expense')
    item_price = st.number_input("Enter cost of expense : ")
    if item_price <=0:
        st.warning('Please enter a valid cost of expense')
    submit = st.button("Submit")
    L = [item_date,option,item_title,item_price]
    print(L)

    if submit:
        with open('pages/data/data  - item.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(L)
            f_object.close()
        lines = []
        with open('pages/data/income.csv', mode ='r') as file:
            csvFile = reader(file)
            for lines in csvFile:
                    continue
            print(lines)
        lines[3] = float(lines[3])
        lines[3] -= L[3]
        with open('pages/data/income.csv', 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(['income','invest_amt','save_amt','spend_amt'])
            writer_object.writerow(lines)
            f_object.close()
        lines = []
        with open('pages/data/income.csv', mode ='r') as file:
            csvFile = reader(file)
            for lines in csvFile:
                    continue
        st.subheader(f"Your daily budget is : {round(float(lines[3])/(months[0] - int(day)),1)}")
        st.subheader(f"The money you can spend this month is : {round(float(lines[3]),1)}")
        if float(lines[3]) < 0:
            st.subheader("You are over your budget!")

 
elif sidebar_main == 'See Finances' : 
    st.title('Expense dashboard')
    sidebar_sub = st.sidebar.radio('Navigation', ['Expense', 'Category', 'boxplot', 'total expenses', 'treemap'])
    
    data = df.preprocess_dataframe().tail()

    st.markdown(
            """
            ##### After preprocessing the data looks like this
            """
        )
    st.dataframe(data.head())
    if sidebar_sub == 'See Finances' : 

        st.markdown(
            """
            ##### Check the expenses 
            """
        ) 
        
        col1, col2 = st.columns(2)
        with col1 : 
            daily = st.button('Daily') 

        with col2 :  
            monthly = st.button('Monthly')
        
        if monthly : 
            st.plotly_chart(df.plot_expenses('month')[0])
            percent = df.plot_expenses('month')[1]

            if percent > 0 : 
                st.write('which is ',percent,'%',' higher than prev month')
            else : 
                st.write('which is ',abs(percent),'%',' lower than prev month')

        else : 
            st.plotly_chart(df.plot_expenses('date'))

    elif sidebar_sub == 'Category' :
        st.markdown(
            """
            ##### Category wise expenses 
            """
        ) 
        st.plotly_chart(df.share_of_category())

    elif sidebar_sub == 'boxplot' : 
        st.markdown(
            """
            ##### Category wise boxplot 
            """
        ) 
        col1, col2, col3 = st.columns(3)
        with col1 : 
            food = st.button('food') 

        with col2 :  
            travel = st.button('travel')
        
        with col3 :  
            wants = st.button('wants')

        if travel :
            st.plotly_chart(df.plot_boxplot('travel'))
        if wants :
            st.plotly_chart(df.plot_boxplot('wants'))
        else: 
            st.plotly_chart(df.plot_boxplot('food'))

    elif sidebar_sub == 'total expenses' : 
        st.markdown(
            """
            ##### Total Expenses 
            """
        ) 
        st.plotly_chart(df.total_spending()[0])
        st.write('Total amount spent is ',df.total_spending()[1])

    else : 
        st.markdown(
            """
            ##### Spending on items 
            """
        ) 
        st.plotly_chart(df.plot_treemap())

elif sidebar_main == 'Edit Monthly Income' : 
    monthly_income = st.number_input("Enter monthly income : ")
    invest_amt = 0
    use_amt = 0
    save_amt = 0
    if monthly_income > 100000:
        invest_amt = 0.5 * monthly_income
        use_amt = 0.3 * monthly_income
        save_amt = 0.2 * monthly_income
    elif monthly_income > 60000 and monthly_income < 100000:
        invest_amt = 0.3 * monthly_income
        use_amt = 0.5 * monthly_income
        save_amt = 0.2 * monthly_income
    elif monthly_income > 30000 and monthly_income < 60000:
        invest_amt = 0.2 * monthly_income
        use_amt = 0.5 * monthly_income
        save_amt = 0.3 * monthly_income
    else:
        invest_amt = 0.2 * monthly_income
        use_amt = 0.6 * monthly_income
        save_amt = 0.2 * monthly_income
    st.subheader(f"You should invest {int(invest_amt)}")
    st.subheader(f"You should save {int(save_amt)}")
    st.subheader(f"You should spend {int(use_amt)}")
    L = [monthly_income, invest_amt, save_amt, use_amt]
    submit = st.button("Submit")
    if submit:
        with open('pages/data/income.csv', 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(['income','invest_amt','save_amt','spend_amt'])
            writer_object.writerow(L)
            f_object.close()
else : 
    # dropdown
    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on food :')
    with col2 :
        check = st.button('check', key = 1)
    
    if check : 
        st.write('I ate ', df.find_max('food')[0], ' on ', df.find_max('food')[2].date(), ' with ', df.find_max('food')[1])
    
    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on travel :')
    with col2 :
        check = st.button('check', key = 2)
    
    if check : 
        st.write('I used ', df.find_max('travel')[0], ' on ', df.find_max('travel')[2].date(), ' for ', df.find_max('travel')[1])

    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on wants :')
    with col2 :
        check = st.button('check', key = 3)
    
    if check : 
        st.write('I have spent on ', df.find_max('wants')[0], ' on ', df.find_max('wants')[2].date(), ' for ', df.find_max('wants')[1])

footer = md.footerSection()
st.markdown(footer,unsafe_allow_html=True) 