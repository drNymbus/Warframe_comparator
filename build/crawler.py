from bs4 import BeautifulSoup
import requests

url_data = "http://warframe.wikia.com/wiki/Weapon_Comparison"

category = ['Primary', 'Secondary', 'Melee', 'AW Primary', 'AW Melee']

def get_data(url, category):
    my_url = url+"#"+category
    file = requests.get(my_url)
    html = BeautifulSoup(file.text, 'html.parser')

    keys=[]
    guns = []

    html = html.find(title=category)
    for div in html.find_all('div', class_="tabbertab"):
        if category != 'AW Primary' or category != 'AW Melee':
            if div.get('title') == 'All' or div.get('title') == 'All weapons':

                for th in div.find_all('th'):
                    th = th.text.encode("utf-8")
                    th = th.replace('\n','')
                    keys.append(th)

                dict = {}
                count=0
                for td in div.find_all('td'):
                    td = td.text.encode("utf-8")
                    td = td.replace('\n','')
                    dict[keys[count]] = td

                    count += 1
                    if count > len(keys)-1:
                        guns.append(dict)
                        dict={}
                        count=0
        else:
            for th in div.find_all('th'):
                th = th.text.encode("utf-8")
                th = th.replace('\n', '')
                keys.append(th)

            dict = {}
            count = 0
            for td in div.find_all('td'):
                td = td.text.encode("utf-8")
                td = td.replace('\n', '')
                dict[keys[count]] = td

                count += 1
                if count > len(keys) - 1:
                    guns.append(dict)
                    dict = {}
                    count = 0

    return guns, keys

def all_weapons(url, category):
    weapons_category = []

    for type in category:
        url_category = url+'#'+type
        data, keys = get_data(url_category, type)
        weapons_category.append((data,keys))

    return weapons_category