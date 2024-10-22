# TODO Найдите количество книг, которое можно разместить на дискете
capacity=1024*1024*1.44
pages = 100
lines = 50
symbols = 25
symbol_weight = 4
max_books = round(capacity/(pages*lines*symbols*symbol_weight))
print("Количество книг, помещающихся на дискету:", max_books)
