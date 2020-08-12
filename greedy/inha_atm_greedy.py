#beakjoon 11399
def main():
    num = int(input())
    if (num < 1) or (num > 1000):
        return
    a_list = list(map(int, input().split()))
    if len(a_list) != num:
        print('what')
        return
    for i in a_list:
        if (i < 1) or (i > 1000):
            print('no')
            return
    a_list.sort()
    sum = 0
    for i in range(len(a_list), 0, -1):
        sum += i * a_list[len(a_list) - i]
    print(sum)

main()
