file = open('FF_tiny.txt')  # 'file' object

year = '1927'  # str, 1927
mktrf_list = []  # empty list

for items in file:  # str, "19260701    0.09    0.22    0.30   0.009\n"
    items = items.strip()  # str, "19260701    0.09    0.22    0.30   0.009"
    split_items = items.split()  # str, ["19260701", "0.09", "0.22", "0.30", "0.009"]
    years = split_items[0]  # str, 19260701
    year_cut = years[0:4]  # str, 1926
    mkt_rf = float(split_items[1])  # float, 0.09
    if year_cut == year:  # bool, True
        mktrf_list.append(mkt_rf)  # list, [0.97, 0.3, 0.0, 0.72]
print(mktrf_list)
