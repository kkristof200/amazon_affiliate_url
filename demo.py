from amazon_affiliate_url import AmazonAffiliateUrl, Country

ASIN = 'SOME_ASIN'
TAG =  'YOUR_AFFILIATE_TAG'
BITLY_TOKEN = 'YOUR_BITLY_TOKEN'

print(
    AmazonAffiliateUrl.url_cls(
        asin_or_url=ASIN,
        affiliate_tag=TAG,
        # bitly_token=BITLY_TOKEN,
        # shorten_url=True,
        country=Country.Netherlands
    )
)
