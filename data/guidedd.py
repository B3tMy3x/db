import urllib
import requests

def result():
    result = "https://www.dota2.com/workshop/builds/view?embedded=workshop&publishedfileid=2966180100&target_uri=https://steamcommunity.com&l=english&u=public"
    r = requests.get(result)
    return r.text

a = result()
a = a[a.find('itemBuildContent'):a.find('		<br clear="both"/>')]
print(a)