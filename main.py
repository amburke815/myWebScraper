from bs4 import BeautifulSoup
import requests

## 1. GET HMTL
###############################################################################
# set the URL
url = 'https://www.allsides.com/media-bias/media-bias-ratings'

r = requests.get(url)
# [:x] --> print the first x characters in this HTML doc of url
print(r.content[:100])

# BS constructor creates a new object 'soup' that parses the HTML content
soup = BeautifulSoup(r.content, 'html.parser')

## 2. EXTRACT DATA
##############################################################################
### see elementSelection.py for notes on CSS selectors ###
# select all table rows <tr> from a table body <tbody>
rows = soup.select('tbody tr')

# rows[x] gets the x'th row of the rows in the table, for example:
row0 = rows[0]

# gets the text of the news source contained within the row
name0 = row0.select_one('source-title').text.strip() # source title is the bottom-level class of the element

# TEST: print this row's source "ABC News (Online)"
print(row0)