# parser.py 
# Tyson Hartwig
# python 3
# This parser prepares an xml data file items-*.xml for bulk loading
# into an SQL database.

from __future__ import print_function
import datetime
import locale
import sys
try:                                 # cElementTree is faster but 
    import xml.etree.cElementTree    # not standard.
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
        # self.categoryTable = list()
        self.categoryFile = open('category.txt', 'a+')
        self.auctionsFile = open('auctions.txt', 'a+')

    def iterparent(self, tree):
        for parent in tree.getiterator():
            for child in parent:
                yield parent, child

    def processFile(self, filename):
        domItems   = xml.etree.ElementTree.parse(filename) 
        root = domItems.getroot()
        for parent, child in self.iterparent(root):
            print(parent.tag, child.tag)
            if child.tag == 'Name':
                itemID = parent.get('ItemID')
                row = itemID + '<>' + child.text
            elif child.tag == 'Category':
                print(itemID, '<>', child.text, 
                     file = self.categoryFile)
            elif child.tag == 'First_Bid' or child.tag == 'Description':  
                print('<>', child.text, 
                     file = self.auctionsFile, end = ' ')
            elif child.tag == 'Started' or child.tag == 'Ends':
                print('<>', transform_dttm(child.text), 
                     file = self.auctionsFile, end = ' ')
            elif child.tag == 'Description':
                row = row + child.text
                print(row, '\n', file = self.auctionsFile)
        """
            else: print('Unknown Tag?')

        for item in root:
            for category in item.findall('Category'):
               print(item.get('ItemID'),'<>', category.text, 
                     file=self.categoryFile)
        """
def main():
    if len(sys.argv) <= 1:
        print("Usage: python3", sys.argv[0], "[file] [file] ...")
    ebay = Processor()     
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    for filename in sys.argv[1:]:
        ebay.processFile(filename)

if __name__ == "__main__":
    main()
