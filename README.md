# amazon_affiliate_url

## Install
~~~~shell
pip install amazon_affiliate_url
or
pip3 install amazon_affiliate_url
~~~~

## Usage
~~~~python
from amazon_affiliate_url.amazon_affiliate_url import AmazonAffiliateURL

affiliate_tag = 'YOUR_AFFILIATE_TAG'
asin = 'PRODUCT_ASIN'

url_creator = AmazonAffiliateURL(affiliate_tag)
affiliate_link = url_creator.url(asin)

print('affiliate_link:', affiliate_link)
~~~~
