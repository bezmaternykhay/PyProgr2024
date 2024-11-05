def product_search(arr, product):
    length_list = len(arr)
    product_index = None
    for iter in range(length_list):
        if arr[iter] == product:
            if product_index == None:
                product_index = iter
    return product_index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = product_search(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
