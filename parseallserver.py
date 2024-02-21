import re

# Chemin vers le fichier de journal
log_file_path = 'C:\\Users\\HP\\Desktop\\server.log'
output_sql_file = 'insert_queries.sql'  # Chemin du fichier SQL de sortie

# Modèles de regex pour diverses lignes de journal
log_line_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w+)  \[(.*?)\] (.*)$')
log_line_pattern_with_arrow = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w+)  \[(.*?)\] (.*) => (.*)$')
additional_log_line_pattern_1 = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w+) \[(.*?)\] \[(.*?)\]: token =([\w-]+), Erreur= (.*)$')
additional_log_line_pattern_2 = re.compile(r'^(\w+ \d{2}, \d{4} \d{2}:\d{2}:\d{2} (?:AM|PM)) (\w+) \[(.*?)\] (.*)$')
additional_log_line_pattern_3 = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w+) \[(.*?)\] (.*)$')
additional_log_line_pattern_4 = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w+) \[STDERR\] (.*)$')

# Liste pour stocker les requêtes SQL générées
sql_queries = []

# Ouvre le fichier de journal en lecture
with open(log_file_path, 'r') as log_file:
    lines = log_file.readlines()

    for line in lines:
        if (match := log_line_pattern.match(line)) or (match := log_line_pattern_with_arrow.match(line)) or \
           (match := additional_log_line_pattern_1.match(line)) or (match := additional_log_line_pattern_2.match(line)) or \
           (match := additional_log_line_pattern_3.match(line)) or (match := additional_log_line_pattern_4.match(line)):
            
            groups = match.groups()
            timestamp, log_level, _, component, method_or_message = groups[0], groups[1], groups[2], groups[3], groups[-1]
            
            # Exemple de construction de requête SQL d'insertion
            sql_query = f"INSERT INTO logs (timestamp, log_level, component, method_or_message) VALUES ('{timestamp}', '{log_level}', '{component}', '{method_or_message}');"
            sql_queries.append(sql_query)

# Construit une seule chaîne contenant toutes les requêtes SQL
all_sql_queries = '\n'.join(sql_queries)

# Écrit toutes les requêtes SQL dans le fichier SQL de sortie
with open(output_sql_file, 'w') as sql_file:
    sql_file.write(all_sql_queries)

print("Extraction et génération de requêtes SQL terminées. Les requêtes ont été écrites dans le fichier", output_sql_file)
