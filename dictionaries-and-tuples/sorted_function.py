dict = {'a': -5, 'b': 1, 'c': -4}

# print(sorted(dict.items(), key=lambda item: item[1], reverse=True))

new_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

print(new_dict)

for item in new_dict:
    print(f"{item[0]}: {item[1]}")