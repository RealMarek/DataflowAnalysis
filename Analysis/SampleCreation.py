import json
import re
import requests
import urllib3
from bs4 import BeautifulSoup

#LINKS

def getIncomingLinks(wikipage):
    backlinks = []
    session = requests.Session()
    url = "https://de.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "backlinks",
        "bltitle": wikipage,
        "bllimit": 500
    }
    lastContinue = {}
    while True:
        actual_param = params.copy()
        actual_param.update(lastContinue)
        response = session.get(url=url, params=actual_param)
        data = response.json()
        if 'error' in data:
            raise Exception(data['error'])
        if 'warnings' in data:
            print(data['warnings'])
        if 'query' in data:
            backlinks.extend(data["query"]["backlinks"])
        if 'continue' not in data:
            break
        lastContinue = data['continue']
    return backlinks

def getOrderedLinks(wikipage):
    http = urllib3.PoolManager()
    response = http.request("GET", wikipage)
    soup = BeautifulSoup(response.data)
    soup = soup.find(id="mw-content-text")
    link_list = soup.find_all("a",href=re.compile("/wiki/"))
    return link_list

def filterTags(tagList):
    return [e for e in tagList if not "Wikipedia:" in e.get("href") and not "Benutzer:" in e.get("href") and not "Spezial:" in e.get("href") and not "Diskussion:" in e.get("href") and not "Portal:" in e.get("href")]

def tagToTitle(tagList):
    return [i.get("title") for i in tagList]

def deleteDuplicates(titleList):
    return list(dict.fromkeys(titleList))

def getTitlePosition(titleList, title):
    return titleList.index(title)

def saveLinks(base_link, outgoing_links, position):
    data = {
        "baselink": base_link,
        "outgoing_links": outgoing_links
    }
    with open(position, "a") as link_file:
        file = json.dumps(data)
        type(file)
        link_file.write(file)

def getPositionsOfBaselink(backlink, baselink):
    orderedBacklinkLinks = deleteDuplicates(tagToTitle(filterTags(getOrderedLinks("https://de.wikipedia.org/wiki/" + backlink))))
    return getTitlePosition(orderedBacklinkLinks, baselink)

def createLinkFile(titelList,position):
    for titel in titelList:
        ordered = deleteDuplicates(tagToTitle(filterTags(getOrderedLinks("https://de.wikipedia.org/wiki/" + titel)), 30))
        saveLinks(titel,ordered,position)

#PAGEVIEWS
def getPageViews(name):
    address = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/de.wikipedia.org/all-access/user/" + name + "/daily/20230701/20231001"
    # Personal username for identification for the Wikipedia API
    headers = {'User-Agent': 'marek.seipel@web.de'}
    resp = requests.get(address, headers=headers)
    details = resp.json()
    return [{"date": e["timestamp"], "views": e["views"]} for e in details["items"]]

#TOTAL

def createCompleteFile(pageName, location):
    base_views = getPageViews(pageName)
    all_backlinks = getIncomingLinks(pageName)
    backlinks_complete = []
    links_complete = []
    for backlink in all_backlinks:
        backlinks_complete.append({"name": pageName, "position": getPositionsOfBaselink(backlink, pageName), "views": getPageViews(backlink)})
    ordered_links = deleteDuplicates(tagToTitle(filterTags(getOrderedLinks("https://de.wikipedia.org/wiki/" + pageName))))
    for link in ordered_links:
        links_complete.append({"name": link, "views": getPageViews(link)})
    data = {
        "baselink": {
            "name": pageName,
            "views": base_views
        },
        "backlinks": backlinks_complete,
        "links": links_complete
    }
    with open(location, "a") as link_file:
        file = json.dumps(data)
        type(file)
        link_file.write(file)