class AmazonAffiliateURL:
    def __init__(self, affiliate_tag: str):
        self.affiliate_tag = affiliate_tag
    
    def url(self, asin: str) -> str:
        return url(self.affiliate_tag, asin)

def url(affiliate_tag: str, asin: str) -> str:
    return 'https://www.amazon.com/dp/' + asin + '?tag=' + affiliate_tag