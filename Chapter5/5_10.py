'''
* **参数的运用
生成html
'''


def tag(name, *content, cls=None, **attrs):
    '''
    生成一个或多个HTML标签
    '''
    if cls:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(
            f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join(f'<{name}{attr_str}>{c}</{name}>' for c in content)
    else:
        return f'<{name}{attr_str} />'


if __name__ == '__main__':
    print(tag('br'))
    print('-------'*5)
    print(tag('p', 'hello'))
    print('-------'*5)
    print(tag('p','hello','world'))
    print('-------'*5)
    print(tag('p','hello',id='kk',cls='col-sm-12'))