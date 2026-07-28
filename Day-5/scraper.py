import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_website_contents(url):

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all links BEFORE removing tags
        links = []

        for a in soup.find_all("a", href=True):
            full_url = urljoin(url, a["href"])

            links.append({
                "text": a.get_text(strip=True),
                "url": full_url
            })

        # Remove unwanted tags
        for tag in soup(["script", "style", "header", "footer",
                         "nav", "aside", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator="\n")

        clean_text = "\n".join(
            line.strip()
            for line in text.splitlines()
            if line.strip()
        )

        return {
            "text": clean_text,
            "links": links
        }

    except requests.exceptions.RequestException as e:
        return {
            "text": "",
            "links": [],
            "error": str(e)
        }