#!/bin/bash
# Script to append focus messages to may.log

# Check if a message was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <message>"
    exit 1
fi

# Define the log file path
LOG_FILE="/home/user/rotko/ibphours/may.log"

# Append the message to the log file with a compact UTC timestamp
echo "$(date -u '+%y%m%d-%H%M') - $*" >> "$LOG_FILE"

