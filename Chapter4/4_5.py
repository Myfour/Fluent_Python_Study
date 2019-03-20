for codec in ['latin_1', 'utf_8', 'utf-16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')
