__author__ = 'adm'
def Fheader():
    headers = {
        "X-EBAY-SOA-SERVICE-NAME": "FindingService",
        "X-EBAY-SOA-OPERATION-NAME": "findItemsAdvanced",
        "X-EBAY-SOA-SERVICE-VERSION": "1.12.0",
        "X-EBAY-SOA-GLOBAL-ID": "EBAY-US",
        "X-EBAY-SOA-SECURITY-APPNAME": "EvgenyOr-f29a-41ba-9145-05cb5304c582",
        "X-EBAY-SOA-REQUEST-DATA-FORMAT": "XML"
    }
    return headers
