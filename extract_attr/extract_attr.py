from queries import insert_data
import datetime

def extract_attr(id_user, id_doc, attributes, status = 0, descript = str(datetime.datetime)):
    text = ''
    for a_name, a_value in attributes.items():
        text = text + str(a_name) +' = ' + str(a_value) + ', '
    temp = '\'' + str(id_user) + '\', \'' + str(id_doc) + '\', \'' + text + '\', \'' + descript + '\', \'' + status + '\''
    insert_data(table_name='attributes', data= temp)
    return True