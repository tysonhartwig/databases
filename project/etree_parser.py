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

def transform_dollar(dollar_str):
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
        self.userFile     = open('users.txt', 'a+')
        self.bidsFile     = open('bids.txt', 'a+')
        self.currentFile  = open('current.txt','a+')
        self.delimiter    = '<>'

    def iterparent(self, tree):
        for parent in tree.iter():
            if parent.tag != 'Items' and parent.tag != 'Bids': 
                for child in parent:
                    yield parent, child

    def processFile(self, filename):
        domItems    = xml.etree.ElementTree.parse(filename) 
        root        = domItems.getroot()
        categoryRow = list()
        auctionsRow = list()
        bidsRow     = list()
        usersRow    = list()
        currentRow  = list()
	# This endless set of elifs puts each variable in the                    
	# correct table, row and column. Note that it is 
	# highly dependent on the output order of iterparent()
	# and the structure of the xml.
        for parent, child in self.iterparent(root):                      
            bidderLocation = self.delimiter + 'NULL' 
            bidderCountry  = self.delimiter + 'NULL' 
            description    = self.delimiter + 'NULL' 
            if child.tag == 'Name':                                      
                itemID     = parent.get('ItemID')                        
                itemNameID = itemID + self.delimiter + child.text
            elif child.tag == 'Category':
                categoryRow.append(itemID + self.delimiter + child.text)
            elif child.tag == 'Currently':
                currentBid = self.delimiter + transform_dollar(child.text)
            elif child.tag == 'First_Bid':
                itemMinBid = self.delimiter + transform_dollar(child.text)
            elif child.tag == 'Number_of_Bids':
                numBids = self.delimiter + child.text
            elif child.tag == 'Started':
                startDate = self.delimiter + transform_dttm(child.text) 
            elif child.tag == 'Ends':
                endDate = self.delimiter + transform_dttm(child.text) 
            elif child.tag == 'Location':
                sellerLocation = self.delimiter + child.text 
            elif child.tag == 'Country':
                sellerCountry = self.delimiter + child.text 
            elif child.tag == 'Seller':
                sellerID = child.get('UserID')
                usersRow.append(sellerID + self.delimiter 
                                + child.get('Rating') + sellerLocation 
                                + sellerCountry)       
            elif child.tag == 'Description':
                if child.text != None:
                    description = self.delimiter + child.text
                auctionsRow.append(itemNameID + itemMinBid 
                                   + startDate + endDate    
                                   + self.delimiter + sellerID 
                                   + description )
                currentRow.append(itemID + numBids + currentBid)
            elif child.tag == 'Bidder':
                bidderID     = child.get('UserID')
                bidderRating = self.delimiter + child.get('Rating')
            elif child.tag == 'Location':
                bidderLocation = self.delimiter + child.text 
            elif child.tag == 'Country':
                bidderCountry = self.delimiter + child.text 
            elif child.tag == 'Time':
                bidTime = self.delimiter + transform_dttm(child.text) 
            elif child.tag == 'Amount':
                bidAmount = self.delimiter + transform_dollar(child.text)
                usersRow.append(bidderID + bidderRating
                                + bidderLocation + bidderCountry)       
                bidsRow.append(itemID + self.delimiter 
                               + bidderID + bidTime + bidAmount)
        self.categoryFile.write('\n'.join(categoryRow))
        self.categoryFile.write('\n')
        self.auctionsFile.write('\n'.join(auctionsRow))
        self.auctionsFile.write('\n')
        self.currentFile.write('\n'.join(currentRow))
        self.currentFile.write('\n')
        self.userFile.write('\n'.join(usersRow))
        self.userFile.write('\n')
        self.bidsFile.write('\n'.join(bidsRow))
        self.bidsFile.write('\n')

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
