class Polynomial():
    def __init__(self, lst): 
        self.lst = lst
        self.degree = len(lst) - 1
        self.lst.reverse()      

    def __repr__(self):
        return f'Polynomial({self.lst})' 

    def __str__(self):
        poly_lst = []
        deg = self.degree
        pol_str = ''
        # build list of polynomial terms
        for i in range(0, self.degree+1):
            poly_lst.append(str(self.lst[i])+'x^'+str(deg))
            deg -= 1
        # remove the x^0 from last term
        poly_lst[-1] = poly_lst[-1][0]
        # remove 0's from the list, remove 1's from the front of any terms
        for count, i in enumerate(poly_lst):
            if int(i[0]) == 0:
                poly_lst.pop(count)
            if int(i[0]) == 1:
                poly_lst[count] = i[1:]
        # build polynomial string to return
        for i in range(0, len(poly_lst)):
            pol_str += poly_lst[i] + ' + '
        # print out the string, excluding the last 3 which are ' + '
        return pol_str[0:-3]

    def evaluate(self, val):
        res = 0
        pwr = self.degree
        for i in self.lst:
            res += val**pwr * i
            pwr -= 1
        return res

    def __add__(self, other):
        # compare list length
        add_lst = []
        p1 = len(self.lst)
        p2 = len(other.lst)
        len_diff = abs(p1 - p2)
        # if input list lengths vary, insert 0s into the shorter list to make the same len
        if p1 > p2:
            other.lst.insert(0,0 * len_diff)
        elif p1 < p2: 
            self.lst.insert(0, 0* len_diff)

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
            other.lst.insert(0,0 * len_diff)
        elif p1 < p2: 
            self.lst.insert(0, 0* len_diff)
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

    def differentiate(self):
        deriv_lst = []
        deg_deriv = len(self.lst) - 1
        for i in range(len(self.lst) - 1): 
            deriv_lst.append(self.lst[i] * deg_deriv)
            deg_deriv -= 1        
        return Polynomial(deriv_lst)
# Integrate throwing list index out of range error
# What I tested
# p = Polynomial([3, 2, 1])
# print(p.integrate())
    def integrate(self): 
        integral_lst = []
        deg_intg = len(self.lst) + 1
        integral_lst.append('C')
        for i in range(deg_intg + 1): 
            integral_lst.append(self.lst[i] / deg_intg +1)
            deg_intg += 1        
        return Polynomial(integral_lst)
    
    # def __mul__(self, other): 
    # would a numpy array be better here? 
    # find Cartesian product with itertools?
    # Non-laborious way to combine like terms? 




a = Polynomial([3, 2, 1])
print(a.differentiate())