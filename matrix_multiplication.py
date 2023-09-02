#raise custom exception
class CustomError(Exception):
    def __init__(self,message):
        super().__init__(message)

''' Matrix Multiplication '''

def matrixMultiplication(matrix1,matrix2):
    try:
        if len(matrix1[0]) == len(matrix2):
            res_arr = []
            for mat1 in range(len(matrix1)):
                inner_arr = []
                if len(matrix1[0])<len(matrix2):
                    for mat2 in range(len(matrix1[0])):
                        sum1 = 0
                        for mat3 in range(len(matrix2)):
                            sum1+=matrix1[mat1][mat3] * matrix2[mat3][mat2]
                        inner_arr.append(sum1) 
                    res_arr.append(inner_arr) 
                else:
                    for mat2 in range(len(matrix2[0])):
                        sum1 = 0
                        for mat3 in range(len(matrix2)):
                            sum1+=matrix1[mat1][mat3] * matrix2[mat3][mat2]
                        inner_arr.append(sum1) 
                    res_arr.append(inner_arr)
            return res_arr  
        raise CustomError('Number of Columns in matrix-A & Number of row in matrix-B should be equal !')
    except CustomError as err:
        return err

'''Matrix Constructor Method'''
def matrixConstructor(rows,columns):
    outer_arr = []
    for row in range(rows):
        inner_arr = []
        for column in range(columns):
            arr = int(input('Enter matrix {}{}: '.format([row],[column])))
            inner_arr.append(arr)
        outer_arr.append(inner_arr)
    return outer_arr

'''Getting User Input Matrix'''
def matrixuserInput(matrixName):
    print('[+] {}'.format(matrixName))
    m = int(input('Enter Number Of Rows: '))
    n = int(input('Enter Number Of Columns: '))
    return matrixConstructor(m,n)
    
#matrix A
matrixA = matrixuserInput('matrix-A')
print(matrixA)

#matrixB
matrixB = matrixuserInput('matrix-B')
print(matrixB)

#matrix multiplicator
resultMatrix = matrixMultiplication(matrixA,matrixB)
print(resultMatrix,'resultmatrix')
