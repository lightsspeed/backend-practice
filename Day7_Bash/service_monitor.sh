#!/bin/bash

# Services to monitor
SERVICES=("nginx" "docker" "ssh")
LOGFILE="/var/log/service_monitor.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Ensure log file exists
touch $LOGFILE

echo "[$TIMESTAMP] Starting service status check..." >> $LOGFILE

for SERVICE in "${SERVICES[@]}"; do
    systemctl is-active --quiet "$SERVICE"
    STATUS=$?

    if [ $STATUS -eq 0 ]; then
        echo "[$TIMESTAMP] $SERVICE is running." >> $LOGFILE
    else
        echo "[$TIMESTAMP] $SERVICE is NOT running. Attempting to restart..." >> $LOGFILE
        systemctl restart "$SERVICE"

        if [ $? -eq 0 ]; then
            echo "[$TIMESTAMP] Successfully restarted $SERVICE." >> $LOGFILE
        else
            echo "[$TIMESTAMP] FAILED to restart $SERVICE." >> $LOGFILE
        fi
    fi
done

echo "[$TIMESTAMP] Service check completed." >> $LOGFILE
