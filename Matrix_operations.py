import numpy as np
print("--Welcome to Matrix calculator--")
print('''2X2 order 2
3X3 order 3''')
m=int(input("Enter your Matrix choice(2,3): "))
if m==3:
    print('''1.Addition
2.Subtraction
3.Multiplication''')
    
    n=int(input("Enter your choice(1,2,3) what you gonna do:-->  "))

    row_1=list(map(float,input("Enter row 1 elements for matrix 1 by giving space: ").split()))
    row_2=list(map(float,input("Enter row 2 elements for matrix 1 by giving space: ").split()))
    row_3=list(map(float,input("Enter row 3 elements for matrix 1 by giving space: ").split()))
        
    row_1_1=list(map(float,input("Enter row 1 elements for matrix 2 by giving space: ").split()))
    row_2_2=list(map(float,input("Enter row 2 elements for matrix 2 by giving space: ").split()))
    row_3_3=list(map(float,input("Enter row 3 elements for matrix 2 by giving space: ").split()))

    matrix_1=np.array([row_1,
                      row_2,
                      row_3])
    matrix_2=np.array(row_1_1,
                      row_2_2,
                      row_3_3)
    if n==1:
        print(matrix_1)
        print(matrix_2)
        print(f"Your matrix  addition is this\n{matrix_1+matrix_2}")
    elif n==2:
        print(matrix_1)
        print(matrix_2)
        print(f"Your matrix subtration is this\n{matrix_1-matrix_2}")
    elif n==3:
        print(matrix_1)
        print(matrix_2)
        print(f"Your matrix multiplication is this\n{np.dot(matrix_1,matrix_2)}")
    else:
        print("You type a wrong number")
elif m==2:
    print('''1.Addition
2.Subtraction
3.Multiplication''')
    n=int(input("Enter your choice(1,2,3) what you gonna do:-->  "))
    row_1=list(map(float,input("Enter row 1 elements for matrix 1 by giving space: ").split()))
    row_2=list(map(float,input("Enter row 2 elements for matrix 1 by giving space: ").split()))
        
    row_1_1=list(map(float,input("Enter row 1 elements for matrix 2 by giving space: ").split()))
    row_2_2=list(map(float,input("Enter row 2 elements for matrix 2 by giving space: ").split()))
        
    
        
    matrix_1=np.array([row_1,
                       row_2,])
    matrix_2=np.array([row_1_1,
                       row_2_2])
    if n==1:
        print(matrix_1)
        print(matrix_2)
        print(f"Your matrix addition is this\n{matrix_1+matrix_2}")
    elif n==2:
        print(matrix_1)
        print(matrix_2)
        print(f"Your matrix subtration is this\n{matrix_1-matrix_2}")
    elif n==3:
        print(matrix_1)
        print(matrix_2)
        print(f"Your matrix  multiplication is this\n{np.dot(matrix_1,matrix_2)}")
    else:
        print("You type a wrong number")
else:
    print("You type a worng number: ")
choice=input("Enter any keyword to exit: ")
