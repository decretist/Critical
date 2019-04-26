#!/usr/local/bin/python3
# Paul Evans (paul.evans@aya.yale.edu)
# 22 April 2019 (Easter Monday)
#
# text template for TEI P5 diplomatic edition of Sg case statements
# command-shift-X in Atom to format XML
#
import xml.etree.ElementTree as ET
cases = ['Prima', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '28', '29', '30', '31', '32', '33', '34',
    '35', '36']
def main():
    builder = ET.TreeBuilder()
    builder.start('TEI', {'xmlns': 'http://www.tei-c.org/ns/1.0'})
    builder.start('text')
    builder.start('body')
    builder.start('div', {'type': 'edition', 'xml:id': 'edition-text', 'xml:space': 'preserve'})
    builder.start('div', {'type': 'section', 'subtype': 'part'})
    for case in cases:
        label1 = 'C.' + case # e.g., 'C.Prima'
        label2 = 'C.' + case + ' d.init.' # e.g., 'C.Prima d.init."
        builder.start('div', {'type': 'section', 'subtype': 'case','n': label1})
        builder.start('head')
        builder.data('(' + label1 + ')')
        builder.end('head')
        builder.start('div', {'type': 'textpart', 'subtype': 'dictum', 'n': label2})
        builder.start('head')
        builder.data('(' + label2 + ')')
        builder.end('head')
        builder.start('ab')
        builder.end('ab')
        builder.end('div')
        builder.end('div')
    builder.end('div')
    builder.end('div')
    builder.end('body')
    builder.end('text')
    builder.end('TEI')
    root = builder.close()
    ET.dump(root)

if __name__ == '__main__':
    main()
