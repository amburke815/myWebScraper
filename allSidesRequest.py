# allows us to easily grab HTML
import requests

# an example website with a lenient /robots.txt
url = 'https://www.allsides.com/media-bias/media-bias-ratings'

r = requests.get(url)

# [:x] ->  print the first x characters of this HTML doc
print(r.content[:100])
