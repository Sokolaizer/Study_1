from sys import stdin
import copy


class Matrix:
    def __init__(self, mtx):
        self.mtx = copy.deepcopy(mtx)

    def __str__(self):
        result = ''
        for i in self.mtx:
            for j in i:
                result += str(j) + '\t'
            result = result[:-1]
            result += '\n'
        return str(result[:-1])

    def size(self):
        line = (len(self.mtx), )
        column = (len(self.mtx[0]), )
        return line + column
    def __add__(self, other):
        ans = []
        inList = []
        for i in range(len(self.mtx)):
            for j in range(len(self.mtx[i])):
                inList = []
                element = self.mtx[i][j] + other.mtx[i][j]
                inList.append(element)
                ans.append(inList)
        ans.append(inList)
        return ans
#exec(stdin.read())
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)