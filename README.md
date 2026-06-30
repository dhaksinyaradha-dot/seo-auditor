# SEO Website Auditor

A Flask-based SEO Website Auditor that crawls websites, analyzes important on-page SEO factors, and generates an audit report with CSV export.

---

## 📌 Features

- Crawl internal website pages
- Extract page titles
- Extract meta descriptions
- Detect missing page titles
- Detect missing meta descriptions
- Detect missing H1 tags
- Detect duplicate page titles
- Detect broken links (404)
- Generate SEO score
- Export audit report as CSV
- Generate sitemap.xml
- Responsive Bootstrap dashboard

---

## 🛠 Technologies Used

- Python 3
- Flask
- BeautifulSoup4
- Requests
- Pandas
- Bootstrap 5
- HTML
- CSS
- Jinja2

---

## 📂 Project Structure

```
seo-auditor/
│
├── app.py
├── crawler.py
├── checker.py
├── sitemap.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   ├── css/
│   └── js/
│
└── data/
    ├── report.csv
    ├── sitemap.xml
    └── results.json
```

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/seo-auditor.git
```

### 2. Open the project

```bash
cd seo-auditor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```
http://127.0.0.1:5000
```

---

## 🚀 How It Works

1. Enter a website URL.
2. Flask receives the URL.
3. The crawler downloads the website.
4. BeautifulSoup extracts SEO information.
5. The checker analyzes SEO issues.
6. Results are displayed on a Bootstrap dashboard.
7. The report can be downloaded as a CSV file.

---

## 📊 SEO Checks Performed

- ✅ Page Title
- ✅ Meta Description
- ✅ H1 Tag
- ✅ Duplicate Titles
- ✅ Broken Links
- ✅ Internal Links
- ✅ Sitemap Generation

---

## 📁 Output Files

The project generates:

- `data/report.csv`
- `data/sitemap.xml`
- `data/results.json`

---

## 🔮 Future Improvements

- JavaScript website crawling
- Robots.txt parser
- Canonical tag validation
- Open Graph tag analysis
- Image ALT text analysis
- PageSpeed Insights integration
- Core Web Vitals support
- Mobile-friendly analysis
- PDF report export
- User authentication

---

## 👨‍💻 Author

**Dhaksinya**

Computer Science Engineering Student

---

## 📄 License

This project is developed for educational and portfolio purposes.