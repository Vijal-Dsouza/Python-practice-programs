import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
cleaned_text = soup.get_text()
print(cleaned_text)