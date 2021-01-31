# saves an html doc locally so that we don't overload a server with requests
def save_html(html, path):
    with open(path, 'wb') as f: # wb - write bytes (fixes encoding issues)
        f.write(html)
# example:
    # save_html(r.content, 'google.com')

# to open the saved html
def open_html(path):
    with open(path, 'rb') as f: # rb - read bytes
        return f.read()
#example: 
# html = open_html('google.com')
