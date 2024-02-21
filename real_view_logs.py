import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

# Charger les données à partir du fichier JSON
with open('C:\\Users\\HP\Desktop\\script file\\server.json', 'r') as f:
    data = json.load(f)

# Trier les événements par timestamp
data.sort(key=lambda x: x['timestamp'])

# Créer des listes vides pour stocker les données
timestamps = []
message_types = []
message_counts = defaultdict(int)
error_messages = defaultdict(list)  # Stocker les messages d'erreur avec leurs timestamps

# Limite pour afficher uniquement les derniers événements
limit = 10  # Ajustez selon vos préférences

# Configurations pour l'envoi d'e-mails
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = '' //smtp username//
smtp_password = 'smtp_password'
sender_email = '' //sender email//
receiver_email = '' //receiver email//

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
        message_counts[message_type] += 1

        # Limiter le nombre d'événements affichés
        if len(timestamps) > limit:
            timestamps.pop(0)
            message = message_types.pop(0)
            message_counts[message] -= 1

        # Vérifier si une erreur se répète
        if message_counts[message_type] > 1:
            error_messages[message_type].append(timestamp)

            # Envoyer un e-mail en cas de répétition d'erreur
            send_email(message_type, timestamp)

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

# Fonction pour envoyer un e-mail en cas de répétition d'erreur
def send_email(error_type, timestamp):
    subject = f"Répétition d'erreur : {error_type}"
    error_messages_str = "\n".join([f"{ts} - {error_type}" for ts in error_messages[error_type]])

    body = f"L'erreur de type '{error_type}' se répète plus d'une fois. Détails : Timestamp - {timestamp}\n\nMessages d'erreur précédents :\n{error_messages_str}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

# Lancer l'animation en temps réel
ani = FuncAnimation(plt.gcf(), update_chart, frames=len(data), interval=1000)
plt.show()
