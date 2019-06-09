import json

# db = json.load(open('test.json', 'r'))

# with open('pretty_test.json', 'w') as fout:
#     json.dump(db, fout, sort_keys=True, indent=4)



db = json.load(open('pretty_test.json', 'r'))['list']

for i, times in enumerate(db):
    if i == 1:
        print("{0:.2f}".format(times['main']['temp_max']-273.15))
