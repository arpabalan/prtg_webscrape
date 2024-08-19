from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

#get the url
page = requests.get(url)

#parser
soup = BeautifulSoup(page.text, 'html')


#print(soup)

table = soup.find_all('table')[1]
#print(soup.find_all('table')[1]) # return list of <tables> of the website


#print(soup.find('table', class_='wikitable sortable')) # string find <table> with class wiki table sortable

world_titles = table.find_all('th')

''''
for title in world_titles:
    print(title.text)
    '''

#world_table_titles = [title.text for title in world_titles] list comprehension
world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


df = pd.DataFrame(columns = world_table_titles)
print(df)


column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)


    length = len(df)
    df.loc[length] = individual_row_data


print(df)

#to save to csv
df.to_csv(r'C:\Users\Pabs\OneDrive\Desktop\desktop files\solarwinds_test.csv', index = False) # index false exclude the index number