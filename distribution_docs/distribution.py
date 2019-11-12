from queries import set_all_where, insert_data

def distrib_docs(rubric_name, user_id_list):
    doc_list = set_all_where(table_name= 'documents', field= 'id_doc', key_field='rubric', key= str(rubric_name), type_comparison= '=')
    i = 0
    max_i = len(user_id_list)
    for d in doc_list:
        rel = '\'' + str(user_id_list[i]) + '\',  \'' + str(d) + '\',  \'' + 'executor'
        insert_data(table_name = 'relation', data = rel)
        i = i + 1
        if i == max_i:
            i = 0
        rel = '\'' + str(user_id_list[i]) + '\',  \'' + str(d) + '\',  \'' + 'executor'
        insert_data(table_name='relation', data=rel)
    return True