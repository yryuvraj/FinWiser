import streamlit as st

st.set_page_config(
    page_title="FinWiser",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded")
st.image("assets/logo.png")
st.header("An application to make people financially literate.")
st.image('assets/pyramid.png', width = 600)
st.header("what finwiser aims to solve?")
#st.subheader("Basic financial literacy is essential for anyone looking to secure their financial future. One of the fundamental principles of financial literacy is understanding the importance of investing. Investing allows individuals to grow their wealth over time, beating inflation and achieving long-term financial goals. However, many people are intimidated by the complexity of investing and are unsure of where to start. FinWiser aims to solve this problem by providing a simple and intuitive platform for people to learn about investing and make informed financial decisions.")

st.markdown("""
    <div style='color: rgb(126,217,87); font-size: 25px;'>
        Basic financial literacy is essential for anyone looking to secure their financial future. One of the fundamental principles of financial literacy is understanding the importance of investing. Investing allows individuals to grow their wealth over time, beating inflation and achieving long-term financial goals. However, many people are intimidated by the complexity of investing and are unsure of where to start. FinWiser aims to solve this problem by providing a simple and intuitive platform for people to learn about investing and make informed financial decisions.
    </div>
    """, unsafe_allow_html=True)

st.header("what is sip and compounding?")

st.markdown("""
    <div style='color: rgb(126,217,87); font-size: 25px;'>
        Systematic Investment Plan (SIP) is a popular investment strategy where individuals invest a fixed amount regularly, benefiting from rupee cost averaging and the power of compounding. Compounding, often referred to as the "eighth wonder of the world" by Albert Einstein, is the process where investments generate earnings, which are reinvested to generate more earnings over time.
    </div>
    """, unsafe_allow_html=True)

st.header("why is budgeting important?")

st.markdown("""
    <div style='color: rgb(126,217,87); font-size: 25px;'>
        Budgeting is the process of creating a plan to spend your money. It is essential for managing your money effectively, ensuring that you have enough money for the things you need and want. Budgeting can help you control your spending, save more money, and achieve your financial goals.    
    </div>
    """, unsafe_allow_html=True)

st.header("why is it important to keep track of your liabilities?")

st.markdown("""
    <div style='color: rgb(126,217,87); font-size: 25px;'>
        Keeping track of your liabilities is crucial for understanding your financial health. It helps you understand how much you owe, to whom, and the terms of repayment. A very common example of this is Loans. Develop a comprehensive budget that includes your loan payments as an essential expense. This will help you allocate your income effectively and ensure that you have enough funds to cover your loan obligations while also meeting other financial goals.
    </div>
    """, unsafe_allow_html=True)

st.header("why is it important to invest in stocks?")

st.markdown("""
    <div style='color: rgb(126,217,87); font-size: 25px;'>
        Investing in stocks can help you grow your wealth over time, beat inflation, and achieve your long-term financial goals. Stocks have historically provided higher returns than other asset classes, making them an essential part of a diversified investment portfolio. However, investing in stocks also comes with risks, and it is essential to understand these risks and invest wisely.
    </div>
    """, unsafe_allow_html=True)