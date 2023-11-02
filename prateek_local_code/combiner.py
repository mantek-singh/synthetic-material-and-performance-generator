from data_provider import DataProvider

dp = DataProvider()

d = dp.get_compound_set()

print({v: 1 for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)})


