# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    #Creates a Stack object and allows things to be added or removed from the stack.
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None
        pass

    def __len__(self):
        # YOUR CODE STARTS HERE
        count=0
        current=self.top
        while current:
            current=current.next
            count+=1
        return count
        pass

    def push(self,value):
        # YOUR CODE STARTS HERE
        if self.top == None:
            self.top = Node(value)
            self.top.next = None
        else:
            previous = self.top
            self.top = Node(value)
            self.top.next = previous
        pass

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return None
        else:
            Rvalue = self.top
            self.top = self.top.next
            return Rvalue.value
        pass

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return None
        else:
            return self.top.value
        pass


#=============================================== Part II ==============================================

class Calculator:
    #Calculator can take an expression and return the postfix version and use that to calculate the equation
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except:
            return False
        pass



    
    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + [ 1 + 4 ]')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('( 3 ) 3')
            '3.0 3.0 *'
            >>> x._getPostfix('( 3 + 1 ) 3 ^ 2')
            '3.0 1.0 + 3.0 2.0 ^ *'
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        SignStack = Stack()
        POpencount = Stack()
        BOpencount = Stack()
        DOpencount = Stack()
        SignDict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, None: 0}
        lst = txt.split()
        #Debug:
        #print(lst)
        Cont = True
        Pcount = 0
        Bcount = 0
        Dcount = 0
        lst.reverse()
        for it in lst:
            postfixStack.push(it)
        #Debug:
        #return postfixStack
        last = None
        item = postfixStack.pop()
        Rlst = []
        while item != None:
            if self._isNumber(item): #Found number
                if last == 'number':
                    return None
                else:
                    Rlst.append(f"{float(item)}")
                    if last == 'ParenthC':
                        SignStack.push('*')
                last = 'number'
            elif item == '(': #Found open (
                Pcount += 1
                if last == 'number' or last == 'ParenthC':
                    SignStack.push('*')
                SignStack.push('(')
                last = 'Parenth'
                POpencount.push(Bcount)
                POpencount.push(Dcount)
            elif item == ')': #Found end )
                Pcount -= 1
                if Pcount < 0:
                    return None
                else:
                    PDcount = POpencount.pop()
                    PBcount = POpencount.pop()
                    if PDcount == Dcount and PBcount == Bcount:
                        while SignStack.peek() != None and SignStack.peek() != '(':
                            Rlst += SignStack.pop()
                        SignStack.pop()
                        last = 'ParenthC'
                    else:
                        return None
            elif item == '[': #Found open [
                Bcount += 1
                if last == 'number' or last == 'ParenthC':
                    SignStack.push('*')
                SignStack.push('[')
                last = 'Parenth'
                BOpencount.push(Pcount)
                BOpencount.push(Dcount)
            elif item == ']': #Found end ]
                Bcount -= 1
                if Bcount < 0:
                    return None
                else:
                    BDcount = BOpencount.pop()
                    BPcount = BOpencount.pop()
                    if BDcount == Dcount and BPcount == Pcount:
                        while SignStack.peek() != None and SignStack.peek() != '[':
                            Rlst += SignStack.pop()
                        SignStack.pop()
                        last = 'ParenthC'
                    else:
                        return None
            elif item == '{': #Found open {
                Dcount += 1
                if last == 'number' or last == 'ParenthC':
                    SignStack.push('*')
                SignStack.push('{')
                last = 'Parenth'
                DOpencount.push(Bcount)
                DOpencount.push(Pcount)
            elif item == '}': #Found end }
                Dcount -= 1
                if Dcount < 0:
                    return None
                else:
                    DPcount = DOpencount.pop()
                    DBcount = DOpencount.pop()
                    if DPcount == Pcount and DBcount == Bcount:
                        while SignStack.peek() != None and SignStack.peek() != '{':
                            Rlst += SignStack.pop()
                        SignStack.pop()
                        last = 'ParenthC'
                    else:
                        return None                        
            elif item == '+' or item == '-' or item == '*' or item == '^' or item == '/': #Operator found
                if last == 'sign' or last == None:
                    return None
                elif item == '^' and postfixStack.peek() != None:
                    #temp = postfixStack.pop()
                    #SignStack.push(item)
                    last = 'sign'
                else:
                    ASign = SignStack.peek()
                    while SignStack.top != None and ASign != '(' and ASign != '[' and ASign != '{' and SignDict[item] <= SignDict[ASign]:
                        Rlst += SignStack.pop()
                        ASign = SignStack.peek()
                SignStack.push(item)
                last = 'sign'

            else: #Foreign string found
                return None
            item = postfixStack.pop()
        if Pcount != 0 or Bcount != 0 or Dcount != 0 or last == 'sign':
            return None
        else:
            # Need Proper print return statement
            # (), [], {}, ^ + 1, * for + and - 
            # Use pull maybe
            #All Done
            item = SignStack.top
            while item != None:
                Rlst += item.value
                item = item.next
            return ' '.join(Rlst)
        pass





    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * { 5 - 3 ^ 2 } + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * [ 4 ] ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''
        #Attempt to create a Stack that collects all the numbers per postfix item then takes out the top 2 numbers when it finds a sign. Find a way to calculate it then put the calculation back in the Stack
        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        # YOUR CODE STARTS HERE
        postfix = self._getPostfix(self.__expr)
        #print(postfix)
        if postfix == None:
            return None
        fixlst = postfix.split()
        #print(fixlst)
        #print(type(fixlst[0]))
        for item in fixlst: #item is a numebr
            if self._isNumber(item):
                calcStack.push(float(item))
            else: #item must be an operation
                num2 = calcStack.pop()
                num1 = calcStack.pop()
                if item == '+':
                    num = num1 + num2
                    calcStack.push(num)
                elif item == '-':
                    num = num1 - num2
                    calcStack.push(num)
                elif item == '*':
                    num = num1 * num2
                    calcStack.push(num)
                elif item == '/':
                    num = num1/num2
                    calcStack.push(num)
                elif item == '^':
                    num = num1**num2
                    calcStack.push(num)
        return calcStack.pop()
        pass



