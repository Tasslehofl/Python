#!/bin/bash

# Here is what we are going to do with this Recon tool:
# see whois
# find subdomains
# see if subdomains are alive
# screenshot alive subdomains

#Variables
domain=$1 # declairing the domain that we will be supplying
#creating different paths
info_path=$domain/info
subdomain_path=$domain/subdomains
screenshot_path=$domain/screenshots
#setting colors
RED="\033[1;31m"
RESET="\033[0m"

#creating the folders if they do not exist
if [ ! -d "$domain" ];then
	mkdir $domain
fi
#
if [ ! -d "$info_path" ];then
	mkdir $info_path
fi
#
if [ ! -d "$subdomain_path" ];then
	mkdir $subdomain_path
fi
#
if [ ! -d "$screenshot_path" ];then
	mkdir $screenshot_path
fi

#running the program
echo -e "${RED} [+] Checking who it is ... ${RESET}"
whois $1 > $info_path/whois.txt

echo -e "${RED} [+] Launching subfinder ... ${RESET}"
subfinder -d $domain > $subdomain_path/found.txt

echo -e "${RED} [+] Running assetfinder ... ${RESET}"
assetfinder $domain | grep $domain >> $subdomain_path/found.txt
#doing the grep command will only bring back the domains, since assetfinder provides more than just the domain information.

#commenting out the code below because it does take so long
# echo -e "${RED} [+] Running Amass. This could take a while ... ${RESET}"
# amass enum -d $domain ?? $subdomain_path/found.txt

echo -e "${RED} [+] Checking what's alive ... ${RESET}"
cat $subdomain_path/found.txt | grep $domain | sort -u | httprobe -prefer-https | grep https | sed 's/https\?:\/\///' | tee -a $subdomain_path/alive.txt
#sed - this command will remove all the https stuff at the beginning and the 443 at the end
#tee - will write to the file as well as write it to the screen so we can see it

echo -e "${RED} [+] Taking screenshots... ${RESET}"
gowitness file -f $subdomain_path/alive.txt -P $screenshot_path/ --no-http


