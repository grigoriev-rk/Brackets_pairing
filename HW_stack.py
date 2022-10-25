brackets = ['()','[]', '{}']                                        

class Stack_():                                                     

    def __init__(self, stack:str=''):
        self.stack = list(stack)
    def isEmpty(self):
        return (True if len(self.stack) == 0 else False)
    def push(self, item:str):
        self.stack += item
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()           
    def peek(self):
        if len(self.stack) == 0:
            return None
        return (self.stack[-1])
    def size(self):
        return (len(self.stack))


def is_balanced(check_stack:Stack_):                                
    if not check_stack.isEmpty() and not check_stack.size() % 2:     
        right_stack = Stack_()                                       
        while check_stack.size() > 1:                                
            last_item = check_stack.pop()
            next_item = check_stack.peek()
            closed_ = (next_item + last_item) in brackets
            if right_stack.size() > check_stack.size():
                bool_ = False
                break
            if not closed_:
                right_stack.push(last_item)
                continue
            check_stack.pop()
            bool_ = True
            while not right_stack.isEmpty():
                next_item = check_stack.pop()
                last_item = right_stack.pop()
                closed_ = (next_item + last_item) in brackets
                if not closed_:
                    bool_ = False
    else:
        bool_ = False
    print('Сбалансировано') if bool_==True else print('Не сбалансировано')  
    return (bool_)


def test():
    stack = Stack_('(((([{}]))))')
    is_balanced(stack)
    stack = Stack_('[([])((([[[]]])))]{()}')
    is_balanced(stack)
    stack = Stack_('{{[()]}}')
    is_balanced(stack)
    stack = Stack_('}{}')
    is_balanced(stack)
    stack = Stack_('{{[(])]}}')
    is_balanced(stack)
    stack = Stack_('[[{())}]')
    is_balanced(stack)
    print('Тесты пройдены')


if __name__ == '__main__':

    test()
