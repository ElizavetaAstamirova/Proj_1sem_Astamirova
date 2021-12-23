# В магазинах имеются следующие товары.
# Магнит-молоко, соль, сахар.
# Пятерочка-мясо, молоко, сыр.
# Перекресток-молоко, творог, сыр, сахар.
# Определить:
# 1. полный список товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каих магазинах можно приобрести сахар.

Magnit = {'молоко', 'соль', 'сахар'}
Pyaterochka = {'мясо', 'молоко', 'сыр'}
Perekryostok = {'молоко', 'творог', 'сыр', 'сахар'}

print('товары в магазине Magnit:'','.join(Magnit))
print('товары в магазине Pyaterochka:'','.join(Pyaterochka))
print('товары в магазине Perekryostok:'','.join(Perekryostok))

print('полный список товаров:'','.join(Magnit | Pyaterochka | Perekryostok))

Syr = {'сыр'}
if Syr & Magnit == set():
    pass
else:
    print('сыр есть в наличии в магазине Magnit')

if Syr & Pyaterochka == set():
    pass
else:
    print('сыр есть в наличии в магазине Pyaterochka')

if Syr & Perekryostok == set():
    pass
else:
    print('сыр есть в наличии в магазине Perekryostok')

Moloko = {'молоко'}
if Moloko & Magnit == set():
    pass
else:
    print('молоко есть в наличии в магазине Magnit')

if Moloko & Pyaterochka == set():
    pass
else:
    print('молоко есть в наличии в магазине Pyaterochka')

if Moloko & Perekryostok == set():
    pass
else:
    print('молоко есть в наличии в магазине Perekryostok')

Sahar = {'сахар'}
if Sahar & Magnit == set():
    pass
else:
    print('сахар есть в наличии в магазине Magnit')

if Sahar & Pyaterochka == set():
    pass
else:
    print('сахар есть в наличии в магазине Pyaterochka')

if Sahar & Perekryostok == set():
    pass
else:
    print('сахар есть в наличии в магазине Perekryostok')
