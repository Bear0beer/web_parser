from app import client

from .secondary import n_pluse_one, bbc, dw, spiegel
from config import URL_PLUS_ONE as n_plus_url, \
    URL_BBC as bbc_url, \
    URL_DW as dw_url, \
    URL_SPIEGEL as spiegel_url



def get_all():
    n_plus = n_pluse_one(n_plus_url)
    bbc_news = bbc(bbc_url)
    dw_news = dw(dw_url)
    spiegel_news = spiegel(spiegel_url)
    all_preview = [n_plus, bbc_news, dw_news, spiegel_news]

    return all_preview