import requests
import sys
url = "https://api.github.com/search/repositories"


info = input("what do you want to search? :").strip()

if not info: 
    print("please enter a search term.")
    sys.exit()

params = {
      "q":info


}
response = requests.get(url,params=params)
data = response.json()
if not data["items"]:
    print("No repositories found")
    sys.exit()

print(len(data["items"]))



for repo in data["items"]:
    print("Repository:",repo["name"])
    print("Full name:",repo["full_name"])
    print("URL:",repo["html_url"])
    print("Stars:",repo["stargazers_count"])

