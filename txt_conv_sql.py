# Read the log data from a file
log_entries = []
with open("C:\\Users\\HP\\Desktop\\script file\\log_entries_all.txt", "r") as file:
    log_entries = file.read().strip().split("\n\n")

# Create SQL statements
sql_statements = []
for entry in log_entries:
    lines = entry.split("\n")
    timestamp = lines[0].split(": ", 1)[1]
    info_level = lines[1].split(": ", 1)[1]
    logger = lines[2].split(": ", 1)[1]
    message = lines[3].split(": ", 1)[1]

    sql_statement = (
        "INSERT INTO errors_log "
        "(TIMESTRAMP, INFO_LEVEL, LOGGER, MESSAGE) "
        "VALUES ('{}', '{}', '{}', '{}');"
    ).format(
        timestamp, info_level, logger, message.replace("'", "''")
    )
    sql_statements.append(sql_statement)

# Save SQL statements to a file
with open("C:\\Users\\HP\\Desktop\\generated_sql_statements.sql", "w") as sql_file:
    for sql_statement in sql_statements:
        sql_file.write(sql_statement + "\n")

print("SQL statements generated and saved to 'generated_sql_statements.sql' file.")
