def count_c(dic):
    dic_count = {}
    for i in dic:
        dic_count[i] = len(dic[i])

    return dic_count


def getList(cnt):
    dic = {}

    for i in cnt:
        lang, ctry = i.split(':')
        ctry = ctry.split()
        dic[lang] = ctry

    return dic
