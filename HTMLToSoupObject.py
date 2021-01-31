from bs4 import BeautifulSoup

# BS constructor creates a new object 'soup' that parses the HTML content
soup = BeautifulSoup(r.content, 'html.parser')
