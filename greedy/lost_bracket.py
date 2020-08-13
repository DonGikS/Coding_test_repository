def main():
    '''
    formular = input()
    if len(formular) > 50:
        return
    tmp_list = []
    a = ''

    check = 0
    for i in formular:
        if i.isdigit():
            a += i
            if check == len(formular)-1:
                tmp_list.append(a)
        else:
            tmp_list.append(a)
            tmp_list.append(i)
            a = ''
        check += 1


    list_num = 0
    minus_check = 0
    modify_list = []
    for i in tmp_list:
        if i == '-':
            if minus_check:
                if i == '-':
                    modify_list.append(')' + i + '(')
                    list_num += 1
                    continue
            else:
                modify_list.append(i+'(')
                minus_check = 1
                list_+'('num += 1
                continue

        if (list_num == len(tmp_list)-1) and minus_check:
            modify_list.append(i + ')')
            break
        modify_list.append(i)
        list_num += 1

    b = ''
    for i in modify_list:
        b += i
    print(eval(b))

    return 0
    '''
    a = input().split('-')
    num = []
    for i in a:
        cnt = 0
        s = i.split('+')
        for j in s:
            cnt += int(j)
        num.append(cnt)
    n = num[0]
    for i in range(1, len(num)):
        n -= num[i]
    print(n)

main()