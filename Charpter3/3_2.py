# 创建一个从单词到其出现情况的映射
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        # print(line_no, line)
        for match in WORD_RE.finditer(line):
            # print(match)
            word = match.group()
            # print(word)
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences=index.get(word,[])
            occurrences.append(location)
            index[word]=occurrences
            # print(index.setdefault(word,[]).append(location))

for word in sorted(index, key=str.upper):
    print(word, index[word])
