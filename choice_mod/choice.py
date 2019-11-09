from nltk.translate.bleu_score import sentence_bleu
from queries import set_field,upd_field
#attrs_text1 = 'имя = Иванов место = Москва организация = КПСС'
#attrs_text2 = 'имя = Иванов место = Москва организация = КПРФ'
#similarity(attrs_text1,attrs_text2)

def similarity(attrs_text1, attrs_text2):
    attrs1 = []
    attrs1.append(attrs_text1.split(' '))
    attrs2 = attrs_text2.split(' ')
    score = sentence_bleu(attrs1, attrs2)
    return score

def choice_attr (attrs1, attrs2):
    #doc = attrs1.id_doc
    doc = set_field (table_name = 'attributes', field = 'id_doc', key_field = 'id_attr', key = str(attrs1))
    #score = similarity(attrs1.text, attrs2.text)
    text1 = set_field(table_name = 'attributes', field = 'attr_text', key_field = 'id_attr', key = str(attrs1))
    text2 = set_field(table_name = 'attributes', field = 'attr_text', key_field = 'id_attr', key = str(attrs2))
    score = similarity(text1, text2)
#TODO: запросы
    if score > 0.2:
        #doc.status = 'yellow'
        upd_field(table_name = 'documents', field = 'status', value = 'yellow', key_field = 'id_doc', key = str(doc))
    if score < 0.15:
        #doc.status = 'red'
        upd_field(table_name='documents', field='status', value='red', key_field='id_doc', key=str(doc))
    if score == 1:
        #doc.status = 'green'
        upd_field(table_name='documents', field='status', value='green', key_field='id_doc', key=str(doc))
        return True

    #r1 = attrs1.id_user.rating
    #r2 = attrs2.id_user.rating

    u1 = set_field (table_name = 'attributes', field = 'id_user', key_field = 'id_attr', key = str(attrs1))
    u2 = set_field (table_name = 'attributes', field = 'id_user', key_field = 'id_attr', key = str(attrs2))
    r1 = int(set_field (table_name = 'users', field = 'rating', key_field = 'id_user', key = str(u1)))
    r2 = int(set_field (table_name = 'users', field = 'rating', key_field = 'id_user', key = str(u2)))
    if r1 > r2:
        #attrs1.status = 1
        upd_field(table_name='attributes', field='status', value='1' , key_field='id_attr', key=str(attrs1))
        #attrs1.id_user.rating = r1 + 1
        upd_field(table_name='users', field='rating', value=str(r1 + 1), key_field = 'id_user', key = str(u1))
        #attrs2.id_user.rating = r2 - 1
        upd_field(table_name='users', field='rating', value=str(r2 - 1), key_field = 'id_user', key = str(u2))
        return True
    if r1 < r2:
        #attrs2.status = 1
        upd_field(table_name='attributes', field='status', value='1', key_field='id_attr', key=str(attrs2))
        #attrs1.id_user.rating = r1 - 1
        upd_field(table_name='users', field='rating', value=str(r1 - 1), key_field='id_user', key=str(u1))
        #attrs2.id_user.rating = r2 + 1
        upd_field(table_name='users', field='rating', value=str(r2 + 1), key_field='id_user', key=str(u2))
        return True

    if r1 == r2:
#TODO: переадресация документа
        pass