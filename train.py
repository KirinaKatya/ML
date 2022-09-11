import argparse
import model


parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", dest='dirinput', help="the path to the directory with the collection of documents")
parser.add_argument("--model", dest='model', help="the path to the file where the model is saved")
args = parser.parse_args()
text = model.Text_Gen()
text.fit(args.dirinput, args.model)
