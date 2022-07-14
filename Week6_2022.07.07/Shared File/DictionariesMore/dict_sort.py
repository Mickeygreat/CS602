import pprint as pp

def my_print(list_of_pairs):
    for p in list_of_pairs:
        print(f"{p[0]:13s} : {p[1]:>10,d}")

d = {"New York City": 8622357,
     "Chicago" : 2670406,
     "Phoenix" : 1743469,
     "Philadelphia" : 1590402,
     "Los Angeles": 4085014,
     "Houston": 2378146}
print('Original dictionary : ')
pp.pprint(d)





print("Another way to sort by ascending value:")
d_population = d.copy()
d_pop_sorted = []
while d_population != {}:
    key_list, val_list = list(d_population.keys()), list(d_population.values())
    min_val = min(val_list)
    position = val_list.index(min_val)
 #   d_pop_sorted.append((key_list[position], val_list[position])) # ascending order
    d_pop_sorted.insert(0,(key_list[position], val_list[position])) # descending order

    d_population.pop(key_list[position])

my_print(d_pop_sorted)
pp.pprint(d)
