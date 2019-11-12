from queries import set_field,upd_field,insert_data, set_all_where, drop_data
from choice_mod import similarity
import random

def choice_attr (attrs1, attrs2): # выбор между 2мя вариантами аттрибутов
    #doc = attrs1.id_doc
    doc = set_field (table_name = 'attributes', field = 'id_doc', key_field = 'id_attr', key = str(attrs1))
    #score = similarity(attrs1.text, attrs2.text)
    text1 = set_field(table_name = 'attributes', field = 'attr_text', key_field = 'id_attr', key = str(attrs1))
    text2 = set_field(table_name = 'attributes', field = 'attr_text', key_field = 'id_attr', key = str(attrs2))
    score = similarity(text1, text2)

    #r1 = attrs1.id_user.rating
    #r2 = attrs2.id_user.rating

    u1 = set_field (table_name = 'attributes', field = 'id_user', key_field = 'id_attr', key = str(attrs1))
    u2 = set_field (table_name = 'attributes', field = 'id_user', key_field = 'id_attr', key = str(attrs2))
    r1 = int(set_field (table_name = 'users', field = 'rating', key_field = 'id_user', key = str(u1)))
    r2 = int(set_field (table_name = 'users', field = 'rating', key_field = 'id_user', key = str(u2)))

#TODO: запросы
    if score > 0.2:
        #doc.status = 'yellow'
        upd_field(table_name = 'documents', field = 'status', value = 'yellow', key_field = 'id_doc', key = str(doc))
    if score < 0.15:
        #doc.status = 'red'
        upd_field(table_name='documents', field='status', value='red', key_field='id_doc', key=str(doc))
    if score == 1:
        #doc.status = 'green'
        upd_field(table_name='documents', field='status', value='green', key_field='id_doc', key=str(doc)) # изменяем статус документа
        upd_field(table_name='users', field='rating', value=str(r1 + 1), key_field='id_user', key=str(u1)) # повышаем рейтинг
        upd_field(table_name='users', field='rating', value=str(r2 + 1), key_field='id_user', key=str(u2))
        upd_field(table_name='attributes', field='status', value='1', key_field='id_attr', key=str(attrs1))# изменяем статус атрибута
        drop_data(table_name='attributes', key_field='id_attr', key=str(attrs2))  # удаляем ненужные атрибуты

        return True

    if r1 > r2:
        #attrs1.status = 1
        upd_field(table_name='attributes', field='status', value='1' , key_field='id_attr', key=str(attrs1))
        #attrs1.id_user.rating = r1 + 1
        upd_field(table_name='users', field='rating', value=str(r1 + 1), key_field = 'id_user', key = str(u1))
        #attrs2.id_user.rating = r2 - 1
        upd_field(table_name='users', field='rating', value=str(r2 - 1), key_field = 'id_user', key = str(u2))# понижаем рейтинг
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
        user_list = set_all_where(table_name='users', field='id_user', key_field = 'rating', key = str(r1), type_comparison = '>')
        if len(user_list) == 0:
            i = random.randint(0,1)
            if i:
                upd_field(table_name='attributes', field='status', value='1', key_field='id_attr', key=str(attrs2))
                upd_field(table_name='users', field='rating', value=str(r1 - 1), key_field='id_user', key=str(u1))
                upd_field(table_name='users', field='rating', value=str(r2 + 1), key_field='id_user', key=str(u2))
            else:
                upd_field(table_name='attributes', field='status', value='1', key_field='id_attr', key=str(attrs1))
                upd_field(table_name='users', field='rating', value=str(r1 + 1), key_field='id_user', key=str(u1))
                upd_field(table_name='users', field='rating', value=str(r2 - 1), key_field='id_user', key=str(u2))
            return True
        i = random.randint(0,len(user_list)-1)
        id_user = user_list[i]
        #пусть будет три типа связи: author, executor, checker
        rel = '\'' + str(id_user) + '\',  \'' + str(doc) + '\',  \'' + 'checker\''
        insert_data(table_name = 'relation', data = rel)
        #добавили задание эксперту с более высоким рейтингом
        #по окончании его работы вызывается функция check

