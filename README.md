# amazon_affiliate_url

## Install

~~~~shell
pip install amazon_affiliate_url
or
pip3 install amazon_affiliate_url
~~~~

## Usage

~~~~python
from amazon_affiliate_url import AmazonAffiliateUrl

ASIN = 'SOME_ASIN'
TAG =  'YOUR_AFFILIATE_TAG'
BITLY_TOKEN = 'YOUR_BITLY_TOKEN'

print(
    AmazonAffiliateUrl.url_cls(
        asin_or_url=ASIN,
        affiliate_tag=TAG,
        bitly_token=BITLY_TOKEN,
        shorten_url=True
    )
)
~~~~
