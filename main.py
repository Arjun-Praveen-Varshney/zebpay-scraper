import requests
# import time
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

# r = requests.get('https://help.zebpay.com/support/home')
# with open('index.html', 'w') as f:
#     f.write(r.text)
with open('index.html', 'r') as f:
        html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()

# sections = soup.find_all('section', class_='cs-g article-list')

# # Iterate through each section and extract article links
# article_links = []
# for section in sections:
#     article_links.extend([article_link['href'] for article_link in section.find_all('a', href=True)])

# # Function to scrape data from an article URL and save it to a file
# def scrape_and_save(url, filename):
#     service = ChromeService(executable_path='chromedriver.exe')
#     driver = webdriver.Chrome(service=service)

#     try:
#         driver.get(f"https://help.zebpay.com{url}")
#         # Wait for a few seconds to ensure dynamic content is loaded
#         time.sleep(5)

#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         # Modify this part to extract the specific data you want from the article
#         article_data = soup.get_text()  # Here, we're saving the whole text of the article

#         with open(filename, 'w', encoding='utf-8') as file:
#             file.write(article_data)
#         print(f"Data from {url} has been scraped and saved in {filename}")
#     except Exception as e:
#         print(f"Failed to fetch data from {url}: {e}")
#     finally:
#         driver.quit()

# # Scrape data from each article URL and save it into different files
# for idx, url in enumerate(article_links, start=1):
#     filename = f"files/article_{idx}.html"
#     scrape_and_save(url, filename)

# print(soup.title.string)
# print(soup.title.name)

sections = soup.select('section.cs-g.article-list ul')
article_links = []
for section in sections:
    article_links.extend([article_link['href'] for article_link in section.select('li.article a[href]')])

# Function to scrape data from an article URL and save it to a file
def scrape_and_save(url, filename):
    response = requests.get(f"https://help.zebpay.com{url}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Modify this part to extract the specific data you want from the article
        article_data = soup.get_text()
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(article_data)
        print(f"Data from {url} has been scraped and saved in {filename}")
    else:
        print(f"Failed to fetch data from {url}")

# Scrape data from each article URL and save it into different files
for idx, url in enumerate(article_links, start=1):
    filename = f"files/article_{idx}.html"
    scrape_and_save(url, filename)