import requests
from colorama import init, Fore, Style
import argparse
import sys

# Initialize colorama for cross-platform terminal coloring support
init()

ASCII_LOGO = f"""
{Fore.WHITE}
       ⠀⣠⣠⣶⣿⣷⣿⣿⣿⣷⣷⣶⣤⣀⠀ AWS Ripper⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣾⣿⢿⣻⡽⣞⣳⡽⠚⠉⠉⠙⠛⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⢻⣟⣧⢿⣻⢿⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⡿⠞⠛⠚⠫⣟⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠈⢻⡽⣆⠀⠀⣴⣷⡄⠀⠀⠀⠘⣿⡆⠀⠀⣀⣠⣤⡄
⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠈⣿⠿⢷⡀⠘⠛⠃⠀⠠⠀⠀⣿⣅⣴⡶⠟⠋⢹⣿
⠀⠀⢻⣿⡀⠀⠀⠀⢾⣿⡆⠀⢿⣴⣴⡇⠀⠀⠀⠀⠀⠀⢠⡟⠋⠁⠀⠀⠀⢸⣿
⠀⠀⠈⢿⣇⠀⠀⠀⠈⠉⠥⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⣾⡏
⠀⠀⠀⠈⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠸⠁⠀⠀⠀⠀⠀⣼⡟⠀
⠀⠀⠀⠀⠀⣹⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠐⢧⡀⠀⢀⣾⠟⠀⠀
⠀⠀⢀⣰⣾⠟⠉⠀⠀⠉⠉⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡟⠋⠀⠀⠀
⣠⣶⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⣿⡆⠀⠀⠀⠀
⢻⣧⣄⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠉⠛⠿⣷⣶⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣾⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣷⣦⡀⠀⢀⣀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⠿⠟⠁⠀⠀⠀⠀
{Style.RESET_ALL}
"""

def check_bucket_accessibility(bucket_name):
    url = f"http://{bucket_name}.s3.amazonaws.com/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "open"
        else:
            return "Read"
    except requests.exceptions.RequestException:
        return "Read"

def search_containers(api_key, keywords):
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    for keyword in keywords:
        url = f'https://buckets.grayhatwarfare.com/api/v2/buckets?keywords={keyword}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['meta']['results'] > 0:
                print(Fore.YELLOW + f"Searching Bucket keyword '{keyword}':")
                for bucket in data['buckets']:
                    accessibility = check_bucket_accessibility(bucket['bucket'])
                    print(Fore.GREEN + f"{bucket['bucket']} - Size: {bucket['fileCount']} files - Accessibility: {accessibility}")
                print(Fore.RED + f"Total {data['meta']['results']} buckets found.")
            else:
                print(Fore.YELLOW + f"No Bucket found matching keyword '{keyword}'")
        else:
            print(Fore.RED + f"Failed to fetch data for keyword '{keyword}'")

def main():
    parser = argparse.ArgumentParser(description='Search for buckets using Grayhat Warfare API.')
    parser.add_argument('-k', '--keywords', type=str, nargs='+', help='Keywords to search for buckets')
    parser.add_argument('-w', '--wordlist', type=str, help='File containing a list of keywords to search for buckets')
    parser.add_argument('-a', '--apikey', type=str, required=True, help='API key for authentication')

    args = parser.parse_args()

    print(ASCII_LOGO)

    if args.keywords:
        search_containers(args.apikey, args.keywords)
    elif args.wordlist:
        with open(args.wordlist, 'r') as file:
            keywords = [line.strip() for line in file]
        search_containers(args.apikey, keywords)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
