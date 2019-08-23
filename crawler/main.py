import requests, re, os
from bs4 import BeautifulSoup

def append_url(url):
    return "http://www.cs.unc.edu/~plaisted/comp455/" + url


def append_file_name(file_name):
    return 'data/' + file_name


def download_data(file):
    file_url = file.get('href', None)
    if file_url is None:
        with open(append_file_name('Hyperlinks.txt'), 'a') as f:
            f.write(file['extended_url'])
        return
    else:
        resp = requests.get(file['extended_url'])
        with open(append_file_name(file['href']), 'wb') as f:
            f.write(resp.content)


def create_folder(file):
    file_href = file['href']
    if file_href is None:
        return
    else:
        re_str = r'\w+\/\w+'
        path = 'data/'
        if re.match(re_str, file_href):
            path_append = re.split(r'\/', file_href)[0] + '/'
            path += path_append

        if not os.path.exists(path):
            os.makedirs(path)
            return


def main():    
    resp = requests.get('http://www.cs.unc.edu/~plaisted/comp455/').text
    soup = BeautifulSoup(resp, 'lxml')
    all_href = soup.find_all('a')
    href_list = []

    for href in all_href:
        href_str = href.string
        if re.match(r'\n', href_str):
            href_str = re.split(r'\n', href_str)[-1]
        href_list.append({'Name': href_str, 'href': href['href']})

    if not os.path.exists('data/'):
        os.makedirs('data/')

    url_header_http = r'http\:\/\/'

    for url in href_list:
        if not re.match(url_header_http, url['href']):
            url['extended_url'] = append_url(url['href'])
        else:
            url['extended_url'] = url['href']
            url['href'] = None

    for url in href_list:
        create_folder(url)

    for url in href_list:
        download_data(url)


main()