# File: MagicSquare.py
#Description: Creates a magic square of size n, for any odd number n greater than or equal to 3
#Student's Name: Luis Jimenez
#Student's UT EID: laj987
#Partner's Name: N/A
#Partner's UT EID: N/A
#Course Name: CS 313E
#Unique Number: 51335
#Date Created: January 24th 9:56PM
#Date Last Modified: January 26th 3:30PM


def make_square(n):
    
    #Initialize an empty square with values of 0
    magic_square = [[0]*n for i in range(n)]
    
    #Find the central column of the square
    central_column = int((n-1)/2)
    
    #Start algorithm by placing first number at the bottom of the central column (value of 1)
    magic_square[n-1][central_column] = 1
    
    #Set the coordinates of the last-placed item
    i = n-1
    j = central_column
    
    #We need to place numbers 2 through n^2
    for k in range(2, n**2 + 1):
        
        #Check to see if next number (lower and to the right) is NOT in range
        if (i+1 == n  or j+1 == n):
            
            #Next number not in range
            #Check to see if it is lower-right diagonal
            
            if (i+1 == n  and j+1 == n):
                
                #It is lower-right diagonal, so according to algorithm, place the number on top of last-placed item
                magic_square[i-1][j] = k 
                
                #After number is placed, set update coordinates
                i = i-1
                
            else:
                
                #Next number not in range, but not lower right diagonal
                #We need to try to wrap around the corners
                
                #Check if i is out of bounds
                if(i+1 == n):
                    
                    #Check if we can wrap around the corner 
                    if(magic_square[0][j+1] == 0):
                        
                        #Set value by wrapping around corner
                        magic_square[0][j+1] = k
                        
                        #Update coordinates of last-placed item
                        i = 0
                        j = j + 1
                        
                        
                    else:
                        
                        #Cannot wrap, so place above last-placed number
                        magic_square[i-1][j] = k 
                        
                        #Update coordinates
                        i = i - 1
                        
                else:
                    
                    #i is not of bounds, so j must be out of bounds
                    
                    #Check if we can wrap around the corner 
                    if(magic_square[i+1][0] == 0):
                        
                        #Set value by wrapping around corner
                        magic_square[i+1][0] = k
                        
                        #Update coordinates
                        i = i + 1
                        j = 0
                        
                        
                    else:
                        
                        #Square is not empty, place above last-placed item
                        magic_square[i-1][j] = k 
                        
                        #Update coordinates
                        i = i - 1
                        
                        
        else:
            
            #Next number is not out of bounds
            
            #Check if square is empty
            if(magic_square[i+1][j+1] == 0):
                
                #Square is empty, so we can use it
                magic_square[i+1][j+1] = k
                
                #Update coordinates
                i = i + 1
                j = j + 1
                
            else:
                
                #Square is not empty, place above last-placed item
                magic_square[i-1][j] = k
                
                #update coordinates
                i = i - 1
                
    return magic_square


def print_square(magic_square):
    
    #Since figure is a square, the # of cols and rows is the same, so we can set n equal to either one
    n = len(magic_square)
    
    print(" ")
    print("Here is a", n, "x", n, "magic square:")
    print(" ")
    for i in range(n):
        for j in range(n):
            
            #Prints each number and right-justifies it with a width of 3
            print(f'{magic_square[i][j]:>3}', end=' ') 
        print(" ")
        
    print(" ")
            
    
def check_square(magic_square):
    
    n = len(magic_square)
    
    #The variable we will use to check the sum of a particular row
    sum = 0
    
    #We first find the sum of each row, and compare to the value of the sum of the first row 
    for i in range(n):
        for j in range(n):
            sum += magic_square[i][j]
            
            #Check if we have summed the entire row
            if(j == n-1):
                
                #Check if this is the first row
                if(i == 0):
                    
                    #Store value
                    sum_of_first_row = sum
                    sum = 0
                    
                else:
                    #Compare sum of current row to the sum of the first row
                    if(not(sum == sum_of_first_row)):
                        #Sum is not valid, magic square is not correct. Failure at row i
                        print("Error: Not a magic square. Failure at row", i)
                        exit()
                    else:
                        #Sum is valid, reset sum variable
                        sum = 0
    
    
                    
    #Rows are okay, let's print value
    print("Sum of row:", sum_of_first_row)
    
    #We now check columns
    #We first find the sum of each column, and compare to the value of the sum of the first column 
    
    for j in range(n):
        for i in range(n):
            sum += magic_square[i][j]
            
            #Check if we have summed the entire column
            if(i == n-1):
                
                #Check if this is the first column
                if(j == 0):
                    
                    #Store value
                    sum_of_first_column = sum
                    sum = 0
                    
                else:
                    #Compare sum of current column to the sum of the first column
                    if(not(sum == sum_of_first_column)):
                        
                        #Sum is not valid, magic square is not correct. Failure at column j
                        print("Error: Not a magic square. Failure at column", j)
                        exit()
                        
                    else:
                        #Sum is valid, reset sum variable
                        sum = 0
                    
    #Columns are okay, let's print value
    print("Sum of column:", sum_of_first_column)
    
    #Check if sum of columns equals sum of rows
    if(not(sum_of_first_row == sum_of_first_column)):
        #Columns don't equal rows
        print("Error, column sum does not match row sum")
        exit()
        
    
    
    sum_diagonal_1 = 0
    sum_diagonal_2 = 0
    
    for i in range(n):
    
        #This is the diagonal that goes from top-left to bottom right
        sum_diagonal_1 += magic_square[i][i]
        
        #This is the diagonal that goes from bottom-left to top-right
        sum_diagonal_2 += magic_square[n-1-i][i]
    
    print("Sum diagonal (UL to LR)", sum_diagonal_1)
    print("Sum diagonal (UR to LL)", sum_diagonal_2)
    
    #Check that values of diagonals are okay
    if(not(sum_diagonal_1 == sum_of_first_row and sum_diagonal_2 == sum_of_first_column)):
        #Sums are not okay, error.
        print("Error, diagonals sum does not match row sum")
        exit()
        
    #The magic square has been verified
    





def main():
    
    #Ask and receive input from user and check if input is odd and bigger than or equal to 3
    print("Enter an odd number bigger than or equal to 3:", end=' ')
    n = int(input())
    is_input_valid = n >= 3 and n % 2 == 1
    
    #While input is not valid, keep asking for input
    while not(is_input_valid):
        print("Enter an odd number bigger than or equal to 3:", end=' ')
        
        #Convert input to integer
        n = int(input())
        is_input_valid = n >= 3 and n % 2 == 1
        
    #Make the magic square
    magic_square = make_square(n)
    
    #Print Magic Square
    print_square(magic_square)
    
    #Verify that magic square is indeed a magic square
    check_square(magic_square)
    

main()
    
    
        
        
