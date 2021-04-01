import random

class Node:
    def __init__(self, Name = None, Left = None, Rigth = None):
        self.Name = Name
        self.Left = Left
        self.Rigth = Rigth

    def __del__(self):   # деструктор
        print("Удален узел", self.Name)

class BynlnkList:
    def __init__(self):
        self.root = None
        self.end = None
    
    def Exist(self, Name):
        found = False
        start = self.root
        end = self.end
        while not found:
            if start.Name == Name:
                found = True
            elif end.Name == Name:
                found = True
            else:
                start = start.Rigth
                end = end.Left
        return found;
        
    def AddNode(self, Name):
        currnode = None
        if not self.root:
            self.root = Node(Name)
            self.end = self.root
            currnode = self.end
        # elif self.Exist(Name):
        #     currnode = self.GetNode(Name)
        elif self.root == self.end:
            self.end = Node(Name)
            self.end.Left = self.root
            self.root.Rigth = self.end
            currnode = self.end
        else:
            currnode = self.end
            self.end = Node(Name)
            currnode.Rigth = self.end
            self.end.Left = currnode
            currnode = self.end
        return currnode;
    
    def GetNode(self, Name):
        currnode = None
        start = self.root
        end = self.end
        found = False
        while not found:
            if start.Name == Name:
                currnode = start
                found = True
            elif end.Name == Name:
                currnode = end
                found = True
            else:
                start = start.Rigth
                end = end.Rigth
        return currnode;
    
    def Clear(self):
        if not self.end:
            return;
        if self.root == self.end:
            del root
        else:
            while self.end:
                currnode = self.end
                self.end = self.end.Left
                if self.end:
                    self.end.Rigth = None
                del currnode
            currnode = self.root
            self.root = None
            del currnode
        return

    def Filling(self):
        al = list()
        for i in range(Size_bl):
            num = random.randint(0, Max_bl)
            if num not in al:
                al.append(num)
        InputFile = open ('input_bynlist.dat', 'w')
        for i in al:
            self.AddNode(i)
            InputFile.write(str(i)+'\n')
        InputFile.close()
    
    def loading(self):
        self.Clear()
        InputFile = open ('input_bynlist.dat')
        for line in InputFile:
            self.AddNode(int(line))
        InputFile.close()
    
    def listing(self):
        bl_list = list()
        currnode = self.root
        while currnode:
            bl_list.append(currnode.Name)
            currnode = currnode.Rigth
        return bl_list

def FillingEven(bl1):
    def Add(lst, Name):
        if Name%2 == 0:
            bl2.AddNode(Name)
    bl2 = BynlnkList()
    if not bl1.root:
        print("Первый список пустой")
        return
    if bl2.root:
        bl2.Clear()
    currnode = bl1.root
    while True:
        if currnode:
            Add(bl2, currnode.Name)
            currnode = currnode.Rigth
        else:
            break
    return bl2;

def NicePrint(blist):
    lst = list()
    Header    = "  №   ┼ Лево │ Имя  │ Право"
    Separator = "──────┼──────┼──────┼──────"
    lst.append(Header)
    currnode = blist.root
    nom = 1
    while currnode:
        line  = ""
        if not currnode.Left:
            left  = ""
        else:
            left = currnode.Left.Name
        name = currnode.Name
        if not currnode.Rigth:
            rigth  = ""
        else:
            rigth = currnode.Rigth.Name
        n =  '{:^6}'.format(nom) + "┼"
        leftstr = '{:^6}'.format(left) + "┼"
        namestr = '{:^6}'.format(name) + "┼"
        rigthstr = '{:^6}'.format(rigth)
        line = n+leftstr+namestr+rigthstr
        lst.append(Separator)
        lst.append(line)
        currnode = currnode.Rigth
        nom += 1
    return lst;

def outfile():
    InputFile = open ('output_bynlist.dat', 'w', encoding='utf-8')
    if bl.root != None:
        InputFile.write('Первый двусвязный список:'+'\n')
        for line in bl_list:
            InputFile.write(line+'\n')
    InputFile.write('\n')
    if bl_new.root != None:
        InputFile.write('Второй двусвязный список:'+'\n')
        for line in bl_new_list:
            InputFile.write(line+'\n')
    InputFile.close()


Size_bl = 12
Max_bl = 1000
bl = BynlnkList()
bl.Filling()
bl.loading()
bl_new = FillingEven(bl)
bl_list = NicePrint(bl)
bl_new_list = NicePrint(bl_new)
for i in bl_list:
    print(i)
print("")
for i in bl_new_list:
    print(i)

outfile()




