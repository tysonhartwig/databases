# skeleton_parser.py 
# Tyson Hartwig
# For: 50:198:451/56:198:551
# python 3
# This parser prepares an xml data file items-*.xml for bulk loading
# into an SQL database.

import datetime
import locale
import sys
import xml.dom.minidom

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

def process_file(filename):
    """
    Process one items-???.xml file.
    """
    
    domItems = xml.dom.minidom.parse(filename) 
    row = []
    # At this point, 'dom' contains a DOM representation of an 'Items'
    # XML file. For example, you can use dom.getElementsByTagName
    # to get specific document elements.
    print domItems.documentElement.nodeType
    print domItems.documentElement.tagName
    print domItems.documentElement.firstChild.data
    for item in domItems.documentElement.childNodes:
    	print item.getAttribute('ItemID')
    category = domItems.getElementsByTagName('Category')
    print category[0].firstChild.data
    print 


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3", sys.argv[0], "[file] [file] ...")

    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    for filename in sys.argv[1:]:
        process_file(filename)

if __name__ == "__main__":
    main()
