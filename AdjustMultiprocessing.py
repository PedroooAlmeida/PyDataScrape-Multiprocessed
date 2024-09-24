# git clone https://github.com/yourusername/your-repository-name.git
# cd your-repository-name

# Here's the line for adjusting the multiprocessing to your own device

with Pool(processes=4) as pool: # Adjust the number of processes here

# This line creates a pool with 4 worker processes. These workers will run independently, each handling a portion of the scraping task.

results = pool.map(fetch_data, urls)

# The map() function distributes the urls list across the 4 worker processes, assigning each URL to one of the workers. 
# Each worker runs the fetch_data() function on its assigned URL. 
 #Once all URLs are processed, map() collects and returns the results from all workers.
