import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-no1')
parser.add_argument('-no2')
args = parser.parse_args()
print('no1',args.no1)
print('no1',args.no2)