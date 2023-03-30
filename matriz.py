# hacer una matriz nxn con nodos y una lista enlzada
# para cada nodo
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        current = self.head
        total = 0
        while current:
            total += 1
            current = current.next
        return total

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current.data is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next
        return '-> '.join(nodes)
    
    def __getitem__(self, index):
        if index >= len(self) or index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    
    def __setitem__(self, index, data):
        if index >= len(self) or index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

class Matrix(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [LinkedList() for i in range(rows)]
        for row in self.matrix:
            for i in range(cols):
                row.append(0)

    def __repr__(self):
        for row in self.matrix:
            print(row)
        return ''

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, data):
        self.matrix[index] = data

    def __iter__(self):
        for row in self.matrix:
            yield row

    def __len__(self):
        return len(self.matrix)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception("Matrices must be of the same size")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception("Matrices must be of the same size")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self[i][j] - other[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise Exception("Matrices must be m*n and n*p")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self[i][k] * other[k][j]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result[j][i] = self[i][j]
        return result

    def identity(self):
        if self.rows != self.cols:
            raise Exception("Identity matrix must be square")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            result[i][i] = 1
        return result
    
    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self[i][j] != other[i][j]:
                    return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __pow__(self, power):
        if self.rows != self.cols:
            raise Exception("Matrix must be square")
        result = self.identity()
        for i in range(power):
            result = result * self
        return result
    
    def __div__(self, other):
        if self.rows != self.cols:
            raise Exception("Matrix must be square")
        return self * other.inverse()
    
    def inverse(self):
        if self.rows != self.cols:
            raise Exception("Matrix must be square")
        if self.determinant() == 0:
            raise Exception("Matrix is not invertible")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = ((-1) ** (i + j)) * self.minor(i, j).determinant()
        return result.transpose() * (1.0 / self.determinant())
    
    def minor(self, row, col):
        if self.rows != self.cols:
            raise Exception("Matrix must be square")
        result = Matrix(self.rows - 1, self.cols - 1)
        r = 0
        for i in range(self.rows):
            if i == row:
                continue
            c = 0
            for j in range(self.cols):
                if j == col:
                    continue
                result[r][c] = self[i][j]
                c += 1
            r += 1
        return result
    
    def determinant(self):
        if self.rows != self.cols:
            raise Exception("Matrix must be square")
        if self.rows == 1:
            return self[0][0]
        if self.rows == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        result = 0
        for i in range(self.cols):
            result += ((-1) ** i) * self[0][i] * self.minor(0, i).determinant()
        return result
    
        

if __name__ == '__main__':
    m = Matrix(5,5)
    m[0][0] = 1
    m[1][1] = 1
    m[2][2] = 1
    m[3][3] = 1 
    m[4][4] = 1
   

