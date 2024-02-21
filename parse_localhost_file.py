import re

def parse_log_line(log_line):
    log_pattern = r'(?P<ip>[\d\.]+) - "(?P<user>[^"]+)" \[(?P<timestamp>[^\]]+)\] "(?P<method>\w+) (?P<path>[^"]+) HTTP/\d+\.\d+" (?P<status>\d+) (?P<size>\d+) (?P<time>\d+) (?P<session>[^\s]+)'
    match = re.match(log_pattern, log_line)
    if match:
        log_data = match.groupdict()
        return log_data
    return None

# Lire le fichier d'entrée
input_file_path = 'C:\\Users\\HP\\Desktop\\script file\\localhost_access_log.2023-08-17.log'
output_file_path = 'C:\\Users\\HP\\Desktop\\script file\\localhost_entries_all.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        log_data = parse_log_line(line)
        if log_data:
            output_file.write("Adresse IP: {}\n".format(log_data['ip']))
            output_file.write("Utilisateur: {}\n".format(log_data['user']))
            output_file.write("Date et Heure: {}\n".format(log_data['timestamp']))
            output_file.write("Méthode de Requête: {}\n".format(log_data['method']))
            output_file.write("Chemin de la Ressource: {}\n".format(log_data['path']))
            output_file.write("Code de Statut: {}\n".format(log_data['status']))
            output_file.write("Taille de la Réponse: {}\n".format(log_data['size']))
            output_file.write("Temps de Traitement: {}\n".format(log_data['time']))
            output_file.write("Identifiant de Session: {}\n".format(log_data['session']))
            output_file.write("-" * 30 + "\n")  # Ligne de séparation entre les entrées
