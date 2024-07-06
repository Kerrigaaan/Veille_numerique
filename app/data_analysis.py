import numpy as np

def analyze_informations(informations):
    descriptions = [info['description_length'] for info in informations]
    mean_length = np.mean(descriptions)
    median_length = np.median(descriptions)
    std_length = np.std(descriptions)

    analysis = {
        'mean_description_length': mean_length,
        'median_description_length': median_length,
        'std_description_length': std_length
    }

    return analysis
