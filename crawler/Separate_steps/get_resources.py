import re, json, requests, os

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

# 因为验证过所有的文件目录
# 发现“无论怎么样最多都只会有一层Folder”
# 所以为了省事就这么直接写了

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
    if not os.path.exists('data/'):
        os.makedirs('data/')

    all_hrefs = {}

    with open('all_href.txt', 'r') as f:
        all_hrefs = json.loads(f.read())

    url_header_http = r'http\:\/\/'

    for url in all_hrefs:
        if not re.match(url_header_http, url['href']):
            url['extended_url'] = append_url(url['href'])
        else:
            url['extended_url'] = url['href']
            url['href'] = None

    for url in all_hrefs:
        create_folder(url)

    for url in all_hrefs:
        download_data(url)
        
        
main()