def even_file(i, list_to_compare):
    with open("F:\HW\Pytnon_unversity\_g", 'a', encoding='utf-8') as g:
        g.write(list_to_compare[i])


def not_even_file(i, list_to_compare):
    with open("F:\HW\Pytnon_unversity\_h", 'a', encoding='utf-8') as h:
        h.write(list_to_compare[i])


def begin():
    with open("F:\HW\Pytnon_unversity\_f", 'r', encoding='utf-8') as f:
        list_f = list(f.read().split(' '))
        for i in range(len(list_f)):
            if int(list_f[i]) % 2 == 0:
                even_file(i, list_f)
            else:
                not_even_file(i, list_f)


begin()
