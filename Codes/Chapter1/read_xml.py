import pandas as pd 
import xml.etree.ElementTree as ET

def xml_encode(row):
    xmlItem = ['  <record>']

    for field in row.index:
        xmlItem \
            .append(
                '        <field name="{0}">{1}</field>' \
                .format(field, row[field])
            )
    
    xmlItem.append('  </record>')
    return '\n'.join(xmlItem)

def iter_records(records):
    '''
        Generator to iterate through all the records
    '''
    for record in records:
        # temporary dictionary to hold values
        return_dict = {}    

        # iterate through all the fields
        for field in record:
            return_dict[field.attrib['name']] = field.text

        # generate the value
        yield return_dict

def read_xml(xml_tree):
    tree = ET.parse(xml_tree)
    root = tree.getroot()

    return pd.DataFrame(list(iter_records(root)))

# names of files to read from
r_filenameXML = '../../Data/Chapter1/realEstate_trans.xml'

# read the data
with open(r_filenameXML, 'r') as xml_file:
    xml_read = read_xml(xml_file)

# print the first 10 records
print(xml_read.head(10))

