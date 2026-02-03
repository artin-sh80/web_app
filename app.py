import requests
from bs4 import BeautifulSoup
import csv
import os
import logging
from datetime import datetime

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebScraper:
    def __init__(self, url, output_filename="scraped_data.csv"):
        self.url = url
        self.output_filename = output_filename
        self.headers = ['Title', 'Link', 'Date']
        self.data = []

    def fetch_page(self):
        """Fetch the HTML content of the webpage."""
        logging.info(f"Fetching the webpage: {self.url}")
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            logging.info("Page fetched successfully.")
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching the page: {e}")
            return None

    def parse_html(self, html_content):
        """Parse the HTML content and extract the data."""
        logging.info("Parsing HTML content...")
        soup = BeautifulSoup(html_content, 'html.parser')

        # Modify the selector based on the structure of the site you're scraping
        articles = soup.find_all('article')  # Example selector for blog posts
        for article in articles:
            try:
                title = article.find('h2').get_text(strip=True)
                link = article.find('a')['href']
                date = article.find('time')['datetime']
                self.data.append([title, link, date])
            except AttributeError as e:
                logging.warning(f"Missing expected data: {e}")

    def save_to_csv(self):
        """Save the scraped data into a CSV file."""
        logging.info(f"Saving data to {self.output_filename}")
        if not os.path.exists(self.output_filename):
            # Create CSV file and write the headers
            with open(self.output_filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                writer.writerows(self.data)
        else:
            # Append data if file already exists
            with open(self.output_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(self.data)

    def run(self):
        """Run the entire scraping process."""
        html_content = self.fetch_page()
        if html_content:
            self.parse_html(html_content)
            self.save_to_csv()
            logging.info("Scraping process completed successfully.")
        else:
            logging.error("Scraping process failed.")

# Example of usage
if __name__ == "__main__":
    # Example URL (change to the website you want to scrape)
    url_to_scrape = 'https://example.com/blog'
    scraper = WebScraper(url=url_to_scrape)

    # Start scraping
    scraper.run()
