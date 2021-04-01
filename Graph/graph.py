class Vertex:
    def __init__ (self, Name = None, Number = 0):
        self.Name = Name
        self.Number = Number

class Edge:
    def __init__ (self, From = None, To = None, Wegth = 0):
        self.From  = From
        self.To    = To
        self.Wegth = Wegth

class Graf:
    def __init__ (self):
        self.Vertexes = list()
        self.Edges    = set()
    
    def AddVertex (self, Name):
        self.Vertexes.append(Vertex(Name, len(self.Vertexes)))
    
    def GetVertex (self, Name):
        return self.Vertexes[Name]
         
    def AddEdge (self, From, To, Wegth):
        self.Edges.add(Edge(self.GetVertex(From), self.GetVertex(To), Wegth))
    
    def Firstload(self):
        for i in range(VertexCount):
            self.AddVertex(i)
        self.AddEdges()
        Matrix = self.AddMatrix()

    def AddEdges(self):
        grf.AddEdge (0, 1, 1)
        grf.AddEdge (0, 2, 1)
        grf.AddEdge (0, 3, 1)
        grf.AddEdge (0, 4, 1)
        grf.AddEdge (0, 5, 1)
        grf.AddEdge (1, 2, 1)
        grf.AddEdge (1, 4, 1)
        grf.AddEdge (2, 3, 1)
        grf.AddEdge (3, 4, 1)
        grf.AddEdge (4, 5, 1)
        grf.AddEdge (5, 2, 1)
        grf.AddEdge (5, 6, 1)
        grf.AddEdge (5, 7, 1)
        grf.AddEdge (6, 5, 1)
        grf.AddEdge (6, 7, 1)
        grf.AddEdge (7, 5, 1)
        grf.AddEdge (7, 6, 1)
    
    def Clear(self):
        self.Edges.clear()
        self.Vertexes.clear()
        return;

    def AddMatrix(self):
        matrix = [[0 for i in range(VertexCount)] for j in range(VertexCount)]
        for edge in self.Edges:
            row = edge.From.Number
            column = edge.To.Number
            matrix [row][column] = int(edge.Wegth)
        InputFile = open ('input_graf.dat', 'w')
        InputFile.write(str(VertexCount)+'\n')
        for vertex in self.Vertexes:
            InputFile.write(str(vertex.Name)+'\n')
        for row in matrix:
            InputFile.write(str(row)+'\n')
        InputFile.close()
        return matrix;
    
    def SaveOutGraf(self, matrix, pathes):
        InputFile = open ('output_graf.dat', 'w', encoding='utf-8')
        InputFile.write('Количество узлов в Графе: ' + str(VertexCount)+'\n')
        InputFile.write('\n')
        InputFile.write('Граф в виде матрицы:'+'\n')
        for line in matrix:
            InputFile.write(line+'\n')
        InputFile.write('\n')
        line = 'Пути обхода Графа в виде матрицы от узла '
        line += str(FirstVertex) + ' до узла ' + str(LastVertex) + ':\n'
        InputFile.write(line)
        for line in pathes:
            InputFile.write(str(line)+'\n')
        InputFile.close()

    def LoadMatrixGraf(self):
        InputFile = open ('input_graf.dat')
        i = VertexCount = 0
        matrix = []
        self.Clear()
        for line in InputFile:
            if i == 0:
                VertexCount = int(line)
            elif i < VertexCount + 1:
                self.AddVertex(int(line))
            else:
                line = line.strip()[1:-1].split()
                row = [int(i.strip(",")) for i in line]
                matrix.append(row)
                j = 0
                for wigth in row:
                    if wigth != 0:
                        self.AddEdge(i-VertexCount-1, j, wigth)
                    j += 1
            i += 1
        InputFile.close()
        return matrix

    def OutMatrix(self, matrix):
        Header = "   "
        Separator = "───"
        Names = list()
        out = []
        for vertex in self.Vertexes:
            Header += f"│ {vertex.Name} "
            Separator += "┼───"
            Names.append(vertex.Name)
        i = 0
        out.append(Header)
        for row in matrix:
            out.append(Separator)
            String = f" {Names[i]} "
            for column in row:
                String += f"│ {column} "
            out.append(String)
            i += 1
        return out

    def FindPathes(self, matrix, vertexFrom, vertexTo):
        def Nodes(first):
            ListNodes = []
            for v in range(len(Matrix)):
                if Matrix[first][v] != 0:
                    ListNodes.append(v)
            return ListNodes;

        def FindPath (v1, v2, path):
            endfound = False
            path.append(v1)
            if v1 == 3:
                v = 0
            while not endfound:
                true_v = Nodes(v1)
                for v in true_v:
                    if matrix[v1][v2] != 0:
                        path.append(v2)
                        if path not in Pathes:
                            endfound = True
                            break
                        else:
                            del path[-1]
                    if (v in path) or (v in valid):
                        continue;
                    else:
                        v1 = v
                        path.append(v1)
                        break
                else:
                    path = []
                    endfound = True
            return path;
        
        Pathes = []
        vertex1 = vertex2 = -1
        for vertex in self.Vertexes:
            if vertex.Name == vertexFrom:
                vertex1 = vertex.Number
            elif vertex.Name == vertexTo:
                vertex2 = vertex.Number
            elif vertex1 > -1 and vertex2 > -1:
                break
        path = [vertex1]
        valid = []
        for vertex in range(len(matrix)):
            if (vertex != vertex1) and (matrix[vertex1][vertex] != 0):
                found = False
                while True:
                    path = [vertex1]
                    path = FindPath (vertex, vertex2, path)
                    if len(path) == 0:
                        break
                    else:
                        Pathes.append(path)
                        found = True
                if found:
                    valid.append(vertex)
        return Pathes;

# Количество узлов в Графе
VertexCount = 8
# Количество связей в Графе
EdgesCount = 17
# Начальный узел обхода Графа
FirstVertex = 0
# Конечный узел обхода Графа
LastVertex = 7
# Инициализация Графа
grf = Graf()
# Объявление изходной матрицы
Matrix = []
# Первоначальное заполнение Графа
# и вывод в файл матрицу
grf.Firstload()
# Очистка Графа и заполнение Графа из файла матрицы 
Matrix = grf.LoadMatrixGraf()
# Формирование списка матрицы 
# для вывода на печать и в файл результата
LineMatrix = grf.OutMatrix(Matrix)
for line in LineMatrix:
    print(line)
print()
# Формирование путей обхода Графа с начального узла до конечного
# и вывод в список для вывода на печать и в файл результата
Pathes = grf.FindPathes(Matrix, FirstVertex, LastVertex)
for line in Pathes:
    print(line)
# Вывод списка матрицы и путей обхода Графа в файл результата
grf.SaveOutGraf(LineMatrix, Pathes)