#!/bin/bash

# kill_processes.sh
# Kills processes by name, counts them, logs action.
# Usage: ./kill_processes.sh [-d] <process_name>

LOG=~/process_killer.log
DRY_RUN=0
PROCESS_NAME=""

# Check for -d flag
if [ "$1" = "-d" ]; then
    DRY_RUN=1
    PROCESS_NAME="$2"
else
    PROCESS_NAME="$1"
fi

# Validate process name
if [ -z "$PROCESS_NAME" ]; then
    echo "Error: Please provide a process name (e.g., $0 java [-d])"
    exit 1
fi

PIDS=$(pgrep -i "$PROCESS_NAME")
[ -z "$PIDS" ] && { echo "No processes found for '$PROCESS_NAME'."; exit 0; }

COUNT=$(echo "$PIDS" | wc -l)

if [ "$DRY_RUN" -eq 1 ]; then
    echo "Dry-run: Would kill $COUNT processes for '$PROCESS_NAME': $PIDS"
else
    echo "$PIDS" | xargs kill 2>/dev/null
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Killed $COUNT processes for '$PROCESS_NAME'" >> "$LOG"
    echo "Killed $COUNT processes. Logged to $LOG."
fi