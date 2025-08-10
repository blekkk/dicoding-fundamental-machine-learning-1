import os
import csv
import json
import pandas as pd
from google_play_scraper import reviews_all
from enum import Enum

class Sort(int, Enum):
    MOST_RELEVANT = 1
    NEWEST = 2
    RATING = 3

class GoogleScraper:
    def __init__(self):
        self.__scraped_data = None
        
    def scrape_all_reviews(self, app_id, lang, country, count, sort):
        try:
            print(f"Started scraping {app_id}")
            self.__scraped_data = reviews_all(
                app_id=app_id,         
                lang=lang,             
                country=country,         
                count=count,           
                sort=sort
            )
            
            return self
        except Exception as e:
            print(f"Error in scraping playstore review: {e}")
            raise e
        
    def to_csv_file(self, filepath):
        if not self.__scraped_data:
            raise ValueError("No data has been scraped")
        
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['review'])  # Menulis header kolom
            for review in self.__scraped_data:
                writer.writerow([review['content']])  # Menulis konten ulasan ke dalam file CSV
                
    def __repr__(self):
        if not self.__scraped_data:
            return f"<GoogleScraper object at {hex(id(self))}>"
        
        return json.dumps(self.__scraped_data, indent=4)
    
    def __str__(self):
        return self.__repr__()
    
    
def main():
    google_scraper = GoogleScraper()
    
    if not os.path.exists("csv_results"):
        os.mkdir('csv_results')

    google_scraper.scrape_all_reviews(app_id='com.aniplex.fategrandorder.en', lang='en', country='us', count=15000, sort=Sort.NEWEST).to_csv_file('csv_results/fate_us_new.csv')
    google_scraper.scrape_all_reviews(app_id='com.aniplex.fategrandorder.en', lang='en', country='uk', count=15000, sort=Sort.NEWEST).to_csv_file('csv_results/fate_uk_new.csv')
    
    root_folder = 'csv_results'

    file1 = os.path.join(root_folder, 'fate_uk_new.csv')
    file2 = os.path.join(root_folder, 'fate_us_new.csv')
    output_file = 'fate_merged.csv'

    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        
        merged_df = pd.concat([df1, df2], ignore_index=True)

        final_df = merged_df.drop_duplicates(subset=['review'], keep='first')

        final_df.to_csv(output_file, index=False)
        

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    
if __name__=='__main__':
    main()