import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from rich.logging import RichHandler
import logging as LOGGING

FORMAT = "%(message)s"
LOGGING.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)  
logger = LOGGING.getLogger("rich")

class PersonalFinance : 
    
    def __init__(self) : 

        self.main_data = 'data/data  - item.csv'
        self.additional_data = 'data/data  - Total_spending.csv'


    def read_data(self, data) : 
        if data == 'primary' :
            df = pd.read_csv(self.main_data)

        return df
    
    def preprocess_dataframe(self) : 
        
        df = pd.read_csv(self.main_data)
        
        df.rename({
                'date ' : 'date',
                'item_name ' : 'item_name',
                'item_category ' : 'item_category',
                'price ' : 'price'    
                }, axis = 1, inplace = True)

        df.dropna(inplace = True)
        date = df.date.str.split('/', expand =True)

        df['month'] = date[0]
        df['day'] = date[1]
        df['year'] = date[2]

        df.year = pd.to_numeric(df.year)
        df.month = pd.to_numeric(df.month)
        df.day = pd.to_numeric(df.day)

        df.date = pd.to_datetime(df.date)

        df['month_name'] = df.date.dt.month_name()
        
        LOGGING.debug('Preprocessing done')

        return df 
    

    def share_of_category(self) : 
        df = self.preprocess_dataframe()
        category_df = df.groupby(['item_category'])['price'].sum().reset_index()
        fig = px.pie(
            category_df, values = 'price', names = 'item_category', 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        return fig

    def plot_boxplot(self, feature) :
        df = self.preprocess_dataframe()
        dummy_df = df[df.item_category == feature]
        fig = go.Figure(data=[go.Box(x=dummy_df.price)])
        fig.update_traces(marker_color='rgb(255, 27, 0)')
        fig.update_layout(plot_bgcolor="white", title = feature.capitalize())
        return fig

    def find_max(self, category) : 
        df = self.preprocess_dataframe()
        dummy_df = df[df.item_category == category]
        final_df = dummy_df[dummy_df.price == dummy_df.price.max()]
        return final_df['item_name'].iloc[0], final_df['price'].iloc[0], final_df['date'].iloc[0]

    def total_spending(self) : 
        df = pd.read_csv(self.additional_data)
        df = df.T.reset_index()
        total_expense = df[0].iloc[4]
        df = df.drop(4)
        fig = px.pie(
            df, names = 'index', values = 0, 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        return fig, total_expense

    def plot_treemap(self) : 
        df = self.preprocess_dataframe()
        dummy_df = df.rename(columns = {'price' : 'total spending'})
        fig = px.treemap(
            dummy_df, path = [px.Constant('total spending'), 'item_name'], color='total spending',
            values = 'total spending', color_continuous_scale='reds',
        )

        return fig
