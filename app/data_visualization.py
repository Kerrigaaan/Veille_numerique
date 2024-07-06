import matplotlib.pyplot as plt

def visualize_informations(informations):
    descriptions = [info['description_length'] for info in informations]

    plt.hist(descriptions, bins=20, color='blue', alpha=0.7)
    plt.title('Distribution of Description Lengths')
    plt.xlabel('Length')
    plt.ylabel('Frequency')
    plt.show()

