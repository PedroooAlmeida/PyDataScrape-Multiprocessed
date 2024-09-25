import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool, cpu_count # For option 2
import pandas as pd
import sys

# Here are the lines for adjusting the multiprocessing to your own device:

# OPTION 1: 

# This line creates a pool with 4 worker processes. These workers will run independently, each handling a portion of the scraping task.

with Pool(processes=4) as pool: # Manually adjust the number of processes here

 
# --------------------------------------------------------------------------------------------------------------------------------------
 
# OPTION 2: 

# Get the number of CPU cores and use that value in the Pool() function

available_cores = cpu_count()

num_processes = available_cores

with Pool(processes=num_processes) as pool:



