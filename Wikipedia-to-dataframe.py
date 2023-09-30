#https://www.youtube.com/watch?v=8dTpNajxaH0&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=57
from bs4 import BeautifulSoup
import requests
import pandas as pd

url ='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
soup= BeautifulSoup(page.text, 'html')
table = soup.find_all('table')[1]
world_titles = table.find_all('th')
#print(world_titles)

world_table_titles =[]
for title in world_titles:
     world_table_titles.append(title.text.strip())
#print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)
df
column_data = table.find_all('tr')

#loop through each element in the list column_data, find all the td tags within that row, store the stripped text from the td tag (not the th tags)
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #append the row onto the dataframe by putting it into the next position in the dataframe
    length = len(df)
    df.loc[length]=individual_row_data
df
