def generate_report(informations, analysis):
    report = f"""
    Rapport d'Analyse des Informations:
    - Nombre total d'articles: {analysis['total_articles']}
    - Longueur moyenne des descriptions: {analysis['mean_description_length']}
    - Longueur médiane des descriptions: {analysis['median_description_length']}
    - Écart-type des longueurs de description: {analysis['std_description_length']}
    """
    
    # Ajouter des statistiques supplémentaires au rapport
    report += "\nArticles par mois:\n"
    for month, count in analysis['articles_per_month'].items():
        report += f"- {month}: {count} articles\n"
    
    report += "\nFréquence des mots-clés:\n"
    for keyword, count in analysis['keyword_frequency'].items():
        report += f"- {keyword}: {count} occurrences\n"
    
    return report

def send_alerts(informations):
    for info in informations:
        if 'alert' in info['description']:
            print(f"ALERT: {info['titre']} - {info['url']}")
