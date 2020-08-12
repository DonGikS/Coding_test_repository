#beakjoon 7638
def main():
    number_of_man = int(input())
    if number_of_man > 50 or number_of_man < 2:
        return

    human_resource = []
    for i in range(number_of_man):
        a_list = []
        a, b = map(int, input().split(' '))
        if a < 10 or a > 200 or b < 10 or b > 200:
            return
        else:
            a_list.append(a)
            a_list.append(b)
        human_resource.append(a_list)

    rank_list = []
    for j in human_resource:
        h_m = 0
        for i in range(len(human_resource)):
            if (j[0] != human_resource[i][0]) and (j[1] != human_resource[i][1]):
                if(j[0] < human_resource[i][0]) and (j[1] < human_resource[i][1]):
                    h_m += 1
        rank_list.append(h_m+1)

    for i in rank_list:
        print(i, end=' ')

main()
