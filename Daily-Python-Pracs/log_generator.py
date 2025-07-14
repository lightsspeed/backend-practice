import random
import datetime

# List of possible log levels and messages
log_levels = ["INFO", "ERROR", "WARNING"]
info_messages = ["System initialized", "User authenticated", "Backup completed", "Service restarted"]
error_messages = ["File not found", "Network Timeout", "Database error"]
warning_messages = ["Disk space low", "High CPU usage", "Memory threshold exceeded"]

# Generate random logs
num_logs = 300
with open("sample_logs.txt", "w") as file:
    for _ in range(num_logs):
        # Random date in 2025
        start_date = datetime.datetime(2025, 1, 1)
        random_days = random.randint(0, 364)  # 2025 is not a leap year
        log_date = start_date + datetime.timedelta(days=random_days)
        
        # Random time
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        # Create a new datetime with random time
        log_datetime = log_date.replace(hour=hour, minute=minute, second=second)
        
        # Random log level
        level = random.choice(log_levels)
        
        # Select message based on level
        if level == "INFO":
            message = random.choice(info_messages)
        elif level == "ERROR":
            message = random.choice(error_messages)
        else:  # WARNING
            message = random.choice(warning_messages)
        
        # Format log entry with date and time combined
        log_entry = f"{log_datetime.strftime('%Y-%m-%d %H:%M:%S')} {level} {' '.join([message])}\n"
        file.write(log_entry)

print("Log file 'sample_logs.txt' has been generated.")