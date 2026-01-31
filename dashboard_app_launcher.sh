#!/bin/bash


SCRIPT_DIR="/home/pi/Documents/Project/Dashboard"
cd "$SCRIPT_DIR"

function exit_cleanup {
	if [ "$is_env_activated" -eq 1 ]; then
		echo "Deactivating Virtual Enviornment"
		deactivate
	fi
	echo "Application closed"
}

trap exit_cleanup EXIT


is_env_activated=0

if [ -d "venv" ]; then
	echo "Virtual Environment exists, Activating...."
	source venv/bin/activate
	is_env_activated=1
else
	echo "Unable to find virtual enviornment: $(pwd)"
	exit 0
fi

echo "Setting dispaly to 0"
export DISPLAY=:0

echo "Running the application"
python main.py
