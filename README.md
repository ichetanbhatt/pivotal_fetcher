# pivotal_fetcher
Very simple and extendable pypi script that can be used to perform desired fetching.
Currently fetches the list of accepted stories.
# Usage:
1. Install via pip. `pip install pivotal_fetcher`
2. Create a file ".pt_config" in your root:

```py
PT_APIKEY=YOUR_API_TOKEN
PROJECT_ID={"PROJECT_NAME": PROJECT_ID}
OWNER_ID=USER_NAME
   ```
3. Use "pt_fetch [days]" for magic!

  
