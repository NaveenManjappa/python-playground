import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

daily_data = data['daily']

df = pd.DataFrame({
    'date': daily_data['time'],
    'temp_max': daily_data['temperature_2m_max'],
    'temp_min': daily_data['temperature_2m_min']
})

df['date'] = pd.to_datetime(df['date'])

print(df)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temp_max'], marker='o', label='Max Temp')
plt.plot(df['date'], df['temp_min'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

# create the last 7 days weather data like above for London
url_london = f"https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response_london = requests.get(url_london)
data_london = response_london.json()
print(data_london)

daily_london = data_london['daily']

df_london = pd.DataFrame({
  'date': daily_london['time'],
  'temp_max': daily_london['temperature_2m_max'],
  'temp_min': daily_london['temperature_2m_min']
})

df_london['date'] = pd.to_datetime(df_london['date'])

print(df_london)

# Create the plot for London
plt.figure(figsize=(10, 6))
plt.plot(df_london['date'], df_london['temp_max'], marker='o', label='London Max Temp')
plt.plot(df_london['date'], df_london['temp_min'], marker='o', label='London Min Temp')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('London Weather - Past 7 Days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('weather_chart_london.png')
plt.show()

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/paris_weather.csv', index=False)
df_london.to_csv('data/london_weather.csv', index=False)