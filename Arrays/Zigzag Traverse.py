def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    row, col = 0, 0
    isGoingDown = True
    result = []
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if isGoingDown:
            if col == 0 or row == height:
                isGoingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if col == width or row == 0:
                isGoingDown = True
                if col == width:
                    row += 1
                else: 
                    col += 1
            else:
                row -= 1
                col += 1
    return result

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width

array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
print zigzagTraverse(array)