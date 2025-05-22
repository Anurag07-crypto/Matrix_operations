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
    if n==1:
        row_1=input("Enter row elements for matrix 1 by giving space: ").split()
        row_2=input("Enter row elements for matrix 1 by giving space: ").split()
        row_3=input("Enter row elements for matrix 1 by giving space: ").split()
        
        row_1_1=input("Enter row elements for matrix 2 by giving space: ").split()
        row_2_2=input("Enter row elements for matrix 2 by giving space: ").split()
        row_3_3=input("Enter row elements for matrix 2 by giving space: ").split()
        
        float_row_1 = [float(x) for x in row_1]
        float_row_2 = [float(x) for x in row_2]
        float_row_3 = [float(x) for x in row_3]
        float_row_1_1 = [float(x) for x in row_1_1]
        float_row_2_2= [float(x) for x in row_2_2]
        float_row_3_3= [float(x) for x in row_3_3]
        
        matrix_1=np.array([float_row_1,
                      float_row_2,
                      float_row_3])
        
        matrix_2=np.array([float_row_1_1,
                      float_row_2_2,
                      float_row_3_3])
        
        print(f"Your matrix addition is this\n{matrix_1+matrix_2}")
    elif n==2:
        row_1=input("Enter row elements for matrix 1 by giving space: ").split()
        row_2=input("Enter row elements for matrix 1 by giving space: ").split()
        row_3=input("Enter row elements for matrix 1 by giving space: ").split()
        
        row_1_1=input("Enter row elements for matrix 2 by giving space: ").split()
        row_2_2=input("Enter row elements for matrix 2 by giving space: ").split()
        row_3_3=input("Enter row elements for matrix 2 by giving space: ").split()
        
        float_row_1 = [float(x) for x in row_1]
        float_row_2 = [float(x) for x in row_2]
        float_row_3 = [float(x) for x in row_3]
        
        float_row_1_1 = [float(x) for x in row_1_1]
        float_row_2_2= [float(x) for x in row_2_2]
        float_row_3_3= [float(x) for x in row_3_3]
        
        matrix_1=np.array([float_row_1,
                      float_row_2,
                      float_row_3])
        
        matrix_2=np.array([float_row_1_1,
                      float_row_2_2,
                      float_row_3_3])
        
        print(f"Your matrix subtration is this\n{matrix_1-matrix_2}")
    elif n==3:
        row_1=input("Enter row elements for matrix 1 by giving space: ").split()
        row_2=input("Enter row elements for matrix 1 by giving space: ").split()
        row_3=input("Enter row elements for matrix 1 by giving space: ").split()
        
        row_1_1=input("Enter row elements for matrix 2 by giving space: ").split()
        row_2_2=input("Enter row elements for matrix 2 by giving space: ").split()
        row_3_3=input("Enter row elements for matrix 2 by giving space: ").split()
        
        float_row_1 = [float(x) for x in row_1]
        float_row_2 = [float(x) for x in row_2]
        float_row_3 = [float(x) for x in row_3]
        
        float_row_1_1 = [float(x) for x in row_1_1]
        float_row_2_2= [float(x) for x in row_2_2]
        float_row_3_3= [float(x) for x in row_3_3]
        
        matrix_1=np.array([float_row_1,
                      float_row_2,
                      float_row_3])
        
        matrix_2=np.array([float_row_1_1,
                      float_row_2_2,
                      float_row_3_3])
        
        print(f"Your matrix multiplication is this\n{matrix_1*matrix_2}")
    else:
        print("You type a wrong number")
elif m==2:
    print('''1.Addition
2.Subtraction
3.Multiplication''')
    n=int(input("Enter your choice(1,2,3) what you gonna do:-->  "))
    if n==1:
        row_1=input("Enter row elements for matrix 1 by giving space: ").split()
        row_2=input("Enter row elements for matrix 1 by giving space: ").split()
        
        row_1_1=input("Enter row elements for matrix 2 by giving space: ").split()
        row_2_2=input("Enter row elements for matrix 2 by giving space: ").split()
        
        float_row_1 = [float(x) for x in row_1]
        float_row_2 = [float(x) for x in row_2]
        
        float_row_1_1 = [float(x) for x in row_1_1]
        float_row_2_2= [float(x) for x in row_2_2]
        
        matrix_1=np.array([float_row_1,
                      float_row_2,])
        matrix_2=np.array([float_row_1_1,
                      float_row_2_2])
        print(f"Your matrix addition is this\n{matrix_1+matrix_2}")
    elif n==2:
        row_1=input("Enter row elements for matrix 1 by giving space: ").split()
        row_2=input("Enter row elements for matrix 1 by giving space: ").split()
        
        row_1_1=input("Enter row elements for matrix 2 by giving space: ").split()
        row_2_2=input("Enter row elements for matrix 2 by giving space: ").split()
       
        float_row_1 = [float(x) for x in row_1]
        float_row_2 = [float(x) for x in row_2]
        
        float_row_1_1 = [float(x) for x in row_1_1]
        float_row_2_2= [float(x) for x in row_2_2]
        
        matrix_1=np.array([float_row_1,
                      float_row_2])
        matrix_2=np.array([float_row_1_1,
                      float_row_2_2])
        print(f"Your matrix subtration is this\n{matrix_1-matrix_2}")
    elif n==3:
        row_1=input("Enter row elements for matrix 1 by giving space: ").split()
        row_2=input("Enter row elements for matrix 1 by giving space: ").split()
        
        row_1_1=input("Enter row elements for matrix 2 by giving space: ").split()
        row_2_2=input("Enter row elements for matrix 2 by giving space: ").split()
        
        float_row_1 = [float(x) for x in row_1]
        float_row_2 = [float(x) for x in row_2]
        
        float_row_1_1 = [float(x) for x in row_1_1]
        float_row_2_2= [float(x) for x in row_2_2]

        matrix_1=np.array([float_row_1,
                      float_row_2])
        matrix_2=np.array([float_row_1_1,
                      float_row_2_2])
        print(f"Your matrix multiplication is this\n{matrix_1*matrix_2}")
    else:
        print("You type a wrong number")
else:
    print("You type a worng number: ")
choice=input("Enter any keyword to exit: ")