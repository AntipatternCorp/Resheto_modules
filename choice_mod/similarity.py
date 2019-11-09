from nltk.translate.bleu_score import sentence_bleu

#attrs_text1 = 'имя = Иванов место = Москва организация = КПСС'
#attrs_text2 = 'имя = Иванов место = Москва организация = КПРФ'
#similarity(attrs_text1,attrs_text2)

def similarity(attrs_text1, attrs_text2): # подсчет похожести по BLEU
    attrs1 = []
    attrs1.append(attrs_text1.split(' '))
    attrs2 = attrs_text2.split(' ')
    score = sentence_bleu(attrs1, attrs2)
    return score