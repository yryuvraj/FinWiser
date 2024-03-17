import streamlit as st


def main():
    st.title("Redirect to TradingView")
    st.image("assets/chart.png")
    redirect_url = "https://in.tradingview.com/chart/DDCpx0QD/?symbol=NSE%3ANIFTY"
    if st.button("View on TradingView"):
        st.markdown(f"[Click here to view on TradingView]({redirect_url})")


if __name__ == "__main__":
    main()
