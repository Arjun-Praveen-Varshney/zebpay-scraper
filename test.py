import requests
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
        html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()

# Find all the folder links within the section
folder_links = [a['href'] for a in soup.select('section.cs-g.article-list a[title]')]
folder_links = folder_links[1:]

def scrape_and_save_folder(url, foldername):
    response = requests.get(f"https://help.zebpay.com{url}")
    if response.status_code == 200:
        with open(foldername, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Data from {url} has been scraped and saved in {foldername}")
    else:
        print(f"Failed to fetch data from {url}")

# Scrape data from each article URL and save it into different files
for idx, url in enumerate(folder_links, start=1):
    foldername = f"folders/title_{idx}.html"
    scrape_and_save_folder(url, foldername)

new_section_links = [a['href'] for a in soup.select('section.article-list.c-list a.c-link')]

# Print the fetched folder links
response=requests.get(f'https://help.zebpay.com/support/solutions/folders/44001201694')
with open('test.html', 'w') as fo:
        fo.write(response.text)