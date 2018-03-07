import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    max_sum = []
    max_sum.append(0)
    exhaustive_search_helper(grid, 0, 0, 0, max_sum)
    return max_sum[0]


def exhaustive_search_helper(grid, i, j, sum, max_sum):
    sum = sum + int(grid[i][j])

    if( i == len(grid) - 1):
        if(sum > max_sum[0]):
            max_sum[0] = sum

    else:
        exhaustive_search_helper(grid, i+1, j, sum, max_sum)
        exhaustive_search_helper(grid, i+1, j+1, sum, max_sum)


# returns the greatest path sum using greedy approach
def greedy (grid):
    return greedy_helper(grid, 0, 0, 0)


def greedy_helper(grid, i, j, sum):
    sum = sum + int(grid[i][j])

    if(i < len(grid) - 1):

        #We now determine the bigger of two numbers below our current position
        #if grid[i+1][j+1] > grid[i+1][j] then we want to call our recursive function with a new 'j' of value j + 1
        #else the new 'j' has the same value of the current 'j' and no assignment is needed
        if(grid[i+1][j+1] > grid[i+1][j]):
            j = j + 1

        return greedy_helper(grid, i+1, j, sum)

    else:
        return sum




# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
    return rec_search_helper(grid, 0, 0)

def rec_search_helper(grid, i, j):
    if(i < len(grid) - 1):
        sum_1 = int(rec_search_helper(grid, i+1, j))
        sum_2 = int(rec_search_helper(grid, i+1, j+1))

        #return the greater of the two sums plus yourself
        if(sum_1 > sum_2):
            return sum_1 + int(grid[i][j])
        else:
            return sum_2 + int(grid[i][j])
    else:
        return int(grid[i][j])

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    num_rows = len(grid)
    new_grid = grid
    return dynamic_prog_helper(new_grid, num_rows - 2)

def dynamic_prog_helper(grid, i):
    if(i >= 0):

        for j in range(i+1):
            sum_1 = int(grid[i+1][j])
            sum_2 = int(grid[i+1][j+1])
            if(sum_1 > sum_2):
                grid[i][j] = sum_1 + int(grid[i][j])
            else:
                grid[i][j] = sum_2 + int(grid[i][j])

        return dynamic_prog_helper(grid, i-1)

    else:

        tuple = grid[0][0], grid
        return tuple



# reads the file and returns a 2-D list that represents the triangle
def read_file ():

    triangle_2d_list = []
    triangle_file_input = open('triangle.txt', 'r')

    num_rows = int(triangle_file_input.readline().strip())

    for i in range(num_rows):

        #Read next line as a list
        triangle_1d_list = triangle_file_input.readline().strip().split(" ")

        #Append row to 2d list
        triangle_2d_list.append(triangle_1d_list)

    return triangle_2d_list

def main ():
    # read triangular grid from file
    grid = read_file()

    ti = time.time()
    exhaustive_search_sum = exhaustive_search(grid)
    print ("The greatest path sum through exhaustive search is", exhaustive_search_sum)

    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive approach
    print("The time taken for exhaustive search is", del_t, "seconds.")

    ti = time.time()
    greedy_sum = greedy(grid)
    print ("The greatest path sum through greedy search is", greedy_sum)
    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach
    print("The time taken for greedy search is", del_t, "seconds.")

    ti = time.time()
    divide_and_conquer_sum = rec_search(grid)
    print ("The greatest path sum through divide-and-conquer search is", divide_and_conquer_sum)
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print("The time taken for divide-and-conquer search is", del_t, "seconds.")

    ti = time.time()
    dynamic_programmin_sum = dynamic_prog(grid)[0]
    print ("The greatest path sum through dynamic programming search is", dynamic_programmin_sum)
    tf = time.time()
    del_t = tf - ti
    print("The time taken for dynamic programming search is", del_t, "seconds.")


if __name__ == "__main__":
    main()
