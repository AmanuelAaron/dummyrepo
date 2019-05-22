import os
import json

REPO_PATH = "/Users/aamanuel/sandbox/testflask/dummyrepo"

products = []
aliases = []

for filename in os.listdir('./products'):
    with open(filename, 'r') as f:
        p = json.load(f)
        products.append(p)

for filename in os.listdir('./aliases'):
    with open(filename, 'r') as f:
        p = json.load(f)
        aliases.append(p)

main_json = {
    "products" : products,
    "aliases" : aliases
}

with open(REPO_PATH + '/test.json', 'w') as f:
    json.dump(main_json, f, indent=4)