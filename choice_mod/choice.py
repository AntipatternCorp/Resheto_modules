from nltk.translate.bleu_score import sentence_bleu
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
    doc = attrs1.id_doc
    score = similarity(attrs1.text, attrs2.text)
#TODO: запросы
    if score > 0.2:
        doc.status = 'yellow'
    if score < 0.15:
        doc.status = 'red'
    if score == 1:
        doc.status = 'green'
        return True
    r1 = attrs1.id_user.rating
    r2 = attrs2.id_user.rating
    if r1 > r2:
        attrs1.status = 1
        attrs1.id_user.rating = r1 + 1
        attrs2.id_user.rating = r2 - 1
        return True
    if r1 < r2:
        attrs2.status = 1
        attrs1.id_user.rating = r1 - 1
        attrs2.id_user.rating = r2 + 1
        return True

    if r1 == r2:
#TODO: переадресация документа
        pass