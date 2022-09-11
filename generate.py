import argparse
import model

# to start, use the command "python generate.py -h" and then "python generate.py length (--prefix=)"
parser = argparse.ArgumentParser(description='Text generator.')

parser.add_argument("--model", dest='model', help="dir of model", default=1)
parser.add_argument("--length", help="length of the generated string", default=0)
parser.add_argument("--prefix", help="initial word", default=1)
args = parser.parse_args()

text = model.Text_Gen()
result = text.generate(args.model, args.length, args.prefix)
print(*result)
