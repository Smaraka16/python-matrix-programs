def matrixAddition(matrix1,matrix2): #Matrix Addition Logic  
    resultMatrix = []
    for mat1 in range(len(matrix1)): #row
        inner_matrix = []
        for mat2 in range(len(matrix2[0])): #column
            inner_matrix.append(matrix1[mat1][mat2] + matrix2[mat1][mat2])
        resultMatrix.append(inner_matrix)
    return resultMatrix
    
def matrixConstructor(m,n): #Matrix Constructor Logic
    output_matrix = []
    for i in range(m):
        inner_matrix = []
        for j in range(n):
            matrix = int(input('Enter {}{} matrix:'.format([i],[j])))
            inner_matrix.append(matrix)
        output_matrix.append(inner_matrix)
    return output_matrix
    
m = int(input('Enter m matrix: '))
n = int(input('Enter n matrix: '))

print('### Enter Matrix A ###')
matrixA = matrixConstructor(m,n)

print('### Enter Matrix B ###')
matrixB = matrixConstructor(m,n)

print(f'{matrixA} ==> Matrix-A')
print(f'{matrixB} ==> Matrix-B')

print(' [+] Matrix Result')
matrixResult = matrixAddition(matrixA,matrixB)
print(matrixResult)
