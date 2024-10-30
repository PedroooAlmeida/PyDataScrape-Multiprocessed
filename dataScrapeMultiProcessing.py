import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import pandas as pd

def fetch_data(url):
    """
    Fetch HTML content from the given URL and parse it using BeautifulSoup.
    
    Args:
    url (str): URL of the webpage to scrape.
    
    Returns:
    dict: Extracted data from the webpage.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for failed requests
        
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')

        # Example: Extract specific information, e.g., title and some content
        title = soup.find('title').text.strip() if soup.find('title') else 'N/A'
        content = soup.find('p').text.strip() if soup.find('p') else 'N/A'

        # Return the data in a dictionary format
        return {'url': url, 'title': title, 'content': content}

    except requests.exceptions.RequestException as e:
        # Handle any exceptions (like network issues or timeouts)
        print(f"Error fetching {url}: {e}")
        return {'url': url, 'title': 'N/A', 'content': 'N/A'}

def scrape_urls(urls):
    """
    Scrape multiple URLs concurrently using multiprocessing.
    
    Args:
    urls (list): List of URLs to scrape.
    
    Returns:
    list: List of dictionaries containing scraped data.
    """
    # Use Pool to run multiple processes (the number of processes will depend on CPU cores)   
    # Adjust the 'processes' number according to your system, in this case our value is "4" 
    # OR use multiprocessing.cpu_count() to get the number of logical CPU cores on your system and set that as the number of processes.
    with Pool(processes=4) as pool:  
        results = pool.map(fetch_data, urls)  # Map the fetch_data function to the list of URLs
    return results

if __name__ == "__main__":
    # List of URLs to scrape (replace with actual URLs you want to scrape)
    urls = [
        'http://example.com/page1',
        'http://example.com/page2',
        'http://example.com/page3',
        'http://example.com/page4',
        'http://example.com/page5'
    ]

    # Start scraping the URLs using multiprocessing
    print("Starting web scraping...")
    scraped_data = scrape_urls(urls) 
    
    # Convert the results into a Pandas DataFrame
    df = pd.DataFrame(scraped_data)
    
    # Export the DataFrame to a CSV file, easier to read and manipulate with csv methods too
    df.to_csv('scraped_data.csv', index=False)

    # Print a success message and show the DataFrame summary
    print(f"Scraping completed. Data saved to 'scraped_data.csv'.")
    print(df.head())  # Display the first few rows of the scraped data
