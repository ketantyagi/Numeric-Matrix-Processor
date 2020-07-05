class Matrix:
    def dimensions(self,dimension):
        self.dimension = [int(number) for number in dimension.split()]
        self.m = self.dimension[0]
        self.n = self.dimension[1]

    def matrix_element_definition(self):
        self.matrix = []
        for i in range(int(self.m)):
            row = input().split()
            self.matrix.append([])
            for j in range(len(row)):
                self.matrix[i].append(float(row[j]))
        return self.matrix

    def matrix_addition(self, second_matrix):
        if len(self.matrix) != len(second_matrix):
            print('The operation cannot be performed')
            exit()
        matrix_sum = []
        for i in range(int(self.m)):
            matrix_sum.append([])
            for j in range(int(self.n)):
                matrix_sum[i].append(self.matrix[i][j] + second_matrix[i][j])
        print("The result is: ")
        for elements in matrix_sum:
            print(*elements)

    def matrix_scalar_multiplication(self,multiplier):
        scalar_matrix = []
        for i in range(len(self.matrix)):
            scalar_matrix.append([])
            for j in range(int(self.n)):
                scalar_matrix[i].append(self.matrix[i][j] * multiplier)
        print("The result is: ")
        for elements in scalar_matrix:
            print(*elements)

    def matrix_multiplication(self,second_matrix):
        matrix_product = []
        for i in range(int(self.m)):
            matrix_product.append([])
            for j in range(len(second_matrix[0])):
                dot_product = 0
                for k in range(len(second_matrix)):
                    dot_product = round(dot_product + self.matrix[i][k] * second_matrix[k][j], 2)
                matrix_product[i].append(dot_product)
        for elements in matrix_product:
            print(*elements)

    def getmatrixminor(self,m, i, j):
        m = m[:i] + m[i + 1:]
        for k in range(0, len(m)):
            m[k] = m[k][:j] + m[k][j + 1:]
        return m

    def getmatrixdeterminant(self,m):

        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        elif len(m) == 1:
            return m[0][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.getmatrixdeterminant(self.getmatrixminor(m,0,c))
        return determinant

    def matrix_transpose(self,transposition_type):
        if transposition_type == 'Main Diagonal':
            new_matrix = []
            for i in range(int(self.n)):
                new_matrix.append([])
                for j in range(int(self.m)):
                    new_matrix[i].append(self.matrix[j][i])
            for elements in new_matrix:
                print(*elements)
        if transposition_type == 'Side Diagonal':
            new_matrix = []
            for i in range(int(self.m)):
                new_matrix.append([])
                for j in range(int(self.n), 0, - 1):
                    new_matrix[i].append(self.matrix[j - 1][(int(self.n) - 1) - i])
            for elements in new_matrix:
                print(*elements)
        if transposition_type == 'Vertical Line':
            new_matrix = []
            for i in range(int(self.m)):
                new_matrix.append([])
                for j in range(int(self.n)):
                    new_matrix[i].append(self.matrix[i][int(self.n) - 1 - j])
            for elements in new_matrix:
                print(*elements)
        if transposition_type == 'Horizontal Line':
            new_matrix = []
            for i in range(int(self.m)):
                new_matrix.append([])
                for j in range(int(self.n)):
                    new_matrix[i].append(self.matrix[int(self.m) - 1 - i][j])
            for elements in new_matrix:
                print(*elements)


    def getMatrixMinor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def getMatrixDeternminant(m):

        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getmatrixminor(m, 0, c))
        return determinant

    def matrix_inverse(self, m):
        def transposematrix(m):
            new_matrix = []
            for i in range(len(m[0])):
                new_matrix.append([])
                for j in range(len(m)):
                    new_matrix[i].append(m[j][i])
            return new_matrix
        determinant = self.getmatrixdeterminant(m)

        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]


        cofactors = []
        for r in range(len(m)):
            cofactorrow = []
            for c in range(len(m)):
                minor = self.getmatrixminor(m, r, c)
                cofactorrow.append(((-1) ** (r + c)) * self.getmatrixdeterminant(minor))
            cofactors.append(cofactorrow)
        cofactors = transposematrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors



while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    user_choice = int(input())
    if user_choice == 1:
        matrix_one = Matrix()
        print("Enter the size of the first matrix: ")
        matrix_one.dimensions(input())
        print('Enter first matrix')
        matrix_one.matrix_element_definition()
        matrix_two = Matrix()
        print('Enter the size of the second matrix: ')
        matrix_two.dimensions(input())
        print('Enter second matrix:')
        matrix_one.matrix_addition(matrix_two.matrix_element_definition())

    elif user_choice == 2:
        matrix = Matrix()
        print('Enter the size of the matrix: ')
        matrix.dimensions(input())
        print('Enter matrix: ')
        matrix.matrix_element_definition()
        scalar_number = int(input('Enter constant: '))
        matrix.matrix_scalar_multiplication(scalar_number)

    elif user_choice == 3:
        matrix_one = Matrix()
        print("Enter the size of the first matrix: ")
        matrix_one.dimensions(input())
        print('Enter first matrix')
        matrix_one.matrix_element_definition()
        matrix_two = Matrix()
        print('Enter the size of the second matrix: ')
        matrix_two.dimensions(input())
        print('Enter second matrix:')
        matrix_one.matrix_multiplication(matrix_two.matrix_element_definition())

    elif user_choice == 4:
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        print('0. Exit')
        user_choice = int(input())

        if user_choice == 0:
            continue

        elif user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 4:
            matrix = Matrix()
            print('Enter the size of the matrix: ')
            matrix.dimensions(input())
            print('Enter matrix: ')
            matrix.matrix_element_definition()
            if user_choice == 1:
                matrix.matrix_transpose('Main Diagonal')
            if user_choice == 2:
                matrix.matrix_transpose('Side Diagonal')
            if user_choice == 3:
                matrix.matrix_transpose('Vertical Line')
            if user_choice == 4:
                matrix.matrix_transpose('Horizontal Line')

    elif user_choice == 5:
        matrix = Matrix()
        print('Enter the size of the matrix: ')
        matrix.dimensions(input())
        print('Enter matrix: ')
        b = matrix.matrix_element_definition()
        print(matrix.getmatrixdeterminant(b))

    elif user_choice == 6:
        matrix = Matrix()
        print('Enter the size of the matrix: ')
        matrix.dimensions(input())
        print('Enter matrix: ')
        b = matrix.matrix_element_definition()
        inverted_matrix = matrix.matrix_inverse(b)
        for elements in inverted_matrix:
            print(*elements)

    elif user_choice == 0:
        exit()