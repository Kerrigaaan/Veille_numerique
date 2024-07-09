from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import mysql.connector
from app.scraping import scrape_informations, urls_to_scrape
from app.data_processing import clean_informations
from app.data_transformation import transform_informations
from app.data_analysis import analyze_informations
from app.data_visualization import visualize_informations, create_bar_chart, create_date_distribution_chart, create_keyword_frequency_chart
from app.modeling import cluster_informations
from app.reporting import generate_report, send_alerts
from app.monitoring import monitor_sources
from app.evaluation import collect_feedback, audit_data

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configuration de la base de données
db_config = {
    'user': 'root',
    'password': '',  # Remplacez par votre mot de passe MySQL
    'host': 'localhost',
    'database': 'veille_ia_medecine'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def truncate_text(text, max_length=200):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "urls_to_scrape": urls_to_scrape})

@app.post("/add_url")
def add_url(request: Request, url: str = Form(...)):
    urls_to_scrape.append(url)
    return templates.TemplateResponse("index.html", {"request": request, "urls_to_scrape": urls_to_scrape, "message": "URL ajoutée avec succès!"})

@app.get("/informations")
def read_informations(request: Request):
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informations")
    informations = cursor.fetchall()
    for info in informations:
        info['description'] = truncate_text(info['description'])
    print(f"Fetched {len(informations)} informations from the database")
    conn.close()
    return templates.TemplateResponse("informations.html", {"request": request, "informations": informations})

@app.get("/scrape")
def scrape_and_store(request: Request):
    if not urls_to_scrape:
        return templates.TemplateResponse("scrape.html", {"request": request, "message": "Aucune URL à scraper. Veuillez ajouter des URL."})

    informations = scrape_informations()
    informations = clean_informations(informations)
    informations = transform_informations(informations)
    analysis = analyze_informations(informations)
    informations = cluster_informations(informations)
    
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor()
    for info in informations:
        print(f"Inserting: {info}")
        cursor.execute("INSERT INTO informations (titre, description, url, date_publication) VALUES (%s, %s, %s, %s)", 
                       (info['titre'], info['description'], info['url'], info['date_publication']))
    conn.commit()
    conn.close()
    
    image_base64 = visualize_informations(informations)
    bar_chart_base64 = create_bar_chart(informations)
    date_distribution_chart_base64 = create_date_distribution_chart(analysis['date_distribution'])
    keyword_frequency_chart_base64 = create_keyword_frequency_chart(analysis['keyword_frequency'])
    report = generate_report(informations, analysis)
    print(report)
    send_alerts(informations)
    
    return templates.TemplateResponse("scrape.html", {"request": request, "image_base64": image_base64, "bar_chart_base64": bar_chart_base64, "date_distribution_chart_base64": date_distribution_chart_base64, "keyword_frequency_chart_base64": keyword_frequency_chart_base64, "report": report})

@app.get("/analyze")
def analyze_data(request: Request):
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informations")
    informations = cursor.fetchall()
    conn.close()
    
    informations = transform_informations(informations)
    analysis = analyze_informations(informations)
    return templates.TemplateResponse("analyze.html", {"request": request, "analysis": analysis})

@app.get("/visualize")
def visualize_data(request: Request):
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informations")
    informations = cursor.fetchall()
    conn.close()

    if not informations:
        return templates.TemplateResponse("visualize.html", {"request": request, "has_data": False})
    
    informations = transform_informations(informations)
    
    image_base64 = visualize_informations(informations)
    bar_chart_base64 = create_bar_chart(informations)
    analysis = analyze_informations(informations)
    date_distribution_chart_base64 = create_date_distribution_chart(analysis['date_distribution'])
    keyword_frequency_chart_base64 = create_keyword_frequency_chart(analysis['keyword_frequency'])
    return templates.TemplateResponse("visualize.html", {"request": request, "has_data": True, "image_base64": image_base64, "bar_chart_base64": bar_chart_base64, "date_distribution_chart_base64": date_distribution_chart_base64, "keyword_frequency_chart_base64": keyword_frequency_chart_base64})

@app.get("/audit")
def audit(request: Request):
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informations")
    informations = cursor.fetchall()
    conn.close()
    
    audit_results = audit_data(informations)
    return templates.TemplateResponse("audit.html", {"request": request, "audit_results": audit_results})

@app.get("/test-db-connection")
def test_db_connection():
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}
    
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    conn.close()
    return {"status": "success", "message": f"Connected to database. Tables: {tables}"}
