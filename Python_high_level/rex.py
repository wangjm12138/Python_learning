import re


def re_practice():
    """
        match: only return one result, from begin
        search: only return one result, will search till end
        findall: return all results
        fullmatch: equal string compare
    :return:
    """
    s = 'python1234python'
    ret = re.match('python', s)
    print(ret.group())
    print(ret.span())
    s1 = 'python1234'
    ret = re.search('python', s1)
    print(ret.group())
    print(ret.span())
    s2 = 'python1234python'
    ret = re.findall('python', s2)
    print(ret)
    s3 = 'python'
    ret = re.fullmatch('python', s3)
    print(ret.group())

def re_practice2():
    s = 'python 1234'
    ret = re.search('\d{4}', s)
    print(ret.group())
    ret = re.search('[0-9]{4}', s)
    print(ret.group())
    ret = re.search('[a-z]', s)
    print(ret.group())
    ret = re.search('\w', s)
    print(ret.group())
    ret = re.search('\s', s)
    print(ret.span())


def re_practice3():
    s = 'python 1234'
    ret = re.search('^p', s)
    print(ret.group())


if __name__ == '__main__':
    # re_practice()
    re_practice2()