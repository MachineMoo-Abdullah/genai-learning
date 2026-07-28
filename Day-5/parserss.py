from scraper import fetch_website_contents
from utils import get_relevant_links


def fetch_page_and_all_relevant_links(url):
    print("Fetching landing page...")
    # Fetch landing page
    landing = fetch_website_contents(url)

    # Ask Gemini which links are useful
    selected = get_relevant_links(
        landing["text"],
        landing["links"]
    )

    document = landing["text"]

    # Visit selected pages
    for page in selected["links"]:

        page_data = fetch_website_contents(page["url"])

        document += "\n\n"
        document += f"===== {page['type']} =====\n"
        document += page_data["text"]
    print("All relevant pages fetched.")
    return document
