import requests
from bs4 import BeautifulSoup
import json
import time
import random
from datetime import datetime, timezone
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

ARCHIVE_URL = "https://pastebin.com/archive"
RAW_URL_TEMPLATE = "https://pastebin.com/raw/{}"
OUTPUT_FILE = "keyword_matches.jsonl"
KEYWORDS = ["crypto", "bitcoin", "ethereum", "blockchain", "t.me"]
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Set up logging
logging.basicConfig(
    filename="pastebin_crawler.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_latest_paste_ids():
    try:
        response = requests.get(ARCHIVE_URL, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select("table tr td a")
        paste_ids = [link.get("href").strip("/") for link in links if link.get("href").startswith("/")]
        return paste_ids[:30]
    except Exception as e:
        logging.error(f"Failed to get paste IDs: {e}")
        return []

def fetch_paste_content(paste_id):
    url = RAW_URL_TEMPLATE.format(paste_id)
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        logging.info(f"Fetched paste ID {paste_id}")
        return response.text
    except Exception as e:
        logging.warning(f"Error fetching paste {paste_id}: {e}")
        return ""

def scan_paste(paste_id):
    time.sleep(random.uniform(1, 3))  # Rate limiting
    content = fetch_paste_content(paste_id)
    found_keywords = [kw for kw in KEYWORDS if kw.lower() in content.lower()]
    if found_keywords:
        match = {
            "source": "pastebin",
            "context": f"Found crypto-related content in Pastebin paste ID {paste_id}",
            "paste_id": paste_id,
            "url": RAW_URL_TEMPLATE.format(paste_id),
            "discovered_at": datetime.now(timezone.utc).isoformat(),
            "keywords_found": found_keywords,
            "status": "pending"
        }
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(match) + "\n")
        logging.info(f"Match found in paste {paste_id} with keywords: {found_keywords}")
    else:
        logging.info(f"No match found in paste {paste_id}")

def main():
    logging.info("Starting Pastebin Crawler with rate-limiting and multi-threading...")
    paste_ids = get_latest_paste_ids()
    if not paste_ids:
        logging.warning("No paste IDs found.")
        return

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(scan_paste, pid) for pid in paste_ids]
        for future in as_completed(futures):
            pass  # Wait for all to finish

    logging.info("Done checking all pastes.")

if __name__ == "__main__":
    main()
