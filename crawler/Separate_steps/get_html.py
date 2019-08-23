# Gets the original HTML file. Downloading HTML directly would also do the trick
import requests
resp = requests.get('http://www.cs.unc.edu/~plaisted/comp455/')
with open('response.html', 'w') as f:
    f.write(resp.text)
