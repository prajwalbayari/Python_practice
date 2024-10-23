import requests
import json
import shutil

print(shutil.get_terminal_size().columns*'-')

query=input("Enter your genre: ")
print("\n"+shutil.get_terminal_size().columns*'-'+"\n")
r = requests.get(f"https://newsapi.org/v2/everything?q={query}&from=2024-09-20&sortBy=publishedAt&apiKey=26582b9d740947c18899438d254c92bf")
news=json.loads(r.text)

# print(news,type(news),dir(news))

for article in news['articles']:
    if article['title']!='[Removed]' and article['description']!='[Removed]':
        print(article['title'])
        print(article['description'])
        print("\n"+shutil.get_terminal_size().columns*'-'+"\n")