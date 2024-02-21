import re

# Chemin vers le fichier de journal
log_file_path = 'C:\\Users\\HP\\Desktop\\script file\\localhost_entries_all.log'
output_errors_file = 'C:\\Users\\HP\\Desktop\\script file\\localhost_errors.txt'  # Chemin du fichier de sortie pour les erreurs

# Modèle de regex pour extraire les informations
log_entry_pattern = re.compile(
    r'Adresse IP: (.*?)\n'
    r'Utilisateur: (.*?)\n'
    r'Date et Heure: (.*?)\n'
    r'Méthode de Requête: (.*?)\n'
    r'Chemin de la Ressource: (.*?)\n'
    r'Code de Statut: (\d+)\n'
    r'Taille de la Réponse: (\d+)\n'
    r'Temps de Traitement: (\d+)\n'
    r'Identifiant de Session: (.*?)\n'
    r'------------------------------'
)

# Fonction pour détecter les erreurs en fonction du code de statut
def detect_errors(status_code):
    if status_code >= 400:
        return True
    else:
        return False

# Ouvre le fichier de journal en lecture
with open(log_file_path, 'r') as log_file:
    log_entries = log_entry_pattern.findall(log_file.read())
    
    # Ouvre le fichier de sortie en écriture
    with open(output_errors_file, 'w') as errors_file:
        for entry in log_entries:
            ip, user, datetime, method, resource, status_code, response_size, processing_time, session_id = entry
            status_code = int(status_code)
            
            if detect_errors(status_code):
                error_message = (
                    f"Adresse IP: {ip}\n"
                    f"Utilisateur: {user}\n"
                    f"Date et Heure: {datetime}\n"
                    f"Méthode de Requête: {method}\n"
                    f"Chemin de la Ressource: {resource}\n"
                    f"Code de Statut: {status_code}\n"
                    f"Taille de la Réponse: {response_size}\n"
                    f"Temps de Traitement: {processing_time}\n"
                    f"Identifiant de Session: {session_id}\n"
                    f"------------------------------\n"
                )
                errors_file.write(error_message)
                print("Erreur détectée. Détails écrits dans le fichier erreurs.txt")
            else:
                print("Pas d'erreur détectée")
