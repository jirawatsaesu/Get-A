f = open('All_book.txt', 'r')

for line in f:
    all_book = [b for b in line.split('\t') if b not in '']
    all_book[-1] = all_book[-1][:-1]
    all_book[2] = float(all_book[2])
    print(all_book)
