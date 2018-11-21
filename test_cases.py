import random
import json
import numpy as np


FILE_NAME = "test_cases.json"

def generate_test_samples(num_nodes):
    judgements = {}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            choice = random.choice(['s', 'd'])
            choice = np.random.choice(['s', 'd'], 1, p=[0.9, 0.1])[0]
            judgements["{}-{}".format(i, j)] = choice
    return judgements


def write_to_file(content, filename = 'tmp.txt'):
    with open(filename, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    print "Generating samples...(might take some time)"
    num_samples = 400
    test_cases = {"samples": []}
    for n in range(2,num_samples+2):
        if n%50 == 0:
            print n
        judgements = generate_test_samples(n)
        test_cases["samples"].append(judgements)
    print "Dumping in {}".format(FILE_NAME)
    write_to_file(json.dumps(test_cases), FILE_NAME)
