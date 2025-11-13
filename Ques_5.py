import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]

response = requests.get(url)
html_content = response.text

print("Original HTML Content:")
print(html_content)

print("\nCleaned Text Content:")
soup = BeautifulSoup(html_content, 'html.parser')
cleaned_text = soup.get_text()
print(cleaned_text)