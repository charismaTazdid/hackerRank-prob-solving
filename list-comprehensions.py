if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list_x = [_ for _ in range(x+1)]
    list_y = [_ for _ in range(y+1)]
    list_z = [_ for _ in range(z+1)]

    result = [[x_, y_, z_] for x_ in list_x for y_ in list_y for z_ in list_z
            if (x_+y_+z_) != n
    ]

    print(result)


    #problem:  https://www.hackerrank.com/challenges/list-comprehensions/problem
