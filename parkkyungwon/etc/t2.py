class node:
    __slots__ = ['data', 'left', 'right']

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    def self_pop(self):
        self.left.right = self.right
        self.right.left = self.left
    

class dll:
    def __init__(self):
        self.head = node(None, None, None)
        self.head.left = self.head.right = self.head
    
    def append(self, data):
        new_node = node(data, self.head.left, self.head)
        self.head.left.right = new_node
        self.head.left = new_node
    
    
def main():
    mydll = dll()
    for i in range(1, 101):
        mydll.append(i)
    
    head = mydll.head
    inode = head.right
    while inode is not head:
        print(inode.data, end=' ')
        inode = inode.right
    
    print()

    for _ in range(5):
        inode = head.right
        p = inode.right.data

        while inode is not head:
            if inode.data % p:
                print(inode.data, end=' ')
            else:
                inode.self_pop()

            inode = inode.right
        
        print()
    

main()
