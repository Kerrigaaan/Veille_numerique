import matplotlib.pyplot as plt
import io
import base64

# Couleurs spécifiques pour l'application
IA_COLOR = '#1E90FF'  
OTHER_COLOR = '#EEC4C9'

def visualize_informations(informations):
    labels = ['AI en médecine', 'Autres']
    ai_count = sum(1 for info in informations if 'ai' in info['description'].lower())
    other_count = len(informations) - ai_count
    sizes = [ai_count, other_count]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=[IA_COLOR, OTHER_COLOR])
    ax.axis('equal') 

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    image_base64 = base64.b64encode(img.read()).decode('utf-8')
    plt.close()

    return image_base64

def create_bar_chart(informations):
    categories = ['AI en médecine', 'Autres']
    counts = [sum(1 for info in informations if 'ai' in info['description'].lower()), 
              sum(1 for info in informations if 'ai' not in info['description'].lower())]

    fig, ax = plt.subplots()
    ax.bar(categories, counts, color=[IA_COLOR, OTHER_COLOR])
    ax.set_ylabel('Nombre d\'articles')
    ax.set_title('Répartition des articles sur l\'IA en médecine')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    image_base64 = base64.b64encode(img.read()).decode('utf-8')
    plt.close()

    return image_base64

def create_date_distribution_chart(date_distribution):
    dates = list(date_distribution.keys())
    counts = list(date_distribution.values())

    fig, ax = plt.subplots()
    ax.bar(dates, counts, color=IA_COLOR)
    ax.set_ylabel('Nombre d\'articles')
    ax.set_title('Distribution des dates de publication')
    plt.xticks(rotation=45)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    image_base64 = base64.b64encode(img.read()).decode('utf-8')
    plt.close()

    return image_base64

def create_keyword_frequency_chart(keyword_frequency):
    keywords = list(keyword_frequency.keys())
    counts = list(keyword_frequency.values())

    fig, ax = plt.subplots()
    ax.barh(keywords, counts, color=IA_COLOR)
    ax.set_xlabel('Fréquence')
    ax.set_title('Fréquence des mots-clés dans les descriptions')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    image_base64 = base64.b64encode(img.read()).decode('utf-8')
    plt.close()

    return image_base64
