import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Africa_climate_change.csv')
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d %H%M%S')
df = df.dropna(subset=['TAVG', 'TMAX'])
tunisia_data = df[df['COUNTRY'] == 'Tunisia']
cameroon_data = df[df['COUNTRY'] == 'Cameroon']
plt.figure(figsize=(12, 6))
plt.plot(tunisia_data['DATE'], tunisia_data['TAVG'], label='Tunisia')
plt.plot(cameroon_data['DATE'], cameroon_data['TAVG'], label='Cameroon')
plt.title('Average Temperature Fluctuations in Tunisia and Cameroon (1980-2023)')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.legend()
plt.show()
tunisia_data_1980_2005 = tunisia_data[(tunisia_data['DATE'].dt.year >= 1980) & (tunisia_data['DATE'].dt.year <= 2005)]
cameroon_data_1980_2005 = cameroon_data[(cameroon_data['DATE'].dt.year >= 1980) & (cameroon_data['DATE'].dt.year <= 2005)]
plt.figure(figsize=(12, 6))
plt.plot(tunisia_data_1980_2005['DATE'], tunisia_data_1980_2005['TAVG'], label='Tunisia')
plt.plot(cameroon_data_1980_2005['DATE'], cameroon_data_1980_2005['TAVG'], label='Cameroon')
plt.title('Average Temperature Fluctuations in Tunisia and Cameroon (1980-2005)')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.legend()
plt.show()
senegal_data = df[df['COUNTRY'] == 'Senegal']

senegal_data_1980_2000 = senegal_data[(senegal_data['DATE'].dt.year >= 1980) & (senegal_data['DATE'].dt.year <= 2000)]
senegal_data_2000_2023 = senegal_data[(senegal_data['DATE'].dt.year >= 2000) & (senegal_data['DATE'].dt.year <= 2023)]

plt.figure(figsize=(12, 6))
plt.hist(senegal_data_1980_2000['TAVG'], bins=30, alpha=0.5, label='1980-2000')
plt.hist(senegal_data_2000_2023['TAVG'], bins=30, alpha=0.5, label='2000-2023')
plt.title('Temperature Distribution in Senegal (1980-2000 vs 2000-2023)')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

avg_temp_per_country = df.groupby('COUNTRY')['TAVG'].mean().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(avg_temp_per_country['COUNTRY'], avg_temp_per_country['TAVG'])
plt.title('Average Temperature per Country')
plt.xlabel('Country')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=45)
plt.show()

egypt_data = df[df['COUNTRY'] == 'Egypt']
plt.figure(figsize=(12, 6))
plt.plot(egypt_data['DATE'], egypt_data['TMAX'])
plt.title('Maximum Temperature Fluctuations in Egypt (1980-2023)')
plt.xlabel('Year')
plt.ylabel('Maximum Temperature (°C)')
plt.show()