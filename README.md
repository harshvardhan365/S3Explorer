# S3Explorer

S3Explorer is a command-line tool designed to search for AWS S3 buckets using the Grayhat Warfare API. It provides information about the accessibility of the buckets, including whether they are open or read-only.

## Features

- **Keyword Search**: Search for AWS S3 buckets using specified keywords.
- **Wordlist Search**: Search for AWS S3 buckets using a file containing a list of keywords.
- **Bucket Accessibility Check**: Determine if the bucket is open or read-only.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/S3Explorer.git
    cd S3Explorer
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python s3explorer.py -a YOUR_API_KEY -k keyword1 keyword2
```

## Options
```bash
-k, --keywords : Keywords to search for buckets (space-separated).
-w, --wordlist : File containing a list of keywords to search for buckets.
-a, --apikey : API key for authentication (required).
```
## Examples Input
# Search with Keywords
```bash
python s3explorer.py -a YOUR_API_KEY -k example keyword
```
## Search with Wordlist
```bash
python s3explorer.py -a YOUR_API_KEY -w wordlist.txt
```
## Example Output
```bash
       ⠀⣠⣠⣶⣿⣷⣿⣿⣿⣷⣷⣶⣤⣀⠀ S3Explorer⠀⠀⠀⠀⠀⠀⠀⠀⠀
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

Searching Bucket keyword 'example':
example-bucket-1 - Size: 100 files - Accessibility: open
example-bucket-2 - Size: 50 files - Accessibility: Read
Total 2 buckets found.

Searching Bucket keyword 'keyword':
keyword-bucket-1 - Size: 200 files - Accessibility: open
keyword-bucket-2 - Size: 75 files - Accessibility: Read
Total 2 buckets found.
```
## Getting an API Key from Grayhat Warfare

To use S3Explorer, you need an API key from Grayhat Warfare. Follow these steps to obtain your API key:

1) Go to the [Grayhat Warfare API](https://buckets.grayhatwarfare.com/).
2) Sign up for an account if you don't have one.
3) Navigate to the API section and generate a new API key.
4) Use this API key with the -a or --apikey option when running S3Explorer.

## Screenshot

![image](https://github.com/user-attachments/assets/d3850482-f213-4749-8f3a-11239560f180)


## Developed by Harshvardhan for enhancing security in the Cyber Security Environment.



