def main():
    # get_sum = lambda x, y: x + y
    # print(get_sum(4, 5))
    li = [7,4,8,9,11,10,-3,-5,0,10]
    result = list(map(lambda x:x**2,li))
    print(f"func map: {result}")
    result = list(filter(lambda x:x%2==0,li))
    print(f"func filter: {result}")
if __name__ == '__main__':
    main()