#=============================================== Part III ==============================================

class AdvancedCalculator:
    #AdvancedCalculator can take a list of expressions separated by ';'. The expressions can included variables that are predefined and will find and answer. The expressions will be returned in a dictionary along with the value of the variables at the time.
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if len(word) == 0:
            return False
        elif word[0].isalpha() == False:
            return False
        else:
            for char in word[1:]:
                if char.isalpha() == False and char.isalnum() == False:
                    return False
            return True
        pass
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        lst = expr.split(' ')
        #Debug:
        #print(lst)
        Rlst = []
        for item in lst:
            if item in self.states:
                Rlst.append(f"{self.states[item]}")
            elif self._isVariable(item):
                return None
            else:
                Rlst += item
            Rlst += ' '
        Rlst.pop()
        return ''.join(Rlst)
        pass

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        #self: _isVariable and _replaceVariables
        #calcObj: calculate, setExpr, getExpr, isNumber, getPostfix in calculate
        lst = self.expressions.strip()
        lst = lst.split(';')
        #Debug:
        #print(lst)
        Rdict = {}
        for eq in lst:
            eqlst = eq.split(' ')
            if eqlst[0] == 'return':
                line = self._replaceVariables(' '.join(eqlst[1:]))
                calcObj.setExpr(line) 
                Rdict['_return_'] = calcObj.calculate
            else:
                if self._isVariable(eqlst[0]):
                    line = self._replaceVariables(' '.join(eqlst[2:]))
                    calcObj.setExpr(line)
                    self.states[eqlst[0]] = calcObj.calculate
                else:
                    self.states = {}
                    return None
                Rdict[eq] = self.states.copy()
        #Debug:
        #print(Rdict)
        return Rdict
        pass



def run_tests():
    import doctest

    #- Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    #doctest.run_docstring_examples(AdvancedCalculator, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()