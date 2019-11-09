from xml.dom import minidom

'''
<?xml version="1.0" encoding="UTF-8"?>
<collection>
<collect_name></collect_name>
<documents_list>
    <document1>
        <doc_name></doc_name>
        <attr1></attr1>
        <attr2></attr2>
    </document1>
<>...</>
</documents_list>
</collection>
'''

def big_xml_gen(collect_name, documents, attributes):
    filename = collect_name + '_annotation.xml'
    doc_xml = minidom.Document()

    root = doc_xml.createElement('collection')
    doc_xml.appendChild(root)

    name = doc_xml.createElement('collect_name')
    text = doc_xml.createTextNode(str(collect_name))
    name.appendChild(text)
    root.appendChild(name)

    # leaf_cdata = doc.createElement('leaf_cdata')
    # cdata = doc.createCDATASection('<em>CData</em> can contain <strong>HTML tags</strong> without encoding')
    # leaf_cdata.appendChild(cdata)
    # root.appendChild(leaf_cdata)

    doc_list = doc_xml.createElement('documents_list')
    i = 1
    for d_name in documents:
        doc=doc_xml.createElement('document'+str(i))
        doc_name = doc_xml.createElement('doc_name')
        doc_name_text = doc_xml.createTextNode(str(d_name))
        doc_name.appendChild(doc_name_text)
        doc.appendChild(doc_name)
        for a_name, a_value in attributes[i-1].items():
            attr = doc_xml.createElement(str(a_name))
            val_attr = doc_xml.createTextNode(str(a_value))
            attr.appendChild(val_attr)
            doc.appendChild(attr)
        doc_list.appendChild(doc)
        i = i + 1

    root.appendChild(doc_list)
    xml_str = doc_xml.toprettyxml(indent="  ")
    with open(filename, mode="w", encoding="utf8") as f:
        f.write(xml_str)
    return True

'''
xml test
docs = ['doc.txt', 'doc1.txt', 'doc2.txt']
attrs = [{'A1': 'Решето', 'A2': 20, 'A3': 19}, {'A4': 'АИС', 'A5': 22, 'A9': 101}, {'A6': ' ', 'A7': 'семь'}] 
xml_gen('collect_test', docs, attrs)
'''
