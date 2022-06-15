from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup 
from newspaper import Article
from tqdm import tqdm
import pandas as pd

def scrap_page(page : int):
    scraped_data = []

    while page<=134:
        page += 1
         
        main_page_url = f"https://www.yjc.news/fa/allnews?page={page}"
      
         
        html = requests.get(main_page_url).text

        soup = BeautifulSoup(html, features='lxml')

        links = soup.find_all('h2')


        for link in tqdm(links):
            page_url = 'https://www.yjc.news' + link.a['href']
            try:
                article = Article(page_url)  
                article.download()
                article.parse()
                scraped_data.append({'url' : page_url, 'text' : article.text , 'title' : article.title}) 
            except:
                print(f"failed to process page: {page_url}")
                    
    df = pd.DataFrame(scraped_data)
    df.to_csv(f'yjc.csv')


if __name__ == '__main__':
    scrap_page(1)
    

             
