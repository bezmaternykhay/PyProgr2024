# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume = 1.44
pages_on_book = 100
lines_on_page = 50
symbols_in_line = 25

lines_in_book = pages_on_book * lines_on_page
symbols_in_book = lines_in_book * symbols_in_line
vol_of_book = symbols_in_book * 4
inf_volume_bites = inf_volume * 1024 * 1024
book_on_disk = int(inf_volume_bites // vol_of_book)
print("Количество книг, помещающихся на дискету:", book_on_disk)
