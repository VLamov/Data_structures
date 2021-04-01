class OneLnkList:
    head = None
    class Node:
        element = None
        next_node = None
        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node
    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = self.Node(element)
    def edit(self, element, index):
        node = self.head
        for i in range(index):
            node = node.next_node
        node.element = element
    def insert(self, index):
        node = self.head
        prev_node = self.head
        for i in range(index):
            prev_node = node
            node = node.next_node
        prev_node.next_node = self.Node(element, next_node=node)
    def length(self):
        if not self.head:
            return 0
        i = 1
        node = self.head
        while node.next_node:
            i += 1
            node = node.next_node
        return i
    def get(self, index):
        if not self.head:
            return ""
        node = self.head
        for i in range(index):
            node = node.next_node
        return node.element
    def reverse(self):
        if not self.head:
            return ""
        index = self.length()
        temp_self = OneLnkList()
        for i in range(index):
            temp_self.append(self.get(index-1-i))
        self.clear()
        for i in range(index):
            self.append(temp_self.get(i))
    def out(self):
        print('\n')
        node = self.head
        if not node:
            return ""
        while True:
            print(node.element)
            node = node.next_node
            if not node:
                break
    def delete(self, index):
        node = self.head
        prev_node = node
        if index == 0:
            self.head = self.head.next_node
        for i in range(index):
            prev_node = node
            node = node.next_node
        prev_node.next_node = node.next_node
        element = node.element
        del node
    def clear(self):
        if not self.head:
            return ""
        node = self.head
        index = self.length()
        for i in range(index)[::-1]:
            self.delete(i)

def input_polinom():
    ap.clear()
    aq.clear()
    wel = "Введите степень первого полинома: "
    wel_in = input(wel)
    p = int(wel_in)
    while p < 0:
        print("степень первого полинома должна быть целым положительным числом: ")
        wel_in = input(wel)
        p = int(wel_in)
    wel = "Введите степень второго полинома: "
    q = int(input(wel))
    while q > p:
        print("степень второго полинома должна быть целым положительным числом больше либо равно степени первого полинома: ")
        q = int(input(wel))
    i = 0
    while i < p+1:
        wel = 'Введите a(',i,') для первого полинома: ' 
        ap.append(int(input(wel)))
        i+=1
    i = 0
    while i < q+1:
        wel = "Введите a(",i,") для второго полинома: " 
        aq.append(int(input(wel)))
        i+=1

    InputFile = open ('input2.dat', 'w')
    InputFile.write(str(p)+'\n')
    for i in range(p):
        InputFile.write(str(ap.get(i))+'\n')
    InputFile.write(str(q)+'\n')
    for i in range(q):
        InputFile.write(str(aq.get(i))+'\n')
    InputFile.close()
def load_polinom():
    ap.clear()
    aq.clear()
    i = p = q =0
    InputFile = open ('input2.dat')
    for line in InputFile:
        if i == 0:
            p = int(line)
        elif i == p+2:
            q = int(line)
        elif q == 0:
            ap.append(int(line))
        else:
            aq.append(int(line))
        i += 1
        wel = line
    InputFile.close()

def Str_Polinom(l_a):
    def str_x(a, i):
        str_a = ""
        str_x = ""
        if i < ap_c:
            if a >= 0:
                str_a = "+"
        if i > 0:
            if a == 0:
                str_a = ""
                str_x = ""
            else:
                if a == 1:
                   str_a = str_a 
                elif a == -1:
                    str_a = "-"
                else:
                    str_a = str_a+str(a)
                if i == 1:
                    str_x = "x"
                else:
                    str_x = "x^" + str(i)
        else:
            str_a = str_a+str(a)
        return (str_a+str_x)

    wel = ""
    ap_c = l_a.length()-1
    for i in range(ap_c+1):
        wel = str_x(l_a.get(i), i) + wel
    return (wel)

def Div ():
    t = ap.length() # степень остатка
    q = aq.length() # степень делителя
    r = t-q+1 # степень частного
    i = 0
    if apt.length() > 0:
        apt.clear()
    if at.length() > 0:
        at.clear()
    for j in range (0, t):
        apt.append(int(ap.get(j)))
    apt.reverse()
    while i < r:
        at.append(int(apt.get(i)//aq.get(0)))  #коэффициент частного
        for j in range (0, q):
            if aq.get(j) != 0:
                a = apt.get(i+j)-(aq.get(j)*at.get(i))
                apt.edit(a, i+j)
        i += 1
    apt_t = OneLnkList()
    for i in range (0, t):
        if apt.get(i) != 0:
            apt_t.append(int(apt.get(i)))
    at.reverse()
    apt_t.reverse()
    InputFile = open ('output2.dat', 'w')
    InputFile.write(str(p)+'\n')
    for i in range(p):
        InputFile.write(str(ap.get(i))+'\n')
    InputFile.write(str(q)+'\n')
    for i in range(q):
        InputFile.write(str(aq.get(i))+'\n')
    t = at.length()
    InputFile.write(str(t)+'\n')
    for i in range(t):
        InputFile.write(str(at.get(i))+'\n')
    t_t = apt_t.length()
    InputFile.write(str(t_t)+'\n')
    for i in range(t_t):
        InputFile.write(str(apt_t.get(i))+'\n')
    InputFile.close()
    return at, apt_t

def menu():
    answer = ""
    while answer != "9":
        print ("Выберите ответ:")
        print ("1 - Ввести полиномы:")
        print ("2 - Загрузить полиномы:")
        print ("3 - Вывести полиномы на экран:")
        print ("4 - Деление полиномов:")
        print ("9 - Выход из программы:")
        answer = input ()
        if answer == "1":
            print ("answer == 1")
            input_polinom()
        elif answer == "2":
            print ("answer == 2")
            load_polinom()
        elif answer == "3":
            print ("answer == 3")
            if ap.length() != 0:
                print("Делимое:  "+Str_Polinom(ap))
                print("Делитель: "+Str_Polinom(aq))
            else:
                print ("2 - ЗАГРУЗИТЬ полиномы:")
        elif answer == "4":
            print ("answer == 4")
            if (ap.length() != 0) and (aq.length() != 0):
                at, apt = Div()
                print("Делимое:  "+Str_Polinom(ap))
                print("Делитель: "+Str_Polinom(aq))
                print("Частное: "+Str_Polinom(at))
                print("Остаток: "+Str_Polinom(apt))
            else:
                print ("2 - ЗАГРУЗИТЬ полиномы:")
        elif answer == "9":
            break
        print("\n")


ap = OneLnkList()  # Делимое
aq = OneLnkList()  # Делитель
at = OneLnkList()  # частное
apt = OneLnkList() # Остаток
p = 0
q = 0

menu()
        

