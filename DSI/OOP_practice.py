
class Polynomial():
    def __init__(self, lst): 
        self.lst = lst
        self.degree = len(lst) - 1
        self.lst.reverse()
        
        
    def __repr__(self):
        return f'Polynomial({self.lst})'

    

     
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
    def differentiate(self):
        deriv_lst = []
        deg_deriv = len(self.lst) - 1
        for i in range(len(self.lst) - 1): 
            deriv_lst.append(self.lst[i] * deg_deriv)
            deg_deriv -= 1
                
        return Polynomial(deriv_lst)

        # def derivative(self):
        # derived_coeffs = []
        # exponent = len(self.coefficients) - 1
        # for i in range(len(self.coefficients)-1):
        #     derived_coeffs.append(self.coefficients[i] * exponent)
        #     exponent -= 1
        # return Polynomial(*derived_coeffs)
        

    def __neg__(self): 
        neg_lst = []
        for i in self.lst: 
            neg_lst.append(-i)
        return Polynomial(neg_lst)
       
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

        # def __eq__(self, other): 
        #     eq_lst = []
        #     other_lst = []
        #     for i in self.lst: 
        #         if i == 0:
        #             continue
        #         else: 
        #             eq_lst.append(i)
        #     for j in other.lst: 
        #         if j == 0:
        #             continue
        #         else:
        #             other_lst.append(j)
        #     if eq_lst == other_lst: 
        #         return True
        def __eq__(self, val):
        
            if isinstance(val, Polynomial):
                return self.coeffs == val.coeffs
            else:
                return len(self.coeffs)==1 and self.coeffs[0]==val
                
            
p = Polynomial([3, 2, 1])
print(p.differentiate())

# # print(p)
# deriv_p = p.differentiate()
# print(deriv_p)


# p1 = Polynomial([3, 2, 1])
# p2 = Polynomial([4, 5, 6, 2])
# # 1x^3 0x^2 + 3x + 3
# print(p1.poly_str() + p1.poly_str())
# print(Polynomial([3, 2, 1]) + Polynomial([3, 2,1]))
# print(p2.poly_str())

# class Polynomial():
#     def __init__(self, lst): 
#         self.lst = lst
#         self.degree = len(lst) - 1
#         self.lst.reverse()
        
    
#     def __repr__(self):
#         return f'Polynomial({self.lst})'

#     def pol_str(self):
#         poly_lst = []
#         deg = self.degree
#         for i in range(0, self.degree+1):
#             poly_lst.append(str(self.lst[i])+'x^'+str(deg))
#             deg -= 1
#         return poly_lst

        
# f'{self.m}x + {self.b}'