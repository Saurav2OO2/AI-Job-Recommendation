
from apify_client import ApifyClient
from dotenv import load_dotenv
import os
import logging

load_dotenv()

apify_client = ApifyClient(os.getenv('APIFY_API_TOKEN'))

def _fetch_apify_jobs(actor_id, search_query, location, rows):
    """Internal helper to fetch jobs from Apify Actors."""
    try:
        run_input = {
            'title': search_query,
            'location': location,
            'rows': rows,
            'proxy': {
                'useApifyProxy': True,
                "apifyProxyGroups": ["RESIDENTIAL"],
            },
        }
        run = apify_client.actor(actor_id).call(run_input=run_input)
        jobs = list(apify_client.dataset(run['defaultDatasetId']).iterate_items())
        return jobs
    except Exception as e:
        logging.error(f"Apify Fetch Error for actor {actor_id}: {e}")
        return []

# Fetch LinkedIn jobs based on the search_query
def fetch_linkedin_jobs(search_query, location='india', rows=60):
    """
    Fetches LinkedIn jobs using the Apify LinkedIn Jobs Scraper.
    """
    return _fetch_apify_jobs("BHzefUZlZRKWxkTck", search_query, location, rows)

# Fetch Naukri jobs based on the search_query
def fetch_naukri_jobs(search_query, location='india', rows=60):
    """
    Fetches Naukri jobs using the Apify Naukri Scraper.
    """
    return _fetch_apify_jobs("wsrn5gy5C4EDeYCcD", search_query, location, rows)