import requests

def get_post_tags(post_id):
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        for post in data["posts"]:
            if post["id"] == post_id:
                return post["tags"]
           # for values in data["posts"][0]["tags"]:
               # tags_.append(values)
                
    else:
        print("Failed to fetch data from the endpoint")    
    
    
    


print(get_post_tags(146))
