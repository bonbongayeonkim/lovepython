from urllib import request
url = 'https://gray-kktv-prod.cdn.arcpublishing.com/resizer/qudmGCxwpzeiKWaTecsihx2PB8A=/1200x675/smart/filters:quality(85)/cloudfront-us-east-1.images.arcpublishing.com/gray/QEURVAQKANERZBDDOI4RXNXUCA.png'
filename='05_crawling/down/사탕.jpg'
request.urlretrieve(url,filename)
