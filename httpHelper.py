import urllib3 as urllib
def PostAsync(url):
    urllib.request("POST",url=url)