class Interpreter:
    def __init__(self,tree):
        self.tree= tree

        
    def computer_bin(self, left, op, right):
        left_type=left.type
        right_type=right.type
        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)
   
        if op.value =="+":
            operator= (left.value)+ (right.value)
        elif op.value =="-":
            operator= (left.value)- (right.value)
        elif op.value =="*":
            operator =(left.value)* (right.value)
        elif op.value =="/":
            operator=(left.value)/ (right.value)
        return int(operator) if left.type=="int" else float(operator)
        

    def interpret(self,tree=None):
        #post order traversal
        if tree == None:
            tree=self.tree 
        left_node=self.tree[0]
        if isinstance(left_node):
            left_node= self.interpret(left_node)
        
        right_node=self.tree[2]
        if isinstance(right_node):
            right_node = self.interpret(right_node)
        operater=self.tree[1]
        return self.computer_bin(left_node,operater,right_node)
    