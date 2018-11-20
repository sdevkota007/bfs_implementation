import random
import json
import pickle



FILE_NAME = "test_cases.json"
FILE_NAME_TXT = "test_cases.txt"
FILE_NAME_PICKLE = "test_cases.pickle"

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
    print "Generating 1000 samples..."
    num_samples = 50
    test_cases = {"samples": []}
    for n in range(2,num_samples+2):
        if n%10 == 50:
            print n
        judgements = generate_test_samples(n)
        test_cases["samples"].append(judgements)
    print "Dumping in {}".format(FILE_NAME)
    write_to_file(json.dumps(test_cases), FILE_NAME)

    # write_to_file(str(test_cases), FILE_NAME_TXT)

    # with open(FILE_NAME_PICKLE, "w") as file:
    #     pickle.dump(str(test_cases), file)