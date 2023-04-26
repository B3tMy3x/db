import urllib
import requests


def guidedata(a):
    print("вызвана")
    if len(a) == 10 and a.isnumeric():
        r = f"https://www.dota2.com/workshop/builds/view?embedded=workshop&publishedfileid={a}&target_uri=https://steamcommunity.com&l=english&u=public"
        r = requests.get(r)
        r = r.text
        r = r[r.find('<div id="itemBuildContent">'):r.find('		<br clear="both"/>')]
        r = r.replace('</div>', '</div>\n')
        print(r)
        with open('news.html', 'w', encoding='utf-8') as f:
            f.write('''{% extends "base.html" %}
    {% block content %}
    <br>
        <div class="di1">
            <div class="col-md6">
                <h1>{{news.title}}</h1>
                <div>
                    {{news.content}}
                </div>''' +
            r +
            '''<div>
                    Автор - {{news.user.name}}, Дата написания - {{news.created_date}}
                </div>
            </div>
        </div>
    {% endblock %})
            ''')
        print("выполнена1")
    else:
        with open('news.html', 'w', encoding='utf-8') as f:
            f.write('''{% extends "base.html" %}
    {% block content %}
    <br>
        <div class="di1">
            <div class="col-md6">
                <h1>{{news.title}}</h1>
                <div>
                    {{news.content}}
                </div>
                <div>
                    Автор - {{news.user.name}}, Дата написания - {{news.created_date}}
                </div>
            </div>
        </div>
    {% endblock %})''')
        print("выполнена2")
    f.close()