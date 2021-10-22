import xml.etree.ElementTree as et
import sqlite3
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
rootname = root.tag
connection = sqlite3.connect('{}'.format(rootname))
cursor = connection.cursor()
for child in root:
    creation_tab = '''CREATE TABLE {} (name TEXT, price TEXT);'''.format(child.tag)
    cursor.execute(creation_tab)
    for gc in child:
        creation_name = '''INSERT INTO {} VALUES (\"{}\", \"{}\");'''.format(child.tag, gc.text, gc.attrib['price'])
        cursor.execute(creation_name)

connection.commit()
cursor.close()
connection.close()