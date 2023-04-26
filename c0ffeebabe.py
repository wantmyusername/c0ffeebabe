import argparse
import hashlib
import json
import logging
import random
import re
import time
from calendar
import timegm

DEFAULT_INPUT_FILE = "wordlist.txt"
NUMBER_OF_ITERATIONS = 10000
DISPERSION = 1000000000


def read_file(input_file):
    try:
    with open(input_file, "r") as f:
    return f.readlines()
except FileNotFoundError:
    logging.error("Can't open file {0}".format(input_file))


def get_dictionary(input_file):
    wordlist = read_file(input_file)
logging.info("Read {0} words".format(len(wordlist)))
result = {}
for word in wordlist:
    word = word.rstrip('\n')
word1 = re.sub('^0x', '', word).rstrip('\n')
word2 = word1.lower().rstrip('\n')
result[word] = [word1, word2]
return result


def find_collisions(input_str, output_str, length):
    for i in range(length):
    if output_str.startswith(input_str[i: ]):
    return length - i
return 0


def process(num_iterations, dispersion):
    output = {}
for base_word, word_list in input_words.items():
    for base_str in word_list:
    logging.info("Processing {0}".format(base_str))
for i in range(num_iterations):
    rand_str = str(random.randint(0, dispersion))
input_str = random.choice([
    base_str + rand_str,
    rand_str + base_str + str(random.randint(0, dispersion)),
    rand_str + base_str
])
output_str = hashlib.md5(input_str.encode output_str = hashlib.md5(input_str.encode("utf-8")).hexdigest() collision = find_collisions(input_str, output_str, len(input_str)) * 100.0 / len(input_str) if collision > 50.0:
        output.setdefault(base_word, []).append({
            "input_str": input_str,
            "output_str": output_str,
            "collision": collision
        }) logging.info("Find collision {0}% {1} {2}".format(collision, input_str, output_str)) return output
        if name == 'main':
        parser = argparse.ArgumentParser(description = 'Find hash collisions.') parser.add_argument('-i', '--input',
            default = DEFAULT_INPUT_FILE,
            help = 'input wordlist file (default: {0})'.format(DEFAULT_INPUT_FILE)) parser.add_argument('-n', '--iterations',
            default = NUMBER_OF_ITERATIONS, type = int,
            help = 'number of iterations (default: {0})'.format(NUMBER_OF_ITERATIONS)) parser.add_argument('-d', '--dispersion',
            default = DISPERSION, type = int,
            help = 'dispersion (default: {0})'.format(DISPERSION)) parser.add_argument('-o', '--output', help = 'output file (default: timestamp.json)') args = parser.parse_args()

        logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s', level = logging.INFO)

        input_words = get_dictionary(args.input)

        while True:
        output = process(args.iterations, args.dispersion) if len(output) > 0:
        output_file = args.output or str(timegm(time.gmtime())) + ".json"
        try:
        with open(output_file, "a") as f:
        jdata = json.dumps(output) f.write(jdata) logging.info("Written to {0} {1}".format(output_file, len(jdata))) except PermissionError:
        logging.error("Can't write to file")
        else :
            logging.info("Empty output, may next time be lucky!")
        time.sleep(1)
