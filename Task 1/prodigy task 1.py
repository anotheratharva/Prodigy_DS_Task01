

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_369784.csv', skiprows=4)


df_2022 = df[['Country Name', '2022']].dropna()
df_2022 = df_2022.sort_values(by='2022', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(df_2022['Country Name'], df_2022['2022'], color='skyblue')
plt.xticks(rotation=45)
plt.title('Top 10 Countries by Population (2022)')
plt.ylabel('Population')
plt.tight_layout()
plt.show()

plt.hist(df_2022['2022'], bins=20, edgecolor='black')
plt.title('Distribution of Population Sizes (2022)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.show()
