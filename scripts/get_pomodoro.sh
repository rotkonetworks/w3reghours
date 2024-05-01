#!/bin/bash
# File: get_pomodoro.sh

# URL of the Pomodoro API
URL="http://localhost:9999"

# File to store the count of completed half-hours
COUNT_FILE="/home/user/rotko/ibphours/half_hour_pomodoro_counts_may.txt"
LOCK_FILE="/home/user/rotko/ibphours/.half_hour_pomodoro_counts_may.txt"
COMMIT_FILE="/home/user/rotko/ibphours/may.log"
increment_count() {
    (
        flock -x 200

        # Read the count, default to 0 if not set
        if [ ! -f "$COUNT_FILE" ]; then
            echo 0 > "$COUNT_FILE"
        fi

        count=$(<"$COUNT_FILE")
        ((count++))
        echo $count > "$COUNT_FILE"
    ) 200>"$LOCK_FILE"
}

commit_timetracking() {
    commit_message=$(tail -n 1 "$COMMIT_FILE")
    git add "$COUNT_FILE"
    git commit -m "pomodoro: $commit_message"
    cd /home/user/rotko/ibphours && git push
}

# Initialize the count file if it doesn't exist
if [ ! -f "$COUNT_FILE" ]; then
    echo 0 > "$COUNT_FILE"
fi

# Function to play a beep sound
play_beep() {
    speaker-test -t sine -f 1000 -l 1 -p 1 >/dev/null 2>&1
}

# Fetch the current timer status from the FastAPI server
response=$(curl -s $URL/time)

if [[ "$response" == *"take_break"* ]]; then
    play_beep
    echo "🍅 Take break!"
    curl -s $URL/next >/dev/null  # Automatically call next to start new period
    increment_count
elif [[ "$response" == *"work_bitch"* ]]; then
    play_beep
    echo "🍅 Work bitch!"
    curl -s $URL/next >/dev/null  # Automatically call next to start new period
elif [[ "$response" == *"PAUSE"* ]]; then
    echo "🍅 Paused"  # Display pause status in Polybar
elif [[ "$response" == *"NO_POMODORO"* ]]; then
    echo "No Pomodoro"  # Display no timer running
else
    # Extract the remaining time and format it for display in Polybar
    remaining=$(echo "$response" | grep -oE '[0-9]{1,2}:[0-9]{2}')
    echo "🍅 $remaining"  # Show remaining time with an icon
fi
