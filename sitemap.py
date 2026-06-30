import json

with open("data/results.json", "r", encoding="utf-8") as file:
    results = json.load(file)

print(results)
sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
sitemap += "<urlset>\n"
for page in results:
    sitemap += "    <url>\n"
    sitemap += f"        <loc>{page['url']}</loc>\n"
    sitemap += "    </url>\n"
sitemap += "</urlset>"

with open("data/sitemap.xml","w",encoding="utf-8") as file:
    file.write(sitemap)

print("Sitemap saved to data/sitemap.xml")