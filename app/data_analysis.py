from collections import Counter
from datetime import datetime

def analyze_informations(informations):
    total_articles = len(informations)
    if total_articles == 0:
        return {
            'total_articles': total_articles,
            'mean_description_length': None,
            'median_description_length': None,
            'std_description_length': None,
            'articles_per_month': {},
            'keyword_frequency': {},
            'date_distribution': {}
        }
    
    description_lengths = [len(info['description']) for info in informations]
    mean_description_length = sum(description_lengths) / total_articles
    median_description_length = sorted(description_lengths)[total_articles // 2]
    std_description_length = (sum((x - mean_description_length) ** 2 for x in description_lengths) / total_articles) ** 0.5
    
    publication_dates = [info['date_publication'] for info in informations]
    date_distribution = Counter(publication_dates)
    articles_per_month = Counter(date.strftime('%Y-%m') for date in publication_dates)
    
    keywords = ["AI", "artificial intelligence", "machine learning", "deep learning", "neural network", "healthcare", "medicine", "medical", "clinical", "biomedical"]
    keyword_frequency = Counter()
    for info in informations:
        for keyword in keywords:
            if keyword.lower() in info['description'].lower():
                keyword_frequency[keyword] += 1
    
    return {
        'total_articles': total_articles,
        'mean_description_length': mean_description_length,
        'median_description_length': median_description_length,
        'std_description_length': std_description_length,
        'date_distribution': date_distribution,
        'articles_per_month': articles_per_month,
        'keyword_frequency': keyword_frequency
    }
