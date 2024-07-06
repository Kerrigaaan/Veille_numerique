import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

def scrape_informations():
    urls = [
        #"https://medicalxpress.com/news/2024-07-applications-ai-medicine.html",
        #"https://www.chiefhealthcareexecutive.com/view/health-technology-in-2024-projections-for-ai-digital-health-and-more",
        #"https://www.technologynetworks.com",
        #"https://med.stanford.edu",
        #"https://www.worldhealth.net",
        #"https://www.nature.com",
        #"https://www.jmir.org"
        "https: //eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    ]

    informations = []

    for url in urls:
        response = requests.get(url)
        print(f"Fetching {url}, status: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = soup.find_all('article')
            print(f"Found {len(articles)} articles")
            for article in articles:
                titre = article.find('h2').text if article.find('h2') else 'No title'
                description = article.find('p').text if article.find('p') else 'No description'
                link_tag = article.find('a')
                article_url = urljoin(url, link_tag['href']) if link_tag else url
                date_publication = datetime.now().date()

                informations.append({
                    'titre': titre,
                    'description': description,
                    'url': article_url,
                    'date_publication': date_publication
                })
        else:
            print(f"Failed to retrieve {url}")

    return filter_informations(informations)

def filter_informations(informations):
    # Filtrer les données non pertinentes ici
    return informations
