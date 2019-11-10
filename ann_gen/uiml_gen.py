'''
<?xml version="1.0" encoding="utf-16"?>
<?uimlDocument version="1.0"?>
<Document>
  <Title Value="Даосизм&#xD;Даоси́зм (кит. упр. 道教, пиньинь: dàojiào) — учение о дао или «пути вещей», китайское традиц..." />
  <Text Value="&lt;
  SECTION_TITLE&gt;Даосизм&#xD;Даоси́зм (кит. упр. 道教, пиньинь: dàojiào) — учение о дао или «пути вещей», китайское традиц...&#xD;&#xA;&#xD;&#xA;&lt;/SECTION_TITLE&gt;&#xA;&lt;
  SECTION_TEXT&gt;Даосизм&#xD;&#xA;Даоси́зм (кит. упр. 道教, пиньинь: dàojiào) — учение о дао или «пути вещей», китайское традиционное учение, включающее элементы религии и философии./SECTION_TEXT&gt;" />
  <DBIdentifiers />
  <DocumentRubrics>
    <Rubric Name="Религия" GUID="b358af84-e4b5-4506-ba3b-99b0d6010a23">
      <EtalonAttribute Code="тема" StringValue="РЕЛИГИЯ" />
      <EtalonAttribute Code="тема" StringValue="УЧЕНИЕ" />
      <EtalonAttribute Code="место" StringValue="КИТАЯ" />
    </Rubric>
  </DocumentRubrics>
</Document>
'''
PATH_DOCS = 'C:\Materials_temp\PyProj\Resheto_modules\Results\\'

def one_uiml_gen(collect_name, doc_text, doc_title, attributes, path = PATH_DOCS):
    filename = path + doc_title + '_annotation_' + collect_name + '.uiml'
    uiml_txt = '<?xml version="1.0" encoding="utf-16"?>\n<?uimlDocument version="1.0"?>\n'
    uiml_txt = uiml_txt + '<Document>\n <Title Value=\"' + doc_title + '\" />\n'
    uiml_txt = uiml_txt + ' <Text Value=\"' + doc_text + '\" />\n'
    uiml_txt = uiml_txt + ' <DocumentRubrics>\n <Rubric Name=\"' + collect_name + '\">\n'
    for a_name, a_value in attributes.items():
        uiml_txt = uiml_txt + '   <EtalonAttribute Code=\"'+ str(a_name)+ '\" StringValue=\"' + str(a_value) + '\" />\n'
    uiml_txt = uiml_txt + '  </Rubric>\n </DocumentRubrics>\n</Document>'

    with open(filename, mode="w", encoding="utf8") as f:
        f.write(uiml_txt)
    return True

'''
uiml test
attrs = {'Система': 'Решето', 'Год': 2019, 'Автор': 'Никита'} 
one_uiml_gen('collect_name', 'doc_text', 'doc_title', attrs)
'''
