'''
使用defaultdict实现单词出现次数的映射
'''
import sys
import re
from collections import defaultdict

WORD_RE = re.compile(r'\w+')

index = defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as f:
    for line_no, line in enumerate(f, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            location = (line_no, match.start() + 1)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
