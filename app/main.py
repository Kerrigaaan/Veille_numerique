from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import mysql.connector
from app.scraping import scrape_informations
from app.data_processing import clean_informations
from app.data_transformation import transform_informations
from app.data_analysis import analyze_informations
from app.data_visualization import visualize_informations
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


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/informations")
def read_informations(request: Request):
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informations")
    informations = cursor.fetchall()
    print(f"Fetched {len(informations)} informations from the database")
    conn.close()
    return templates.TemplateResponse("informations.html", {"request": request, "informations": informations})


@app.get("/scrape")
def scrape_and_store():
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

    visualize_informations(informations)
    report = generate_report(informations, analysis)
    print(report)
    send_alerts(informations)

    return {"status": "success", "message": "Data scraped, cleaned, transformed, analyzed, and stored successfully"}


@app.get("/analyze")
def analyze_data(request: Request):
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informations")
    informations = cursor.fetchall()
    conn.close()

    analysis = analyze_informations(informations)
    return {"status": "success", "analysis": analysis}


@app.get("/visualize")
def visualize_data(request: Request):
    conn = get_db_connection()
    if conn is None:
        return {"status": "error", "message": "Failed to connect to database"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informations")
    informations = cursor.fetchall()
    conn.close()

    visualize_informations(informations)
    return {"status": "success", "message": "Data visualized successfully"}


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
