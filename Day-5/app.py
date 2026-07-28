import os

from parserss import fetch_page_and_all_relevant_links

from brochure import generate_brochure

url = input("Website URL: ")

document = fetch_page_and_all_relevant_links(url)

brochure = generate_brochure(document)

os.makedirs("outputs", exist_ok=True)

with open("outputs/brochure.md", "w", encoding="utf-8") as f:
    f.write(brochure)

print("Brochure saved to outputs/brochuree.md")