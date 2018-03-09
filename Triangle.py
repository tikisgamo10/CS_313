# File: Triangle.py
#Description: Calculate the maximum path sum of a triangle
#Student's Name: Luis Jimenez
#Student's UT EID: laj987
#Partner's Name: N/A
#Partner's UT EID: N/A
#Course Name: CS 313E
#Unique Number: 51335
#Date Created: March 7th 10:08AM
#Date Last Modified: March 8th 8:15PM

import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    #Max sum will be stored as the first element of a list
    #This way it will be mutable from inside exhaustive_search_helper function
    max_sum = []
    max_sum.append(0)
    exhaustive_search_helper(grid, 0, 0, 0, max_sum)
    return max_sum[0]


def exhaustive_search_helper(grid, i, j, sum, max_sum):
    #Add the value of current element to the previous sum
    sum = sum + int(grid[i][j])

    #Checks if we reached the bottom of the triangle
    if( i == len(grid) - 1):
        #If this path's sum is greater than max_sum then set max_sum to the sum of this path
        if(sum > max_sum[0]):
            max_sum[0] = sum

    else:
        #We haven't reached the bottom of the triangle
        #Recurse by calling the function on the two possible paths, i.e. straight down and diagonally below and to the right
        exhaustive_search_helper(grid, i+1, j, sum, max_sum)
        exhaustive_search_helper(grid, i+1, j+1, sum, max_sum)


# returns the greatest path sum using greedy approach
def greedy (grid):
    return greedy_helper(grid, 0, 0, 0)


def greedy_helper(grid, i, j, sum):
    #Add the value of current element to the previous sum
    sum = sum + int(grid[i][j])

    if(i < len(grid) - 1):

        #We now determine the bigger of two numbers below our current position
        #if grid[i+1][j+1] > grid[i+1][j] then we want to call our recursive function with a new 'j' of value j + 1
        #else the new 'j' has the same value of the current 'j' and no assignment is needed
        if(grid[i+1][j+1] > grid[i+1][j]):
            j = j + 1

        #Recurse only on the greatest of the two values of the two possible paths
        return greedy_helper(grid, i+1, j, sum)

    else:
        return sum




# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
    return rec_search_helper(grid, 0, 0)

def rec_search_helper(grid, i, j):
    #Checks if we haven't reach the bottom of the triangle
    if(i < len(grid) - 1):
        #Find the sum of the path of the two triangles that formed with the two elements below are current one as their top
        sum_1 = int(rec_search_helper(grid, i+1, j))
        sum_2 = int(rec_search_helper(grid, i+1, j+1))

        #return the greater of the two sums found plus yourself
        if(sum_1 > sum_2):
            return sum_1 + int(grid[i][j])
        else:
            return sum_2 + int(grid[i][j])
    else:
        #We have reached the bottom of the triangle, so just return the value of the current element
        return int(grid[i][j])

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    num_rows = len(grid)
    new_grid = grid

    #The dynamic programming helper will start percolating the triangle at the second to the last row
    #This is because the last row will be left intact, as there is nothing below to percolate with
    #Hence we call it with an initial parameter of num_rows - 2
    return dynamic_prog_helper(new_grid, num_rows - 2)

def dynamic_prog_helper(grid, current_row):
    #Check that current row is still valid
    if(current_row >= 0):

        #For every element in our current row, check which of the two percolated sums below is greatest
        #Then add the greatest of the two to the value of the current element and finish percolation by
        #updating current element to be the new percolated sum
        for j in range(len(grid[current_row])):
            sum_1 = int(grid[current_row+1][j])
            sum_2 = int(grid[current_row+1][j+1])
            if(sum_1 > sum_2):
                grid[current_row][j] = sum_1 + int(grid[current_row][j])
            else:
                grid[current_row][j] = sum_2 + int(grid[current_row][j])

        #Finished percolating current row, recurse by calling on the row above
        return dynamic_prog_helper(grid, current_row-1)

    else:
        #We finished percolating the entire triangle, create the required tuple and return it
        tuple = grid[0][0], grid
        return tuple



# reads the file and returns a 2-D list that represents the triangle
def read_file ():

    #Empty list that will become the grid
    triangle_2d_list = []

    #File handler
    triangle_file_input = open('triangle.txt', 'r')

    #Gets first element, which is the number of rows
    num_rows = int(triangle_file_input.readline().strip())

    for i in range(num_rows):

        #Read next line as a list
        triangle_1d_list = triangle_file_input.readline().strip().split(" ")

        #Append row to 2d list
        triangle_2d_list.append(triangle_1d_list)

    #return grid
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
