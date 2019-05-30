from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simpe_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                # print(resp.content)
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error(e)
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


def find_tag(content):
    soup = BeautifulSoup(content, 'html.parser')

    for tag in soup.find_all("meta"):
        if tag.get("name", None) == "keywords":
            print(tag.get("content", None))
        # elif tag.get("property", None) == "og:url":
        #     print(
        #     tag.get("content", None))


    # kw = soup.find_all("meta", name="keywords")


    # print(kw["content"] if kw else "No meta title given")



    # for m in html.find_all("meta"):
    #     xxx = m.get('name')
    #     if xxx == 'keywords':
    #         print(xxx)
        # print(m.get('name'))
        # for k in m.find_all('keywords'):
        #     print('aaa:aaa: ', k)
    # print(html.prettify())

    # print(html.head.meta)

    # for m in html.head:
    #     a = ''
    #     if m.has_attr('charset'):
    #         if m['charset'] == 'utf-8':
    #
    #     # if m.name == "keywords":
    #     #     print(m)
    #             print(m)

    # print(html.find_all('keywords'))
        # print('\n')
    # print(html.find_all('meta'))
    # for m in html.select('meta'):
    #     # if m['name'] == 'keywords':
    #     print(m.text)
