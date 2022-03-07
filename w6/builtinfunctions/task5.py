def all_true_tuple(tpl):
    for i in tpl:
        if i:
            continue
        else:
            return False
    return True

tpl1 = (1, True, 1, 'abs')

tpl2 = (1241, True, 'Abzal', 'abs')

tpl3 = (False, 214, True, 'abs')

tpl4 = (True, True, 'abs', 0)

print(all_true_tuple(tpl1))
print(all_true_tuple(tpl2))
print(all_true_tuple(tpl3))
print(all_true_tuple(tpl4))