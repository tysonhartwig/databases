# parser.py 
# Tyson Hartwig
# python 3
# This parser prepares an xml data file items-*.xml for bulk loading
# into an SQL database.

from __future__ import print_function
import datetime
import locale
import sys
import time
try:                                 # cElementTree is faster but 
    import xml.etree.cElementTree    # not always available.
except ImportError:
    import xml.etree.ElementTree

def transformDollar(dollar_str):
    """
    Returns the amount (in XXXXX.xx format) denoted by a money-string
    like $3,453.23. 
    """
    return '{:.2f}'.format(locale.atof(dollar_str.strip("$")))

def transform_dttm(dttm_str):
    """
    Returns date/time string in format like "2001-03-25 10:25:57" from
    a format like "Mar-25-01 10:25:57".
    """
    dt = datetime.datetime.strptime(dttm_str, "%b-%d-%y %H:%M:%S")  
    return dt.isoformat(' ')

class Processor: 
    def __init__(self):
        self.categoryFile = open('category.txt', 'a+')
        self.auctionsFile = open('auctions.txt', 'a+')
        self.delimiter    = '<>'

    def iterparent(self, tree):
        for parent in tree.iter():
            for child in parent:
                if parent.tag != 'Items': yield parent, child

    def processFile(self, filename):
        domItems    = xml.etree.ElementTree.parse(filename) 
        root        = domItems.getroot()
        categoryRow = list() 
        auctionsRow = list()
        for parent, child in self.iterparent(root):
            if child.tag == 'Name':
                itemID     = parent.get('ItemID')
                itemNameID = itemID + self.delimiter + child.text
            elif child.tag == 'Category':
                categoryRow.append(itemID + self.delimiter + child.text)
            elif child.tag == 'First_Bid':
                itemMinBid = self.delimiter + child.text
            elif child.tag == 'Starts':
                startDate = self.delimiter + transform_dttm(child.text) 
            elif child.tag == 'Ends':
                endDate = self.delimiter + transform_dttm(child.text) 
            elif child.tag == 'Description':
                auctionsRow.append(itemNameID + itemMinBid + startDate 
                                              + endDate    + self.delimiter 
                                              + child.text)
                print(child.text)
            elif parent.tag == 'Bids':
                print(child.text)
        self.categoryFile.write("\n".join(categoryRow))
        self.auctionsFile.write("\n".join(auctionsRow))

def main():
    startTime = time.time()
    if len(sys.argv) <= 1:
        print("Usage: python3", sys.argv[0], "[file] [file] ...")
    ebay = Processor()     
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    for filename in sys.argv[1:]:
        ebay.processFile(filename)
    endTime = time.time()
    print("Elapsed time was %g seconds" % (endTime - startTime))

if __name__ == "__main__":
    main()
