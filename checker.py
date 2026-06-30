import requests


def check_seo(results):

    report = {
        "pages_crawled": len(results),
        "missing_titles": [],
        "missing_meta": [],
        "missing_h1": [],
        "duplicate_titles": [],
        "broken_links": [],
        "seo_score": 100
    }

    title_count = {}

    for page in results:

        # Missing Title
        if page["title"] == "No title":
            report["missing_titles"].append(page["url"])

        # Missing Meta
        if page["meta_description"] == "No meta description":
            report["missing_meta"].append(page["url"])

        # Missing H1
        if page["h1"] == "No H1":
            report["missing_h1"].append(page["url"])

        # Count duplicate titles
        title = page["title"]

        if title in title_count:
            title_count[title] += 1
        else:
            title_count[title] = 1

        # Broken links
        try:

            response = requests.get(page["url"], timeout=5)

            if response.status_code == 404:
                report["broken_links"].append(page["url"])

        except Exception:
            report["broken_links"].append(page["url"])

    # Duplicate titles
    for title, count in title_count.items():

        if count > 1:
            report["duplicate_titles"].append({
                "title": title,
                "count": count
            })

    # SEO Score

    score = 100

    score -= len(report["missing_titles"]) * 5

    score -= len(report["missing_meta"]) * 5

    score -= len(report["missing_h1"]) * 5

    score -= len(report["duplicate_titles"]) * 3

    score -= len(report["broken_links"]) * 10

    if score < 0:
        score = 0

    report["seo_score"] = score

    return report