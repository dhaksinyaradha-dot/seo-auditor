from flask import Flask, render_template, request,send_file
import pandas as pd
import os

from crawler import crawl_website
from checker import check_seo


app = Flask(__name__)
latest_results=[]


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/audit", methods=["POST"])
def audit():

    website = request.form.get("url")

    if not website:

        return "Please enter a website URL."

    try:

        # Crawl the website
        crawl_results = crawl_website(website)

        # Run SEO checks
        seo_report = check_seo(crawl_results)
        global latest_results
        latest_results = crawl_results

        return render_template(

            "results.html",

            website=website,

            pages_crawled=seo_report["pages_crawled"],

            seo_score=seo_report["seo_score"],

            missing_titles=seo_report["missing_titles"],

            missing_meta=seo_report["missing_meta"],

            missing_h1=seo_report["missing_h1"],

            duplicate_titles=seo_report["duplicate_titles"],

            broken_links=seo_report["broken_links"],

            crawl_results=crawl_results
                    )

    except Exception as e:

        return f"""
        <h2>Error</h2>

        <p>{e}</p>

        <a href="/">Go Back</a>
        """
@app.route("/export")
def export_csv():

    global latest_results

    if not latest_results:

        return "No audit available."

    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(latest_results)

    csv_path = "data/report.csv"

    df.to_csv(csv_path, index=False)

    return send_file(
        csv_path,
        as_attachment=True
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)

    