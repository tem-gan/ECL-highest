import argparse
import json
import sys

# O(nlogn) time complexity O(n) space complexity

'''
Handle command line arguments
'''
parser = argparse.ArgumentParser(prog='ecl-highest.py',
                                 description='N highest record. ')
parser.add_argument('filename', 
                    metavar='file')
parser.add_argument('nhighest',
                    type=int)
args = parser.parse_args()


# Checking if file exists
try:
    input_file = open(args.filename)
except IOError:
    print('File not found!')
    sys.exit(1)

# Fetch {score} and {id} into a list
mylines=[]
with input_file:
    for line in input_file:
        if not line.strip():
            continue
        else:
            spliter=line.partition(':')
            score=spliter[0]
            try:
                int(score)
                id=json.loads(spliter[2])["id"]
            except (KeyError, json.decoder.JSONDecodeError, ValueError):
                print("Input data not valid!")
                sys.exit(2)
            mylines.append([score, id])
            input_file.closed


# Sort scores in descending order
mylines.sort(reverse=True)

# N highest score into dictionary list
json_list=[]
for i in range(args.nhighest):
    dict={
        "score":mylines[i][0],
        "id":mylines[i][1]
    }
    json_list.append(dict)
json_result=json.dumps(json_list,  indent=4)+'\n'
sys.stdout.write(json_result)
sys.exit(0)