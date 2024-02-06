string = input()
pos = string.find('f')
posl = string[::-1]  # строка наоборот для нахождения первого f с конца
kon = len(posl) - posl.find('f') - 1  # вычесть из общей длины
if pos != -1:
    if pos == kon:
        pos = kon
        print(pos)
    elif pos != kon:
        print(pos, kon)
