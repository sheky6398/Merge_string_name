def pattern():
    for i in range(len(name)):
        if name[i]=="A":
            print_A = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j == 0 and i != 0 or j == 4 and i != 0 or i == 0 and j != 0 and j != 4 or i == 2):
                        print_A[i][j] = "*"
            list2.append(print_A)
        elif name[i]=="B":
            print_B = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (
                            j == 0 or i == 0 and j != 4 or i == 2 and j != 4 or i == 4 and j != 4 or i == 1 and j == 4 or i == 3 and j == 4):
                        print_B[i][j] = "*"
            list2.append(print_B)
        elif name[i]=="C":
            print_C = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 and i!=0 and i!=4 or i==0 and j!=0 or i==4 and j!=0):
                        print_C[i][j] = "*"
            list2.append(print_C)
        elif name[i]=="D":
            print_D = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or i==0 and j!=4 or i==4 and j!=4 or j==4 and i!=0 and i!=4):
                        print_D[i][j] = "*"
            list2.append(print_D)
        elif name[i]=="E":
            print_E = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==0 and j!=0 or i==2 and j!=0 and j!=4 or i==4 and j!=0 or i==1 and j==0 or i==3 and j==0):
                        print_E[i][j] = "*"

            list2.append(print_E)
        elif name[i]=="F":
            print_F = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or i==0 or i==2 and j!=3 and j!=4):
                        print_F[i][j] = "*"
            list2.append(print_F)

        elif name[i]=="G":
            print_G = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 and i!=0 and i!=4 or i==0 and j!=0 or i==4 and j!=0 or j==4 and i!=1 or i==2 and j==3):
                        print_G[i][j] = "*"
            list2.append(print_G)

        elif name[i]=="H":
            print_H = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or j==4 or i==2):
                        print_H[i][j] = "*"
            list2.append(print_H)
        elif name[i]=="I":
            print_I = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==0 or i==4 or j==2):
                        print_I[i][j] = "*"
            list2.append(print_I)
        elif name[i]=="J":
            print_J = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==0 or j==2 and i!=4 or i==4 and j==1 or i==3 and j==0):
                        print_J[i][j] = "*"
            list2.append(print_J)
        elif name[i] == "K":
            print_K = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or i==1 and j==1 or i==0 and j==2 or i==3 and j==1 or i==4 and j==2 ):
                        print_K[i][j] = "*"
            list2.append(print_K)
        elif name[i] == "L":
            print_L = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or i==4 ):
                        print_L[i][j] = "*"
            list2.append(print_L)
        elif name[i] == "M":
            print_M = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or j==4 or i==1 and j==1 or i==2 and j==2 or i==1 and j==3 ):
                        print_M[i][j] = "*"
            list2.append(print_M)
        elif name[i] == "N":
            print_N = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or j==4 or i==j ):
                        print_N[i][j] = "*"
            list2.append(print_N)
        elif name[i] == "O":
            print_O = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==0 and j!=0 and j!=4 or j==0 and i!=0 and i!=4 or i==4 and j!=0 and j!=4 or j==4 and i!=0 and i!=4 ):
                        print_O[i][j] = "*"
            list2.append(print_O)
        elif name[i] == "P":
            print_P = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or i==0 and j!=4 or i==2 and j!=4 or i==1 and j==4):
                        print_P[i][j] = "*"
            list2.append(print_P)
        elif name[i] == "Q":
            print_Q = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==0 and j!=0 and j!=4 or j==0 and i!=0 and i!=4 or i==4 and j!=0 and j!=4 or j==4 and i!=0 and i!=4 or i==3 and j==3):
                        print_Q[i][j] = "*"
            list2.append(print_Q)
        elif name[i] == "R":
            print_R = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or i==0 and j!=3 and j!=4 or i==2 and j!=3 and j!=4 or i==1 and j==3 or i==3 and j==1 or i==4 and j==2):
                        print_R[i][j] = "*"
            list2.append(print_R)
        elif name[i] == "S":
            print_S = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==0 and j!=0 or i==2 and j!=0 and j!=4 or i==4 and j!=4 or i==3 and j==4 or i==1 and j==0):
                        print_S[i][j] = "*"
            list2.append(print_S)
        elif name[i] == "T":
            print_T = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i == 0  or j==2):
                        print_T[i][j] = "*"
            list2.append(print_T)
        elif name[i] == "U":
            print_U = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 and i!=4 or j==4 and i!=4 or i==4 and j!=0 and j!=4):
                        print_U[i][j] = "*"
            list2.append(print_U)
        elif name[i] == "V":
            print_V = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==j and i<=2 or i==1 and j==3 or i==0 and j==4):
                        print_V[i][j] = "*"
            list2.append(print_V)
        elif name[i] == "W":
            print_W = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (j==0 or j==4 or i==3 and j==1 or i==j and j>=2):
                        print_W[i][j] = "*"
            list2.append(print_W)
        elif name[i] == "X":
            print_X = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==j or i==0 and j==4 or i==1 and j==3 or i==3 and j==1 or i==4 and j==0):
                        print_X[i][j] = "*"
            list2.append(print_X)
        elif name[i] == "Y":
            print_Y = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if (i==j and j<=2 or i==1 and j==3 or i==0 and j==4 or j==2 and i>2 ):
                        print_Y[i][j] = "*"
            list2.append(print_Y)
        elif name[i] == "Z":
            print_Z = [[" " for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if ( i==0 or i==4 or i==1 and j==3 or i==2 and j==2 or i==3 and j==1 ):
                        print_Z[i][j] = "*"
            list2.append(print_Z)

        else:
            print("invalid")

    return list2
name=input("enter your name: ")
list2=[]
list3=pattern()

for i in range(5):
    for j in range(len(list3)):
        print("      ",end="")
        for k in range(5):
            print(list3[j][i][k],end="")
            print(end=" ")
    print()