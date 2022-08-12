# SuperFastPython.com
# example of checking the status of many websites
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus

# get the status of a website
def get_website_status(url):
    # handle connection errors
    try:
        # open a connection to the server with a timeout
        with urlopen(url, timeout=3) as connection:
            # get the response code, e.g. 200
            code = connection.getcode()
            return code
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason
    except Exception as e:
        return e

# interpret an HTTP response code into a status
def get_status(code):
    if code == HTTPStatus.OK:
        return 'OK'
    return 'ERROR'

# check status of a list of websites
def check_status_urls(urls):
    for url in urls:
        # get the status for the website
        code = get_website_status(url)
        # interpret the status
        status = get_status(code)
        # report status
        print(f'{url:20s}\t{status:5s}\t{code}')

# protect the entry point
if __name__ == '__main__':
    # list of urls to check
    urls = ['https://twitter.com',
            'https://google.com',
            'https://facebook.com',
            'https://reddit.com',
            'https://youtube.com',
            'https://amazon.com',
            'https://wikipedia.org',
            'https://ebay.com',
            'https://instagram.com',
            'https://cnn.com']
    # check all urls
    check_status_urls(urls)
