import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll

# Bolcek: 183892@vutbr.cz

def ex_1():
    
    for i in range(6):
        print("x"*i)
    
    for i in range(6):
        print("x"*(6-i))

def ex_2(input_string):

    img_arr = []
    for c in input_str:
        try:
            num = float(c)
            img_arr.append(num)
        except:
            continue

    return sum(img_arr)

def num_to_bin(num=0):

    x = num
    out_bin = []
    while True:
        if x == 0:
            break
        out_bin.append(x % 2)
        x = x // 2

    return '0x' + ''.join(map(str, out_bin[::-1]))

def fibonaci(x):
    
    out_fib = []
    for i in range(x + 1):
        if (i == 0) or (i == 1):
            out_fib.append(i)
            continue

        out_fib.append(out_fib[i - 2] + out_fib[i - 1])
    
    return out_fib

def display_as_digi(input_number: int) -> None:

    num_to_str = str(input_number)
    dict1 = {
        '0' : ('###','# #','# #','# #','###'),
        '1' : (' ##','###',' ##',' ##',' ##'),
        '2' : ('###','  #','###','#  ','###'),
        '3' : ('###','  #','###','  #','###'),
        '4' : ('# #','# #','###','  #','  #'),
        '5' : ('###','#  ','###','  #','###'),
        '6' : ('###','#  ','###','# #','###'),
        '7' : ('###','  #','  #','  #','  #'),
        '8' : ('###','# #','###','# #','###'),
        '9' : ('###','# #','###','  #','###'),
        '.' : (' ', ' ', ' ', ' ', '#')
    }
    nums = []
    for row in range(len(dict1['0'])):
        print(" ".join(dict1[i][row] for i in num_to_str))

def zero_digits(input_array, treshold=10):

    input_array[input_array < treshold] = 0

    return input_array

def zero_digit_loop(input_array, treshold=10):

    out_arr = np.empty(input_array.shape)

    for i, row in enumerate(input_array):
        row_ed = row
        for index, number in enumerate(row):
            if number < treshold:
                row_ed[index] = 0

        out_arr[i] = np.array(row_ed, dtype=np.uint8)

    return out_arr

def display_as_digi_plt(number):

    numbers = [int(x) for x in str(number)]
    width, height = 1, 1
    digits = np.array([
        [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 1], [1, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1]]
    ], dtype=np.uint8)
    chosen_digits = [digits[number] for number in numbers]

    fig = plt.figure
    ax = plt.subplot(111, aspect='equal')
    pat = []

    for num_index, digit in enumerate(chosen_digits):
        for y_index, row in enumerate(digit[::-1]):
            print(row)
            for x_index, px in enumerate(row):
                if px != 0:
                    sq = patches.Rectangle((x_index + 4*num_index, y_index), width, height, fill=True)
                    print(x_index, y_index)
                    ax.add_patch(sq)

    pc = coll.PatchCollection(pat)
    ax.add_collection(pc)
    ax.relim()
    ax.autoscale_view()

    plt.axis('off')
    plt.show() 
    
if __name__ == '__main__':
    ## Exercise 1.1
    print("\n Ex 1.1 \n")
    ex_1()

    ## Exercise 1.2
    print("\n Ex 1.2 \n")

    input_str = "n45as29@#8ss6"
    sum_nums = ex_2(input_string=input_str)
    print(sum_nums)

    ## Exercise 1.3
    print("\n Ex 1.3 \n")

    bin_num = num_to_bin(10)
    print(bin_num)

    ## Exercise 1.4
    print("\n Ex 1.4 \n")

    print(fibonaci(10)) 

    ## Exercise 1.5
    print("\n Ex 1.5 \n")

    digits = display_as_digi(5.8795)

    ## Exercise 2
    # 2.1
    print("\n Ex 2.1 \n")

    array = np.random.randint(0, 25, size=[5, 5])

    start = time.time()
    array_zer = zero_digits(array)
    end = time.time()
    print(f"Total time {(end - start):.16f} using numpy only")
    print(array_zer)

    start = time.time()
    array_zer = zero_digit_loop(array)
    end = time.time()
    print(f"Total time {(end - start):.16f} using loops")


    print(array_zer)

    # 2.2
    print("\n Ex 2.2 \n")

    display_as_digi_plt(1234567890)

    # 2.3
    print("\n Ex 2.3 \n")


    


