import random
import json



FILE_NAME = "test_cases.json"

def generate_test_samples(num_nodes):
    judgements = {}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            choice = random.choice(['same', 'different'])
            judgements["{}-{}".format(i, j)] = choice
    return judgements


def write_to_file(content, filename = 'tmp.txt'):
    with open(filename, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    #generating 1000 samples
    num_samples = 10
    test_cases = {"samples": []}
    for n in range(2,num_samples+2):
        judgements = generate_test_samples(n)
        test_cases["samples"].append(judgements)
    print test_cases["samples"]
    write_to_file(json.dumps(test_cases, indent=4), FILE_NAME)