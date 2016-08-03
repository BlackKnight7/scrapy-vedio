import urllib.request

url = 'http://v2.mukewang.com/410739b7-cd23-441d-aeaf-521f93648420/L.mp4?auth_key=1470217158-0-0-130c44d5978d70486c269a2ea119b4ba'
path = 'L.mp4';

urllib.request.urlretrieve(url, path)