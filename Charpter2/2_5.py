if __name__ == '__main__':

    symbols = '&%*$@'
    lcom = [ord(x) for x in symbols]
    print(lcom)
    generator = (ord(x) for x in symbols)
    print(generator)
    print(tuple(generator))
    print(tuple(ord(x) for x in symbols))  # 如果生成器表达式是函数唯一的参数，可以不用套上小括号直接写

    hund_hund = ((x, y) for x in range(1000)
                 for y in range(1000))  # 当数据量巨大时，列表生成式就难以维持正常了
    print(hund_hund)
    for x in hund_hund:
        print(x)