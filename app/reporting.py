def generate_report(informations, analysis):
    report = f"""
    Rapport d'Analyse des Informations:
    - Nombre total d'articles: {len(informations)}
    - Longueur moyenne des descriptions: {analysis['mean_description_length']}
    - Longueur médiane des descriptions: {analysis['median_description_length']}
    - Écart-type des longueurs de description: {analysis['std_description_length']}
    """
    return report

def send_alerts(informations):
    for info in informations:
        if 'alert' in info['description']:
            print(f"ALERT: {info['titre']} - {info['url']}")
