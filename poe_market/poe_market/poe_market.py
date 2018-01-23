import re
import urllib.request
from bs4 import BeautifulSoup
from collections import OrderedDict

search_url = 'http://currency.poe.trade/search?league=Hardcore+Abyss&online=x&want=4&have=1'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse_menu(html):
    soup = BeautifulSoup(html, 'html.parser')
    select = soup.find('select', class_='league chosen')
    leagues = []
    options = select.find_all('option')
    #print(options)
    for i in range(len(options)):
        leagues.append(re.sub(r'\s+', '+', options[i].text))

    content_list = soup.find_all('div', class_='has-tip')
    path_array = {}
    path_array[0] = 'Array of relations between items'
    #path_array.insert(0,'Array of relations between items')
    name_list = {}
    name_list[0] = 'List of names'
    #name_list.insert(0,'List of names')
    for value in content_list:
        #title = re.split(r'"', re.search(r'title="\w+', value))
        #atr = map(value.attrs)
        atr = dict(value.attrs.items())
        title = atr.get('title')
        id = atr.get('data-id')
        if int(id) not in name_list:
            name_list[int(id)] = title
            #name_list.insert(int(id),title)
            path_array[int(id)] = []
            #path_array.insert(int(id),[])
        else:
            break
        #print(value.attrs.items())
        #print(value.attrs)
        #want.insert(value.id, { 'title': value.title, 'id':value.id}) 2 5
    return leagues, name_list
    #for i in sorted(name_list):
    #    print(i,name_list[i])
    #for i in sorted(path_array):
    #    print(i,path_array[i])

    #print(leagues)
    #for option in select.find_all('option'):
    #    print(option)

def parse_search(html):
    soup = BeautifulSoup(html, 'html.parser')
    offers = soup.find_all('div', class_='displayoffer')
    offer_list = []
    for value in offers:
        #title = re.split(r'"', re.search(r'title="\w+', value))
        #atr = map(value.attrs)
        atr = dict(value.attrs.items())
        ign = atr.get('data-ign')
        sellcur = atr.get('data-sellcurrency')
        sellval = atr.get('data-sellvalue')
        buycur = atr.get('data-buycurrency')
        buyval = atr.get('data-buyvalue')
        stock = atr.get('data-stock')
        offer_list.append({
            'ign':ign,
            'sellcur':sellcur,
            'sellval':sellval,
            'buycur':buycur,
            'buyval':buyval,
            'stock':stock
            })
        #print('ign: ',ign)
        #print('sellcur: ',sellcur)
        #print('sellval: ',sellval)
        #print('buycur: ',buycur)
        #print('buyval: ',buyval)
        #print('stock: ',stock,'\n')
    return offer_list
    #print(offers)


def main():
    order = []
    order.append('http://currency.poe.trade/search')
    order.append('?league=')
    order.append('&online=')
    order.append('&want=')
    order.append('&have=')
    print(order)
    leagues, name_list = parse_menu(get_html('http://currency.poe.trade/'))
    print(leagues)
    for i in sorted(name_list):
        print(i,name_list[i])
    print('Enter indices of items in the following order: want1, want2 - have1, have2')
    items = input()
    splited = re.split(r' *- *', (re.sub(r',+', ' ', items)))
    #print(splited)
    want = re.split(r' +', splited[0])
    have = re.split(r' +', splited[1])
    want_str = ''
    for i in range(len(want)):
        want_str += want[i]
        if i != len(want) - 1:
            want_str += '-'
    have_str = ''
    for i in range(len(have)):
        have_str += have[i]
        if i != len(have) - 1:
            have_str += '-'
    #print(want_str)
    #print(have_str)
    offer_list = parse_search(get_html(order[0]+order[1]+leagues[1]+order[2]+'x'+order[3]+want_str+order[4]+have_str))
    for i in offer_list:
        print(i)


if __name__ == '__main__':
    main()