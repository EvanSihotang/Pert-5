import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data_path = 'players.csv'  # Replace this with the path to your CSV file
data = pd.read_csv("players.csv")

# Data preparation and cleaning
data_cleaned = data.dropna(subset=['market_value_in_eur'])
data_cleaned['date_of_birth'] = pd.to_datetime(data_cleaned['date_of_birth'], errors='coerce')
data_cleaned['contract_expiration_date'] = pd.to_datetime(data_cleaned['contract_expiration_date'], errors='coerce')
median_height = data_cleaned['height_in_cm'].median()
data_cleaned['height_in_cm'].fillna(median_height, inplace=True)
data_cleaned['foot'].fillna(data_cleaned['foot'].mode()[0], inplace=True)
data_cleaned['age'] = 2024 - pd.DatetimeIndex(data_cleaned['date_of_birth']).year

# Streamlit application title
st.title('Top 10 Players by Market Value')

# Show the top 10 players by market value
top_10_players = data_cleaned[['name', 'market_value_in_eur']].sort_values(by='market_value_in_eur', ascending=False).head(10)

# Display the dataframe in Streamlit
st.subheader('Top 10 Players:')
st.dataframe(top_10_players)

# Visualization: Bar plot of top 10 players
st.subheader('Top 10 Players by Market Value')

# Create the bar plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='market_value_in_eur', y='name', data=top_10_players, palette='Blues_r', ax=ax)
ax.set_title('Top 10 Players by Market Value')
ax.set_xlabel('Market Value in EUR')
ax.set_ylabel('Player Name')

# Display the plot in Streamlit
st.pyplot(fig)