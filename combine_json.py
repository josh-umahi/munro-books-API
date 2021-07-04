# To run file ---> python combine_json.py;

files = [
    "best_of_paperback_fiction.json",
    "best_of_paperback_nonfiction.json",
    "best_of_hardcover_fiction.json",
]

combined = '{\n' + '"bestsellers": [\n'

for file in files:
    with open(file) as fp:
        combined += fp.read() + ',\n'

combined = combined.rstrip(',\n')
combined += '\n]' + '\n}'

with open('db.json', 'w') as fp:
    fp.write(combined)
