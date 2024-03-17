import streamlit as st


def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)


def main():
    st.title("Compound Interest Calculator")
    st.image("assets/lumpsump.png")

    principal = st.number_input("Enter the principal amount:", min_value=0.0)
    rate = st.number_input("Enter the annual interest rate (%):", min_value=0.0)
    time = st.number_input("Enter the time period (in years):", min_value=0.0)

    if st.button("Calculate"):
        result = compound_interest(principal, rate, time)
        st.subheader(f"The amount after {time} years will be: ₹{result:.2f}")


if __name__ == "__main__":
    main()
