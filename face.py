import streamlit as st
import pandas as pd

# Load the CSV file
csv_file_path = 'recognition_log.csv'
df = pd.read_csv(csv_file_path)

# Streamlit app
st.title('Face Recognition Log Viewer')

# Display the dataframe
st.write(df)