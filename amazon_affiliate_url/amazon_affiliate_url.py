# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Tuple, List
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
# from urllib import urlencode

# Pip
from bitlyshortener import Shortener

# Local
from .country import Country

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: AmazonAffiliateUrl ------------------------------------------------------- #

class AmazonAffiliateUrl:

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        affiliate_tag: str,
        shorten_urls: bool = False,
        accept_long_urls: bool = True,
        bitly_token: Optional[Tuple[str, List[str]]] = None,
        country: Country = Country.UnitedStates
    ):
        """Creates an AmazonAffiliateUrl object

        Args:
            affiliate_tag (str): [description]. Your affiliate tag.
            shorten_url (bool, optional): Shorten the generated url. Defaults to False).
            accept_long_url (bool, optional): If url shortening is unsuccessful, should the url still be returned. Defaults to True).
            bitly_token (Optional[Tuple[str, List[str]]], optional): Bitly token(s) needed for URL shortening. Defaults to None.
            country (Optional[Country], optional): Country to use to create the link with. Only used, if asiin is passed instead of url (Defaults to Country.UnitedStates).
        """
        self.affiliate_tag = affiliate_tag
        self.shorten_urls = shorten_urls
        self.accept_long_urls = accept_long_urls
        self.bitly_token = bitly_token
        self.country = country


    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    def url(
        self,
        asin_or_url: str,
        affiliate_tag: Optional[str] = None,
        shorten_url: Optional[bool] = None,
        accept_long_url: Optional[bool] = None,
        bitly_token: Optional[Tuple[str, List[str]]] = None,
        country: Optional[Country] = None
    ) -> Optional[str]:
        """Generate affiliate url, or replace ones tag with yours

        Args:
            asin_or_url (str): An asin or an amazon url
            affiliate_tag (Optional[str], optional): [description]. Defaults to None(used from self).
            shorten_url (Optional[bool], optional): Shorten the generated url. Defaults to None(used from self(defults to False)).
            accept_long_url (Optional[bool], optional): If url shortening is unsuccessful, should the url still be returned. Defaults to None(used from self(defults to True)).
            bitly_token (Optional[Tuple[str, List[str]]], optional): Bitly token(s) needed for URL shortening. Defaults to None.
            country (Optional[Country], optional): Country to use to create the link with. Only used, if asiin is passed instead of url (Defaults to None).

        Returns:
            Optional[str]: Amazon url with the passed affiliate tag
        """
        if 'amazon.' in asin_or_url or 'amzn.' in asin_or_url:
            url = asin_or_url

            if not asin_or_url.startswith('https://') and not asin_or_url.startswith('http://'):
                url = 'https://{}'.format(url)
        else:
            country = country or self.country
            url = 'https://amazon.{}/dp/{}'.format(country.value, asin_or_url)

        parsed_url = urlparse(url)

        if not parsed_url.netloc:
            print('ERROR-AmazonAffiliateUrl: Invalid Formatted URL Original:\'{}\' ---> Formatted:\'{}\''.format(asin_or_url, url))

            return None

        affiliate_tag = affiliate_tag or self.affiliate_tag

        if not affiliate_tag.endswith('-20'):
            affiliate_tag += '-20'

        shorten_url = shorten_url if shorten_url is not None else self.shorten_urls

        query_dict = parse_qs(parsed_url[4])
        query_dict['tag'] = affiliate_tag or self.affiliate_tag
        parsed_url = parsed_url[:4] + (urlencode(query_dict, True), ) + parsed_url[5:]
        url = urlunparse(parsed_url)

        if shorten_url:
            bitly_token = bitly_token or self.bitly_token
            accept_long_url = accept_long_url if accept_long_url is not None else self.accept_long_urls

            if not bitly_token:
                print('WARNING-AmazonAffiliateUrl: No bitly token(s) passed. These are necessary for URL shortening.')

                return url if accept_long_url else None

            if type(bitly_token) == str:
                bitly_token = [bitly_token]

            short_urls = Shortener(tokens=bitly_token).shorten_urls([url])

            if short_urls:
                return short_urls[0]
            elif accept_long_url:
                return url
            
            return None

        return url

    @classmethod
    def url_cls(
        cls,
        asin_or_url: str,
        affiliate_tag: str,
        shorten_url: bool = False,
        accept_long_url: bool = True,
        bitly_token: Optional[Tuple[str, List[str]]] = None,
        country: Optional[Country] = None
    ) -> Optional[str]:
        """Generate affiliate url, or replace ones tag with yours

        Args:
            asin_or_url (str): An asin or an amazon url
            affiliate_tag (str): [description]. Your affiliate tag.
            shorten_url (bool, optional): Shorten the generated url. (Defaults to False).
            accept_long_url (bool, optional): If url shortening is unsuccessful, should the url still be returned. (Defaults to True).
            bitly_token (Optional[Tuple[str, List[str]]], optional): Bitly token(s) needed for URL shortening. (Defaults to None).
            country (Optional[Country], optional): Country to use to create the link with. Only used, if asiin is passed instead of url (Defaults to None).

        Returns:
            Optional[str]: Amazon url with the passed affiliate tag
        """
        return cls(affiliate_tag).url(asin_or_url, shorten_url=shorten_url, accept_long_url=accept_long_url, bitly_token=bitly_token, country=country)


# ---------------------------------------------------------------------------------------------------------------------------------------- #