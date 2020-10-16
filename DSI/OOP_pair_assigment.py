from fractions import Fraction
class Polynomial():
    # from fractions import Fraction
    def __init__(self, lst): 
        self.lst = lst
        self.degree = len(lst) - 1
        
        
    def __repr__(self):
        return f'Polynomial({self.lst})'


    def __str__(self):
        poly_lst = []
        pol_str = ''
        
        # build list of polynomial terms
        for count, i in enumerate(self.lst):
            if i == 0:
                continue
            elif i == 1 or i == -1:
                if count == 0:
                    poly_lst.append(str(i))
                elif count == 1:
                    poly_lst.append('x')
                else:
                    poly_lst.append('x^' + str(count))
            else:
                if count == 0:
                    poly_lst.append(str(i))
                elif count == 1:
                    poly_lst.append(str(i) + 'x')
                else:
                    poly_lst.append(str(i) + 'x^' + str(count))
        
            
        # reverse poly_lst and build polynomial string to return
        poly_lst.reverse()
        for count, i in enumerate(poly_lst):
            if i[0] == '-' and count == 0:
                pol_str += i
            elif i[0] == '-' and count > 0:
                pol_str += ' - ' + i[1:]
            elif count == 0:
                pol_str += i
            else:
                pol_str += ' + ' + i
                
        # return the string
        return pol_str


    def evaluate(self, num):
        ev = 0
        for count, i in enumerate(self.lst):
            ev += i * num ** count

        return ev


    def __add__(self, other):
        # compare list length
        add_lst = []
        p1 = len(self.lst)
        p2 = len(other.lst)
        len_diff = abs(p1 - p2)
        # if input list lengths vary, insert 0s into the shorter list to make the same len
        if p1 > p2:
            other.lst.insert(len(other.lst), 0 * len_diff)
        elif p1 < p2: 
            self.lst.insert(len(self.lst), 0 * len_diff)
        for a, b in zip(self.lst, other.lst): 
                add_lst.append(a + b)
        
        return Polynomial(add_lst)


    def __sub__(self, other):
        # compare list length
        sub_lst = []
        p1 = len(self.lst)
        p2 = len(other.lst)
        len_diff = abs(p1 - p2)
        # if input list lengths vary, insert 0s into the shorter list to make the same len
        if p1 > p2:
            other.lst.insert(len(other.lst), 0 * len_diff)
        elif p1 < p2: 
            self.lst.insert(len(self.lst), 0* len_diff)
        for a, b in zip(self.lst, other.lst): 
                sub_lst.append(a - b)
        
        return Polynomial(sub_lst)


    def __neg__(self): 
        neg_lst = []
        for i in self.lst: 
            neg_lst.append(-i)
        return Polynomial(neg_lst)


    def __eq__(self, other): 
        eq_lst = []
        other_lst = []
        for i in self.lst: 
            if i == 0:
                continue
            else: 
                eq_lst.append(i)
        for j in other.lst: 
            if j == 0:
                continue
            else:
                other_lst.append(j)
        if eq_lst == other_lst: 
            return True
        else: 
            return False


    def __mul__(self, other):
        prod_dict = {}
        prod_lst = []
        for count_i, i in enumerate(self.lst):
            for count_j, j in enumerate(other.lst):
                if count_i + count_j not in prod_dict:
                    prod_dict[count_i + count_j] = i * j
                else:
                    prod_dict[count_i + count_j] += i * j
        for k in prod_dict:
            prod_lst.append(prod_dict[k])
        return Polynomial(prod_lst)


    def differentiate(self):
        deriv_lst = []
        for count, i in enumerate(self.lst): 
            deriv_lst.append(i * count)  
        deriv_lst.pop(0) 
        return Polynomial(deriv_lst)


    def integrate(self): 
        integ_lst = ['C']
        for count, i in enumerate(self.lst): 
            integ_lst.append(Fraction(i,(count + 1)))
        return Polynomial(integ_lst)


    # Integrate throwing list index out of range error
    # What I tested
    # p = Polynomial([3, 2, 1])
    # print(p.integrate())

   

    # def __mul__(self, other): 
    # would a numpy array be better here? 
    # find Cartesian product with itertools?
    # Non-laborious way to combine like terms? 


# some tests

# a = Polynomial([1, 2,  3])
# print('a = ' + str(a))

# b = Polynomial([1, 2, 3, 4])
# print('b = ' + str(b))

# c = a + b
# print('c = ' + str(c))

# d = a - b
# print('d = ' + str(d))

# e = a * b
# print('e = ' + str(e))

# print('a(3) = ' + str(a.evaluate(3)))

# print(Polynomial([2, 0, -2, -4]))

a = Polynomial([3, 2, 1])
b = a.integrate()
print
print(-a)
print(b)