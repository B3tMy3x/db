import urllib
import requests

def result(a):
    result = f"https://www.dota2.com/workshop/builds/view?embedded=workshop&publishedfileid={a}&target_uri=https://steamcommunity.com&l=english&u=public"
    r = requests.get(result)
    r = r.text
    r = r[r.find('itemBuildContent'):r.find('		<br clear="both"/>')]
    return r
