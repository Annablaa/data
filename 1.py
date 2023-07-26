import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('coaster_db.csv')

# ... (Rest of your data processing code) ...

# Create a Streamlit app
st.title('Coaster Data Exploration')

# Display the first few rows of the DataFrame
st.subheader('Coaster Data')
st.dataframe(df.head())

# Bar chart: Top 10 years coasters introduced
st.subheader('Top 10 Years Coasters Introduced')
top_years_count = df['year_introduced'].value_counts().head(10)
st.bar_chart(top_years_count)

# Histogram: Coaster Speed (mph)
st.subheader('Coaster Speed (mph) Histogram')
plt.figure()  # Create a new Matplotlib figure
plt.hist(df['speed_mph'], color='green', bins=20, edgecolor='black')  # Generate the histogram
st.pyplot(plt)  # Display the Matplotlib figure in Streamlit

# Density plot: Coaster Speed (mph)
st.subheader('Coaster Speed (mph) Density Plot')
fig_kde, ax_kde = plt.subplots()  # Create a new Matplotlib figure and axis
sns.kdeplot(df['speed_mph'], color='green', ax=ax_kde)  # Generate the density plot using Seaborn
st.pyplot(fig_kde)  # Display the Matplotlib figure using st.pyplot()

# Scatter plot: Coaster Speed vs Height
st.subheader('Coaster Speed vs Height')
fig_scatter, ax_scatter = plt.subplots()  # Create a new Matplotlib figure and axis
ax_scatter.scatter(df['speed_mph'], df['height_ft'])
ax_scatter.set_xlabel('Speed (mph)')
ax_scatter.set_ylabel('Height (ft)')
ax_scatter.set_title('Coaster Speed vs Height')
st.pyplot(fig_scatter)  # Display the Matplotlib figure using st.pyplot()


# Seaborn Scatter plot with hue: Coaster Speed vs Height with year_introduced as hue
st.subheader('Coaster Speed vs Height with Year Introduced as Hue')
fig_seaborn, ax_seaborn = plt.subplots()  # Create a new Matplotlib figure and axis
sns.scatterplot(x='speed_mph', y='height_ft', hue='year_introduced', data=df, ax=ax_seaborn)
st.pyplot(fig_seaborn)


