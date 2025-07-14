#!/bin/bash

#threshold for alerts


THRESHOLD=80

#function to check CPU Usage

check_cpu_usage() {
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}' | cut -d. -f1)
    CPU_USAGE=$(printf "%.0f" "$CPU_IDLE")

    if [ "$CPU_USAGE" -ge "$THRESHOLD" ]; then
        echo "Alert : CPU usage is at {$CPU_USAGE}%"
    else
        echo "CPU usage is at {$CPU_USAGE}%"
    
    fi

}


# Function to check memory usage
check_memory_usage() {
    MEM=$(free | grep Mem)
    USED=$(echo $MEM | awk '{print $3}')
    TOTAL=$(echo $MEM | awk '{print $2}')
    MEM_USAGE=$((USED * 100 / TOTAL))
    if [ "$MEM_USAGE" -ge "$THRESHOLD" ]; then
        echo "ALERT: Memory usage is at ${MEM_USAGE}%"
    else
        echo "Memory usage is at ${MEM_USAGE}%"
    fi
}

# Function to check disk usage
check_disk_usage() {
    DISK_USAGE=$(df -h / | awk 'NR==2 {gsub("%",""); print $5}')
    if [ "$DISK_USAGE" -ge "$THRESHOLD" ]; then
        echo "ALERT: Disk usage on / is at ${DISK_USAGE}%"
    else
        echo "Disk usage on / is at ${DISK_USAGE}%"
    fi
}

# Run all checks
echo "Running system health check..."
check_cpu_usage
check_memory_usage
check_disk_usage
