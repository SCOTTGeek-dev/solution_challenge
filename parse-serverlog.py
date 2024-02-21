import re

log_line_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (ERROR)  \[(.*?)\] (.*)$')
log_line_pattern_with_arrow = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (ERROR)  \[(.*?)\] (.*) => (.*)$')
additional_log_line_pattern_1 = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (ERROR) \[(.*?)\] \[(.*?)\]: token =([\w-]+), Erreur= (.*)$')
additional_log_line_pattern_2 = re.compile(r'^(\w+ \d{2}, \d{4} \d{2}:\d{2}:\d{2} (?:AM|PM)) (ERROR) \[(.*?)\] (.*)$')
additional_log_line_pattern_3 = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (ERROR) \[(.*?)\] (.*)$')
additional_log_line_pattern_4 = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (ERROR) \[STDERR\] (.*)$')

error_log_entries = []

# Read the log file
with open('C:\\Users\\HP\\Desktop\\server.log', 'r') as log_file:
    for line in log_file:
        match = log_line_pattern_with_arrow.match(line)
        if not match:
            match = log_line_pattern.match(line)
        if not match:
            match = additional_log_line_pattern_1.match(line)
        if not match:
            match = additional_log_line_pattern_2.match(line)
        if not match:
            match = additional_log_line_pattern_3.match(line)
        if not match:
            match = additional_log_line_pattern_4.match(line)
        if match:
            timestamp, info_level, logger, message, *details = match.groups()
            details = ' '.join(details) if details else None

            error_log_entry = {
                "timestamp": timestamp,
                "info_level": info_level,
                "logger": logger,
                "message": message,
                "details": details
            }

            error_log_entries.append(error_log_entry)

# Write error log entries to a text file
with open('C:\\Users\\HP\\Desktop\\server.json', 'w') as txt_file:
    for entry in error_log_entries:
        txt_file.write(f"Timestamp: {entry['timestamp']}\n")
        txt_file.write(f"Info Level: {entry['info_level']}\n")
        txt_file.write(f"Logger: {entry['logger']}\n")
        txt_file.write(f"Message: {entry['message']}\n")
        if entry['details']:
            txt_file.write(f"Details: {entry['details']}\n")
        txt_file.write("\n")
