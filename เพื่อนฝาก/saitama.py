''' Saitama '''

def main():
    ''' print '''
    mission1 = int(input())
    mission2 = int(input())
    mission3 = int(input())
    mission4 = int(input())
    count1 = int(input())
    count2 = int(input())
    count3 = int(input())
    count4 = int(input())
    result1 = mission1/count1
    result2 = mission2/count2
    result3 = mission3/count4
    result4 = mission4/count3
    for _ in range(4):
        if result1 <= result2:
            result1, result2 = result2, result1
        if result2 <= result3:
            result2, result3 = result3, result2
        if result3 <= result4:
            result3, result4 = result4, result3
    print(int(result1))
main()
