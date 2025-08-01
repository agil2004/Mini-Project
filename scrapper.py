import os
import requests
from bs4 import BeautifulSoup

# Read TARGET_URL from environment
target_url = os.getenv("TARGET_URL", "https://news.ycombinator.com")

try:
    response = requests.get(target_url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    soup = BeautifulSoup(response.text, "html.parser")

    # Find h1 and h2 tags
    headings = soup.find_all(["h1", "h2"])

    print(f"\nScraping: {target_url}\n")
    for i, title in enumerate(headings, 1):
        print(f"{i}. {title.get_text(strip=True)}")

except Exception as e:
    print(f"Error fetching or parsing the URL: {e}")
