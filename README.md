This Python script is a web scraper that utilizes the multiprocessing library to speed up data collection by running multiple processes in parallel. 
It fetches HTML content from a list of URLs, parses the content using BeautifulSoup, and stores the scraped data into a CSV file for further analysis.

Features
- Multiprocessing: Uses the multiprocessing library to scrape multiple pages concurrently, reducing the total time needed to gather data.
- Efficient Parsing: Leverages BeautifulSoup and the lxml parser for fast and efficient HTML parsing.
- Data Storage: Outputs the scraped data into a CSV file for easy analysis using Pandas.
- Error Handling: Implements basic error handling to manage network issues and failed requests.

For Usage
- Clone repository and input your own URLs.
- Run script.
