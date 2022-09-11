import re
import random
import pickle


class Text_Gen:
    def fit(self, dirinput, filePath):
        file = open(dirinput, 'r', encoding='utf-8')
        stroke = file.read()
        stroke = re.sub(r'[^А-Яа-я\s]+', '', stroke)
        stroke = stroke.lower()
        bidict = {}
        strList = stroke.split()
        for i in range(len(strList) - 1):
            if strList[i] in bidict:
                bidict[strList[i]].append(strList[i + 1])
            else:
                bidict[strList[i]] = []
                bidict[strList[i]].append(strList[i + 1])

        file.close()
        with open(filePath, 'wb') as f:
            pickle.dump(bidict, f)
        f.close()

    def generate(self, filePath, args_length, args_prefix):
        with open(filePath, 'rb') as f:
            model = pickle.load(f)
        f.close()
        if args_prefix == 1:
            currWord = random.choice(list(model.keys()))
        else:
            currWord = args_prefix
            currWord = currWord.lower()
        length = int(args_length)
        result = [currWord]
        for i in range(length - 1):
            nextWord = random.choice(model[currWord])
            currWord = nextWord
            result.append(nextWord)
        return result
