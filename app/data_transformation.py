def transform_informations(informations):
    for info in informations:
        info['description_length'] = len(info['description'])
        # Ajoutez d'autres transformations ici
    return informations
