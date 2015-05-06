# coding=utf-8
__author__ = 'adm'
import httplib
import xml.etree.ElementTree as ET
import smtplib
import Fheader

xml = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"+\
    "<findItemsAdvancedRequest xmlns=\"http://www.ebay.com/marketplace/search/v1/services\">"+\
    "<categoryId>171485</categoryId>"+\
    "<sortOrder>EndTimeSoonest</sortOrder>"+\
    "<keywords>Nexus 7</keywords>"+\
    "<itemFilter>"+\
        "<name>Condition</name>"+\
        "<value>Used</value>"+\
    "</itemFilter>"+\
    "<itemFilter>"+\
        "<name> MaxPrice </name>"+\
        "<value> 140.00 </value>"+\
    "</itemFilter>"+\
    "<paginationInput>"+\
    "<entriesPerPage>50</entriesPerPage>"+\
    "</paginationInput>"+\
    "<outputSelector>SellerInfo</outputSelector>"+\
    "</findItemsAdvancedRequest>"

def sendRequest():
    connection = httplib.HTTPConnection('svcs.ebay.com') #didn't work with HTTPS
    connection.request("POST", '/services/search/FindingService/v1?', xml, Fheader.Fheader())
    response = connection.getresponse()
    if response.status != 200:
        print response.reason
        print response.read()
        return
    else:
        data = response.read()
        connection.close()
    pars(data)
    return

def pars(data):
    data = ET.fromstring(data)
    count = len(data.findall('.//{http://www.ebay.com/marketplace/search/v1/services}itemId'))
    msg = ''
    msg += '\n' + data.find('.//{http://www.ebay.com/marketplace/search/v1/services}timestamp').text + '\n'
    for i in xrange(0, count):
        #msg += data.findall('.//{http://www.ebay.com/marketplace/search/v1/services}itemId')[i].text + ' '
        msg += data.findall('.//{http://www.ebay.com/marketplace/search/v1/services}viewItemURL')[i].text + ' '
        msg += data.findall('.//{http://www.ebay.com/marketplace/search/v1/services}title')[i].text.encode('utf8') + ' '
        msg += '[' + data.findall('.//{http://www.ebay.com/marketplace/search/v1/services}currentPrice')[i].text + ']'
        msg += data.findall('.//{http://www.ebay.com/marketplace/search/v1/services}endTime')[i].text + ' '
        msg += data.findall('.//{http://www.ebay.com/marketplace/search/v1/services}conditionDisplayName')[i].text + "\n"+"\n"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login("evgenyorlov1@gmail.com", "sillybugs0")
    server.sendmail("evgenyorlov1@gmail.com", "evgenyorlov1@gmail.com", msg)
    server.quit()



def main():
    sendRequest()
    #raw_input('Pres Enter to exit')

if __name__ == "__main__":
    main()

