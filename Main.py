# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result = matrix[1][2]
# # print(result)

# for row in matrix:
#     # print(row)
#     # for element in row:
        
# # matrix[1][1] = 10
# # print(matrix)

inp_rows = int(input("Enter the amount of rows: "))
inp_columns = int(input("Enter the amount of columns: "))

empty = []
for i in range(inp_rows):
    row = []
    for col in range(inp_columns):
        element = int(input(f"enter element at position({i},{col})"))
        row.append(element)
    empty.append(row)
print(empty)


