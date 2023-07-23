import requests
from bs4 import BeautifulSoup

def fetch_article_links(folder_link):
    article_links = []
    page_number = 1
    while True:
        try:
            response = requests.get(f"https://help.zebpay.com{folder_link}/page/{page_number}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                articles_on_page = soup.select('section.article-list.c-list a.c-link')
                if not articles_on_page:
                    break
                article_links.extend([a['href'] for a in articles_on_page])
                page_number += 1
            else:
                print(f"Failed to fetch data from {folder_link}/page/{page_number}")
                break
        except Exception as e:
            print(f"An error occurred with {e}")
    return article_links

def scrape_and_save_file_data(url, filename):
    try:
        response = requests.get(f"https://help.zebpay.com{url}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            file_data = soup.find('article', class_='article-body')
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(str(file_data))
            print(f"Data from {url} has been scraped and saved in {filename}")
        else:
            print(f"Failed to fetch data from {url}")
    except Exception as e:
        print(f"There was an error with {e}")

r = requests.get('https://help.zebpay.com/support/solutions')

with open('index.html', 'w') as impfile:
    impfile.write(r.text)

with open('index.html', 'r') as f:
        html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()

folder_links = [a['href'] for a in soup.select('section.cs-g.article-list a[title]')]
folder_links = folder_links[1:]

all_article_links = []
for folder_link in folder_links:
    article_links = fetch_article_links(folder_link)
    all_article_links.extend(article_links)

for idx, url in enumerate(all_article_links, start=1):
    filename = f"scraped_data/article_{idx}.html"
    scrape_and_save_file_data(url, filename)