



def chufa(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return 'Error, cannot divide by zero!!!'
        if b != 0:
            return a / b
    except Exception as e:
        print(f'Error exist: {e}')
        return e

def gongyue(a,b):
    try:
        if a != int(a) or a <= 0:
            return 'Error, input should be positive int or bigint'
        if b != int(b) or b <= 0:
            return 'Error, input should be positive int or bigint'
        else:
            for i in range(max(a,b),1,-1):
                if a%i == 0 and b%i == 0:
                    print(f'a = {a}, b = {b}, gongyueshu i = {i}')
                    return i
            return 1
    except Exception as e:
        print(e)
        return 'Some invalid input happened!'

def customSort(source):
    result = []
    len1 = len(source)
    print(f'len = {len1}')
    print(f'result = {sorted(source)}')
    for i in source:
        try:
            assert i == int(i)
        except Exception as e:
            print(e)
            return e
    for i in range(0, len1 - 1):
        for j in range(i + 1, len1):
            print(f'i = {i}, j = {j}')
            # print(source[i], source[j])
            if source[i] > source[j]:
                source[i],source[j] = source[j], source[i]
                print(f'i[{i}], j[{j}] switch')
    print(f'result2= {source}')
    return source



def printjiashu(intlist, intDigit):
    res = 0
    for i in intlist:
        try:
            i = int(i)
            intDigit = int(intDigit)
        except Exception as e:
            print(e)
            print('Error happened')
            return
        res = intDigit - i
        for j in intlist:
            if j != i and j == res:
                print(f'Valid result: {i} + {j} = {intDigit}')
                return
        else:
            print(f'No valid result returned for {intDigit}')
            return





if __name__=='__main__':
    # # 除法函数
    # abc = 'abc'
    # print('Hello, give it a try first!')
    # print(f'10/2 = {chufa(10,2)}')
    # print(f'10/0 = {chufa(10, 0)}')
    # print(f'1/2 = {chufa(1, 2)}')
    # print(f'0/2 = {chufa(0, 2)}')
    # print(f'0.1/0.2 = {chufa(0.1, 0.2)}')
    # print(f'abc/0.2 = {chufa(abc, 0.2)}')
    # print(f'0.1/abc = {chufa(0.1, abc)}')

    # # 最大公约数
    # a = 'aabb'
    # b = '!@#'
    # print(f'gongyue(15, 18) = {gongyue(15, 18)}')
    # print(f'gongyue(99, 108) = {gongyue(99, 108)}')
    # print(f'gongyue(16, 2) = {gongyue(16, 2)}')
    # print(f'gongyue(5, 0) = {gongyue(5, 0)}')
    # print(f'gongyue(-1, 17) = {gongyue(-1, 17)}')
    # print(f'gongyue(aabb, 18) = {gongyue(a, 18)}')
    # print(f'gongyue(111, !@#) = {gongyue(111, b)}')


    # # 数组排序
    # '''
    # 列表a和列表为正向有序列表，要求，生成一个新的列表，使a和b中值有序排序
    # '''
    # a = [3, 5, 7, 11, 19, 66]
    # b = [0, 2, 7, 9, 10, 20, 30]
    # a.sort(reverse=True)
    # result = []
    # x = 0
    # for i in a:
    #     for j in b:
    #         if i > j:
    #             result[x] = i
    #             x = x + 1
    #
    # print(a)
    # print(f'a = {a}, b = {b}, sorta = {a.sort()}, sortb = {b.sort()}')

    # # 整数数组排序
    # source = [3,6,5,2,2,6,8,0,11,111,221]
    # customSort(source)

    intlist = [1,2,43,5,6,7,7]
    intDigit = 6
    printjiashu(intlist, intDigit)

    intlist = [1, 2, 43, 5, 6, 7, 7]
    intDigit = 66
    printjiashu(intlist, intDigit)

    intlist = [9, 1, 'a', 43, 5, 6, 7, 7]
    intDigit = 66
    printjiashu(intlist, intDigit)


