import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
import re

urls_to_scrape = [
    "https://medicalxpress.com/news/2024-07-applications-ai-medicine.html",
    "https://www.chiefhealthcareexecutive.com/view/health-technology-in-2024-projections-for-ai-digital-health-and-more",
    "https://www.technologynetworks.com",
    "https://med.stanford.edu",
    "https://www.worldhealth.net",
    "https://www.nature.com",
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/",
    "https://www.inserm.fr/dossier/intelligence-artificielle-et-sante/",
    "https://www.sciencedirect.com/science/article/abs/pii/S1385894724022393"
    "https://www.medaviz.com/8-utilisations-de-lia-en-medecine/"
]

keywords = [
    "AI", "artificial intelligence", "machine learning", "deep learning", "neural network",
    "healthcare", "medicine", "medical", "clinical", "biomedical", "health", "diagnosis",
    "treatment", "patient", "disease", "drug", "therapeutics", "hospital", "doctor", "nurse"
]


keywords_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b', re.IGNORECASE)

def scrape_informations():
    informations = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    session = requests.Session()
    session.headers.update(headers)

    for url in urls_to_scrape:
        response = session.get(url.strip())
        print(f"Fetching {url}, status: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            if "chiefhealthcareexecutive.com" in url:
                articles = extract_chiefhealthcareexecutive_articles(soup)
            else:
                articles = soup.find_all(['article', 'div'])


            print(f"Found {len(articles)} articles")
            for article in articles:
                titre = extract_title(article)
                description = extract_text(article)
                if not is_relevant(titre, description):
                    continue

                link_tag = article.find('a')
                article_url = urljoin(url, link_tag['href']) if link_tag and 'href' in link_tag.attrs else url

                date_publication = datetime.now().date()

                informations.append({
                    'titre': titre,
                    'description': description,
                    'url': article_url,
                    'date_publication': date_publication
                })
        else:
            print(f"Failed to retrieve {url}")
            print(f"Response content: {response.content}")

    return filter_informations(informations)

def extract_chiefhealthcareexecutive_articles(soup):
    main_content = soup.find('div', {'class': 'content-body'})
    if not main_content:
        return []
    articles = []
    for element in main_content.find_all(['h1', 'h2', 'h3', 'p', 'div']):
        parent = element.find_parent('div')
        if parent and parent not in articles:
            articles.append(parent)
    return articles

def extract_title(article):
    for tag in ['h1', 'h2', 'h3']:
        if article.find(tag):
            return article.find(tag).text
    return 'No title'

def extract_text(article):
    paragraphs = article.find_all(['p', 'span', 'div'])
    text = ' '.join(p.text for p in paragraphs)
    return text

def is_relevant(titre, description):
    combined_text = (titre + " " + description).lower()
    return bool(keywords_pattern.search(combined_text))

def filter_informations(informations):
    # Filtrer les données non pertinentes ici
    return informations

# Fonction de test
if __name__ == "__main__":
    infos = scrape_informations()
    for info in infos:
        print(info)