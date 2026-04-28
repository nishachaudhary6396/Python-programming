#https://google.com
import re
url = input("Enter URL: ")
pattern = r"^https?://[a-zA-Z]\.[a-zA-Z]{2,}$"
if re.match(pattern,url):
    print("Valid Url")
else:
    print("Invalid URL")