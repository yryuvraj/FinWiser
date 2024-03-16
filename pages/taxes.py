import streamlit as st
import pandas as pd
data = pd.read_csv('pages/data/income.csv')
income_value = int(data['income'])

