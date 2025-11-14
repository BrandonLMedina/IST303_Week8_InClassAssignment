# Concurrency example using multiple implementations
# Example searches for a topic on wikipedia, gets related topics and 
#   saves the references from related topics in their own text file
# info on wikipedia library: https://thepythoncode.com/article/access-wikipedia-python
# info on concurrent.futures library: https://docs.python.org/3/library/concurrent.futures.html#

import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# convert objects produced by wikipedia package to a string var for saving to text file
def convert_to_str(obj):
    if type(obj) == list:
        mystr = '\n'.join(obj)
        return mystr
    elif type(obj) in [str, int, float]:
        return str(obj)

# NEW: single shared download/save function (removes duplicate logic)
def dl_and_save(item):
    page = wikipedia.page(item, auto_suggest=False)
    title = page.title
    references = convert_to_str(page.references)
    out_filename = title + ".txt"
    print(f'writing to {out_filename}')
    with open(out_filename, 'w') as fileobj:
        fileobj.write(references)

# NEW: function to get user input with default behavior
def get_search_term():
    default_term = "generative artificial intelligence"
    user_input = input(
        f"Enter a Wikipedia search term (min 4 characters, or press Enter for default '{default_term}'): "
    ).strip()

    if len(user_input) < 4:
        print(f"Search term too short. Using default: '{default_term}'")
        return default_term
    return user_input

# IMPLEMENTATION 1: sequential example
def wiki_sequentially(results):
    print('\nsequential function:')
    t_start = time.perf_counter()

    for item in results:
        dl_and_save(item)

    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'code executed in {t_lapse} seconds')

# IMPLEMENTATION 2: concurrent example w/ threads
def concurrent_threads(results):
    print('\nthread pool function:')
    t_start = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        executor.map(dl_and_save, results)

    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'code executed in {t_lapse} seconds')

# IMPLEMENTATION 3: concurrent example w/ processes
# processes do not share memory; multiprocessing and concurrent.futures.ProcessPoolExecutor pickle
# objects in order to communicate - functions must be at module level (dl_and_save already is)
def concurrent_process(results):
    print('\nprocess pool function:')
    t_start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save, results)

    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'code executed in {t_lapse} seconds')

if __name__ == "__main__":
    # get user input search term (with default if < 4 chars)
    search_term = get_search_term()

    # do the search once and reuse results for all implementations
    results = wikipedia.search(search_term)

    wiki_sequentially(results)
    concurrent_threads(results)
    concurrent_process(results)