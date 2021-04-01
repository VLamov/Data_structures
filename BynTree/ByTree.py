import random

class node:   # узел дерева
    def __init__(self, data = None, left = None, right = None):  # инициализатор
        self.data   = data
        self.left   = left
        self.right  = right

    def __del__(self):   # деструктор
        print("удален узел", self.data)

#/* класс, описывающий само дерево */  
class Tree:
    def __init__(self):
        self.root = None #корень дерева
        self.sizetree = 0
        self.maxnode = 0
        self.minnode = 0

# /* функция для добавления узла в дерево */
    def insert(self, root, data):
        if(root is None):
            self.root = node(data)
            self.maxnode = data
            self.minnode = data
            self.sizetree = 1
        else:
            if(data <= root.data):
              if root.left is None:
                root.left = node(data)
                self.sizetree += 1
                self.minnode = min(data, self.minnode)
              else:
                self.insert(root.left, data)
            else:
              if root.right is None:
                root.right = node(data)
                self.sizetree += 1
                self.maxnode = max(data, self.maxnode)
              else:
                self.insert(root.right, data)

# /* функция для удаления дерева */
    def clear(self, root):
      if root:
        self.clear(root.left)
        self.clear(root.right)
        self.root = None
        self.maxnode = 0
        self.minnode = 0
        self.sizetree = 0

# /* функция для вычисления высоты дерева */
    def height(self, root, lheight = 0, rheight = 0):
      if root is None:
        return 0
      else:
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if lheight > rheight:
          return(lheight+1)
        else:
          return(rheight+1)

# /* функция для вычисления разряда ноды */
    def lenNode(self):
      if self.root is None:return 0;
      rank = len(max(str(self.maxnode),str(self.minnode)))
      return (rank);

# /* функция для вычисления высоты дерева */
    def size(self, root):
      if root is None: 
          return 0
      return (self.size(root.left) + 1 + self.size(root.right));

# /* функция для записи дерева в файл */
    def saveTree(self):
      def Preorder(root, ap_tt):
        if root:
          ap_tt.append(root.data)
          Node = Preorder(root.left, ap_tt)
          Node = Preorder(root.right, ap_tt)
        return ap_tt;
      if self.root is None:
        return 0;
      else:
        ap_t = list()
        ap_t = Preorder(self.root, ap_t)
        InputFile = open ('input_tree.dat', 'w')
        l_ap = 0
        InputFile.write(str(l_ap)+'\n')
        for element in ap_t:
          InputFile.write(str(element)+'\n')
        InputFile.close()

# /* функция для ввода дерева */
def input_tree():
  wel = "Введите размер дерева: "
  wel_in = input(wel)
  l_ap = int(wel_in)
  while l_ap < 0:
      print("размер дерева должен быть целым положительным числом: ")
      wel_in = input(wel)
      l_ap = int(wel_in)
  ap.clear(ap.root)
  ap_list = list()
  for i in range(l_ap):
    ap_list.append(random.randint(0, 1000))
  print(ap_list)
  for element in ap_list:
    ap.insert(ap.root, element)
  ap.saveTree()

# /* функция для загрузки дерева из файла */
def load_tree():
  ap.clear(ap.root)
  i = l_ap = 0
  InputFile = open ('input_tree.dat')
  for line in InputFile:
    if i == 0:
        l_ap = int(line)
    else:
      ap.insert(ap.root, int(line))
    i += 1
  InputFile.close()

def AnswerOut(ap):
  if ap.root:
    app = list()
    app.append ("Размер дерева: " + str(ap.sizetree)+" элементов")
    app.append ("Высота дерева: " + str(ap.height(ap.root))+" уровней")
    lsize = ap.size(ap.root.left) 
    rsize = ap.size(ap.root.right)
    app.append ("Длина левой ветки: " + str(lsize)+" элементов")
    app.append ("Длина правой ветки: " + str(rsize)+" элементов")
    if lsize > rsize:
      app.append ("Левая ветка длинее")
    else: 
      app.append ("Правая ветка длинее")
    app.append ("Максимальный элемент дерева: " + str(ap.maxnode))
    app.append ("Минимальный элемент дерева: " + str(ap.minnode))
    app.append ("Максимальная длина элемента дерева: " + str(ap.lenNode()))
    InputFile = open ('output_tree.dat', 'w',  encoding='utf-8')
    for str_app in app:
      print (str_app)
      InputFile.write(str_app+'\n')
    InputFile.close()
  else:
      print ("2 - Загрузить дерево:")


def menu():
    answer = ""
    while answer != "9":
        print ("Выберите ответ:")
        print ("1 - Ввести дерево:")
        print ("2 - Загрузить дерево:")
        print ("3 - Вывести дерево на экран:")
        print ("4 - Параметры дерева:")
        print ("9 - Выход из программы:")
        answer = input ()
        if answer == "1":
            print ("answer == 1")
            input_tree()
        elif answer == "2":
            print ("answer == 2")
            load_tree()
        elif answer == "3":
            print ("answer == 3")
            if ap.root:
              print(str(ap))
              # ap.printLevelOrder()
            else:
                print ("2 - Загрузить дерево:")
        elif answer == "4":
            print ("answer == 4")
            AnswerOut(ap)
        elif answer == "9":
            break
        print("\n")

ap = Tree()
l_ap = 0
menu()