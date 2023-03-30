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
    
    def determinant_recursive(self):
        if self.rows != self.cols:
            raise Exception("Matrix must be square")
        if self.rows == 1:
            return self[0][0]
        if self.rows == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        result = 0
        for i in range(self.cols):
            result += ((-1) ** i) * self[0][i] * self.minor(0, i).determinant_recursive()
        return result
    

        

if __name__ == '__main__':
    m = Matrix(5, 5)
    for i in range(5):
        for j in range(5):
            m[i][j] = int(input(f'Valor de la casilla {i}{j}: '))
    print (m.determinant_recursive())
    

