def analyze_logs(log_file_path):
    
    # Initialize dictionary to count log levels
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0}
    
    # List to store ERROR messages
    error_messages = []
    
    try:
        # Open and read the log file
        with open(log_file_path, 'r') as file:
            for line in file:
                # Strip whitespace and split the line into components
                parts = line.strip().split()
                if len(parts) >= 2:  # Ensure line has at least timestamp and level
                    log_level = parts[1]  # Second element is the log level
                    # Update count if log level is valid
                    if log_level in log_counts:
                        log_counts[log_level] += 1
                    # Collect ERROR messages
                    if log_level == "ERROR":
                        error_messages.append(" ".join(parts[2:]))  # Join message parts
        
        # Find the most frequent log level
        most_frequent = max(log_counts, key=log_counts.get)
        
        # Save ERROR messages to a new file
        with open("errors.log", "w") as error_file:
            for message in error_messages:
                error_file.write(message + "\n")
        
        return most_frequent
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {log_file_path} was not found.")
    except IOError as e:
        raise IOError(f"Error processing file: {str(e)}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")

# Example usage (uncomment to test with a sample log file)
if __name__ == "__main__":
    # Sample log content (for testing, create sample_logs.txt first)
    
    
    with open("sample_logs.txt", "w") as f:
        f.write("log_analyzed.txt")
    
    try:
        result = analyze_logs("sample_logs.txt")
        print(f"Most frequent log level: {result}")
        # Verify errors.log content (manual check recommended)
    except Exception as e:
        print(f"Error: {e}")