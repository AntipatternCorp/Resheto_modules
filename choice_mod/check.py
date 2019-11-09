from choice_mod import similarity
from queries import set_field,upd_field,set_executors,drop_data

def check (attr): # функция для согласования данных после экспертной оценки неудачного выбора
    upd_field(table_name='attributes', field='status', value='1', key_field='id_attr', key=str(attr))
    doc = set_field(table_name='attributes', field='id_doc', key_field='id_attr', key=str(attr))
    user_list = set_executors(doc)
    attrs = []
    for u in user_list:
        attrs.append(set_field (table_name = 'attributes', field = 'id_attr', key_field = 'id_user', key = str(u)))
    text_right = set_field(table_name='attributes', field='attr_text', key_field='id_attr', key=str(attr))
    texts = []
    for a in attrs:
        texts.append(set_field(table_name = 'attributes', field = 'attr_text', key_field = 'id_attr', key = str(a)))
        drop_data(table_name= 'attributes', key_field= 'id_attr', key = str(a)) #удаляем ненужные атрибуты
    scores = []
    for t in texts:
        scores.append(int(similarity(text_right, t)))
    ms = max(scores)
    if ms > 0.85:
        i = 0
        for s in scores:
            u_temp = user_list[i]
            r_temp = int(set_field(table_name='users', field='rating', key_field='id_user', key=str(u_temp)))
            if s == ms:#повышаем рейтинг тех, кто был ближе всего
                upd_field(table_name='users', field='rating', value=str(r_temp + 1), key_field='id_user', key=str(u_temp))
            else:
                upd_field(table_name='users', field='rating', value=str(r_temp - 1), key_field='id_user', key=str(u_temp))
            i = i+1
    return True