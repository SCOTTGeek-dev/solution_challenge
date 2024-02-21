import re
import json

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

# Write error log entries to a JSON file
with open('C:\\Users\\HP\\Desktop\\central_log_errors.txt', 'w') as json_file:
    json.dump(error_log_entries, json_file, indent=4)
