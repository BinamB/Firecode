"""
You're given a 2D board which contains an m x n matrix (2D list of characters). Write a method - print_paths that prints all possible paths from the top left cell to the bottom right cell. Your method should return a list of strings, where each string represents a path with characters appended in the order of movement. You're only allowed to move down and right on the board. The order of string insertion in the list does not matter.
 
Example:

Input Board :      
[
    [A, X],
    [D, E]
]
Output: ["ADE", "AXE"]

"""
def print_paths(board):
    output = []
    temp = []
    search(0, 0, board, temp, output)
    return output
    
def search(i,j,board,temp,output):
    rows = len(board)
    cols = len(board[0])
    if i > rows - 1 or j > cols - 1:
        return
    temp.append(board[i][j])
    if i == rows - 1 and j == cols - 1:
        output.append("".join(temp))
        temp.pop()
        return
    search(i+1, j, board, temp, output)
    search(i, j+1, board, temp, output)
    temp.pop()