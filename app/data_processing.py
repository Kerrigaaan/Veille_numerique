from datetime import datetime

def clean_informations(informations):
    cleaned_informations = []
    seen_titles = set()

    for info in informations:
        if info['titre'] not in seen_titles:
            seen_titles.add(info['titre'])
            info['description'] = correct_errors(info['description'])
            info['date_publication'] = normalize_date(info['date_publication'])
            cleaned_informations.append(info)

    return cleaned_informations

def correct_errors(text):
    # Correction des fautes de frappe et des incohérences
    corrected_text = text.replace("l'IA", "l’intelligence artificielle")
    # Ajoutez d'autres corrections si nécessaire
    return corrected_text

def normalize_date(date):
    # Uniformisation des formats de date
    if isinstance(date, str):
        normalized_date = datetime.strptime(date, "%Y-%m-%d").date()
    else:
        normalized_date = date
    return normalized_date

