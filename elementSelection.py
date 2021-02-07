import requests
from bs4 import BeautifulSoup


# to get a tag <x>stuff</x>, use select_one(x) to return a single element
# select(x) returns a list of elements

# CSS selectors
    # select_one('a') gets an anchor
    # select_one('body') gets a body

    # select_one('.temp') gets the element of CLASS temp: <a class="temp"></a>

    # select_one('#temp') gets the element of ID temp: <a id="temp"></a>

    # select_one('.temp.example') gets the element of BOTH CLASSES temp and example: <a class="temp example"></a>

    # select_one('.temp .example') gets the element with class example that is nested inside of the parent class temp: <div class="temp"><a class="example"></a></div> 

    # select_one('.temp a') gets the anchor element nested inside of a parent element with class temp: <div class="temp"><a></a></div>

    
# Finding selectors in chrome
    # inspect element > copy > copy CSS selector


# selecting all table rows <tr> from a table body <tbody>
rows = soup.select('tbody tr') # can just use tbody since there's only one <tbody> on this page

# now we can use rows[x] to get the x'th row of rows
row0 = rows[0]

# gets the text of the news source contained within row 
name0 = row0.select_one('soure-title').text.strip() # source title is the bottom-level class of the element

print(name)
