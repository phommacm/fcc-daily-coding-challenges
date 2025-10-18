#!/usr/bin/env bash

# Path to the scripts directory
BASE_DIR="scripts"

# Ask for challenge name
read -e -p "→ Enter challenge name: " challenge
while [[ -z "$challenge" ]]; do
    read -e -p "Challenge name cannot be empty. Enter challenge name: " challenge
done

# Sanitize challenge name
challenge=$(echo "$challenge" | xargs | tr '[:upper:]' '[:lower:]' | tr -s ' ' '_')

# Get today's date and use it as a default value
printf -v today '%(%Y-%m-%d)T' -1
read -e -p "→ Enter challenge date: " -i "$today" date

# Create folder with an empty README.md
folder="${BASE_DIR}/${date}_${challenge}"

if [[ -d "$folder" ]]; then
    echo "Folder already exists: $folder"
else
    mkdir -p "$folder"
    touch "${BASE_DIR}/${date}_${challenge}/README.md"
    echo "→ Successfully created: $folder"
    echo "→ Successfully created an empty README.md"
fi
