import plotly.graph_objects as go
import pandas as pd

# Chemin vers le fichier de logs
log_file_path = "C:\\Users\HP\Desktop\script file\\log_entries_all.txt"

# Lire le fichier de logs et stocker les messages dans une liste
with open(log_file_path, "r") as log_file:
    log_lines = log_file.readlines()

messages = [line.split("Message:", 1)[1].strip() for line in log_lines if "Message:" in line]

# Compter les occurrences des messages
message_counts = pd.Series(messages).value_counts()

# Créer un DataFrame
df = pd.DataFrame({'Message': message_counts.index, 'Occurrences': message_counts.values})

# Utiliser une représentation en barres empilées avec Plotly
fig = go.Figure(data=[go.Bar(x=df['Message'], y=df['Occurrences'], text=df['Occurrences'], textposition='auto')])

# Personnaliser le graphique
fig.update_layout(title='Répartition des Occurrences des Messages d\'Erreur',
                  xaxis_title='Message',
                  yaxis_title='Occurrences')

# Afficher le graphique
fig.show()
