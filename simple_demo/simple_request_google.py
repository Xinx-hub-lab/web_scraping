
## Terminal: 
## Enter 'python' to start
## Enter ^D (Control + D) to exit

import requests

response = requests.request('GET', 'http://www.google.com') ## http is needed
print(response.status_code)
print(response.encoding)
print(response.text)