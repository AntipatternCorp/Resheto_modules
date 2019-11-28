def dist_docs(doc_list, user_id_list):
    doc2user = []
    i = 0
    max_i = len(user_id_list)
    for d in doc_list:
        u = user_id_list[i]
        temp = (d, u)
        doc2user.append(temp)
        i = i+1
        if i == max_i:
            i = 0
        u = user_id_list[i]
        temp = (d, u)
        doc2user.append(temp)
    return doc2user