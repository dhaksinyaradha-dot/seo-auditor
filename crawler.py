import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def crawl_website(url):

    parsed_url = urlparse(url)
    base_domain = parsed_url.netloc

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    internal_links = set()

    for link in soup.find_all("a"):

        href = link.get("href")

        if not href:
            continue

        if href.startswith("mailto:"):
            continue

        if href.startswith("javascript:"):
            continue

        if href.startswith("#"):
            continue

        if href.startswith("/") or base_domain in href:

            full_url = urljoin(url, href)

            internal_links.add(full_url)

    results = []

    visited_urls = set()

    max_pages = 20

    for page_url in list(internal_links)[:max_pages]:

        if page_url in visited_urls:
            continue

        visited_urls.add(page_url)

        try:

            page_response = requests.get(page_url)

            page_soup = BeautifulSoup(
                page_response.text,
                "html.parser"
            )

            title = (
                page_soup.title.text.strip()
                if page_soup.title
                else "No title"
            )

            meta_tag = page_soup.find(
                "meta",
                attrs={"name": "description"}
            )

            if meta_tag and meta_tag.get("content"):
                meta_description = meta_tag.get("content")
            else:
                meta_description = "No meta description"

            h1_tag = page_soup.find("h1")

            if h1_tag:
                h1_text = h1_tag.text.strip()
            else:
                h1_text = "No H1"

            results.append({

                "url": page_url,

                "title": title,

                "meta_description": meta_description,

                "h1": h1_text

            })

        except Exception:

            continue

    return results