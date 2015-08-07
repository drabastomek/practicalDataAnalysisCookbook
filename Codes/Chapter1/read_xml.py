import pandas as pd 
import xml.etree.ElementTree as ET

def read_xml(xmlFileName):
    '''
        Read an XML encoded data and return pd.DataFrame
    '''
    with open(xmlFileName, 'r') as xml_file:
        # read the data and store it as a tree
        tree = ET.parse(xml_file)

        # get the root of the tree as this is the starting point
        root = tree.getroot()

        # return the DataFrame
        return pd.DataFrame(list(iter_records(root)))

def iter_records(records):
    '''
        Generator to iterate through all the records
    '''
    for record in records:
        # temporary dictionary to hold values
        temp_dict = {}    

        # iterate through all the fields
        for var in record:
            temp_dict[var \
                .attrib['var_name']
            ] = var.text

        # generate the value
        yield temp_dict

def write_xml(xmlFileName, data):
    '''
        Save the data in an XML format
    '''
    # open the file for writing
    with open(xmlFileName, 'w') as xmlFile:

        # write the headers
        xmlFile.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
        )

        xmlFile.write('<records>\n')

        # write the data
        xmlFile.write(
            '\n'.join(data.apply(xml_encode, axis=1))
        )

        # write the footer
        xmlFile.write('\n</records>')

def xml_encode(row):
    '''
        Encode the row as an XML with a specific hierarchy
    '''
    # first -- we are writing a record
    xmlItem = ['  <record>']

    # next -- for each field in the row we create a XML markup
    #         in a <field name=...>...</field> format
    for field in row.index:
        xmlItem \
            .append(
                '  <var var_name="{0}">{1}</var>' \
                .format(field, row[field])
            )
    
    # last -- this marks the end of the record
    xmlItem.append('  </record>')

    # return a string back to the calling method
    return '\n'.join(xmlItem)

# names of files to read from and write to
r_filenameXML = '../../Data/Chapter1/realEstate_trans.xml'
w_filenameXML = '../../Data/Chapter1/realEstate_trans.xml'

# read the data
xml_read = read_xml(r_filenameXML)

# print the first 10 records
print(xml_read.head(10))

# write back to the file in an XML format
write_xml(w_filenameXML, xml_read)
