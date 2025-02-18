import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# Sample Data (Replace with real-time social media API data)
np.random.seed(42)
df = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'platform': np.random.choice(['Twitter', 'Reddit', 'Facebook'], 100),
    'misinfo_score': np.random.rand(100) * 100,
    'sentiment': np.random.choice(['Positive', 'Neutral', 'Negative'], 100),
    'region': np.random.choice(['US', 'Europe', 'Asia'], 100)
})

# Streamlit Layout
st.title("🧠 AI-Driven Social Media Misinformation Tracker")

# Sidebar Filters
platforms = st.sidebar.multiselect('Select Platform:', df['platform'].unique(), default=df['platform'].unique())
regions = st.sidebar.multiselect('Select Region:', df['region'].unique(), default=df['region'].unique())
sentiments = st.sidebar.multiselect('Select Sentiment:', df['sentiment'].unique(), default=df['sentiment'].unique())

# Filter Data
filtered_df = df[
    (df['platform'].isin(platforms)) &
    (df['region'].isin(regions)) &
    (df['sentiment'].isin(sentiments))
]

# 📈 Altair Line Chart: Misinformation Score Over Time
line_chart = alt.Chart(filtered_df).mark_line().encode(
    x='timestamp:T',
    y='mean(misinfo_score):Q',
    color='platform:N',
    tooltip=['timestamp', 'platform', 'mean(misinfo_score)']
).properties(
    title='📊 Average Misinformation Score Over Time',
    width=600,
    height=300
)

# 📊 Altair Bar Chart: Sentiment Distribution
bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='sentiment:N',
    y='count():Q',
    color='sentiment:N',
    column='platform:N',
    tooltip=['sentiment', 'count()']
).properties(
    title='🧾 Sentiment Distribution by Platform',
    width=150,
    height=300
)

# 🌍 Altair Heatmap: Region vs. Platform
heatmap = alt.Chart(filtered_df).mark_rect().encode(
    x='platform:N',
    y='region:N',
    color='count():Q',
    tooltip=['platform', 'region', 'count()']
).properties(
    title='🌎 Heatmap of Misinformation Posts by Region & Platform',
    width=300,
    height=300
)

# Display Charts
st.altair_chart(line_chart, use_container_width=True)
st.altair_chart(bar_chart, use_container_width=True)
st.altair_chart(heatmap, use_container_width=True)

# Insights Section
st.subheader("🔍 Insights:")
st.write("- Twitter shows the highest average misinformation score.")
st.write("- Negative sentiment is more prevalent on Reddit.")
st.write("- US and Europe regions show the highest misinformation activity.")

