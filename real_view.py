import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Charger les données à partir du fichier JSON
with open('C:\\Users\\HP\\Desktop\\server.json', 'r') as f:
    data = json.load(f)

# Trier les événements par timestamp
data.sort(key=lambda x: x['timestamp'])

# Créer des listes vides pour stocker les données
timestamps = []
message_types = []

# Limite pour afficher uniquement les derniers événements
limit = 10  # Ajustez selon vos préférences

# Créer le graphique avec une taille fixe
plt.figure(figsize=(10, 4))  # Ajuster la taille selon vos préférences
plt.xlabel('Timestamp')
plt.ylabel('Event Type')
plt.title('Visualisation des logs en temps réel')

# Fonction de mise à jour en temps réel
def update_chart(frame):
    if frame < len(data):
        event = data[frame]
        timestamp = event['timestamp']
        message_type = event['message']

        # Mettre à jour les données
        timestamps.append(timestamp)
        message_types.append(message_type)

        # Limiter le nombre d'événements affichés
        if len(timestamps) > limit:
            timestamps.pop(0)
            message_types.pop(0)

        # Effacer le graphique actuel
        plt.clf()
        plt.bar(timestamps, message_types)  # Utiliser plt.bar() pour des barres verticales

        # Personnaliser l'apparence du graphique
        plt.xlabel('Timestamp')
        plt.ylabel('Event Type')
        plt.title('Visualisation en temps réel du fichier centralisé server.log')
        plt.gca().invert_yaxis()  # Inverser l'axe vertical pour afficher les événements les plus récents en haut

        # Rotation des labels sur l'axe des timestamps pour un meilleur affichage
        plt.xticks(rotation=45, fontsize=8)  # Réduire la taille de la police

        # Définir les limites de l'axe des x pour rester statique
        plt.xlim(timestamps[0], timestamps[-1])

        # Ajuster la disposition du graphique selon les paramètres spécifiés
        plt.subplots_adjust(top=0.953, bottom=0.3, left=0.455, right=0.99, hspace=0.2, wspace=0.2)

# Lancer l'animation en temps réel
ani = FuncAnimation(plt.gcf(), update_chart, frames=len(data), interval=1000)
plt.show()
