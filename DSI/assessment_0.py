import numpy as np
def fizz_buzz():
    '''Returns the numbers from 1 to 100 into list. But for
    multiples of three append "Fizz" instead of the number and for the multiples
    of five append "Buzz". For numbers which are multiples of both three and five
    append "FizzBuzz".

    The first five elements of the output list are:
        lst = [1, 2, "Fizz", 4, "Buzz", ....]

    Parameters
    ----------
    None

    Returns
    -------
    list
    '''
    new_lst = []
    num_lst = list(range(101))
    for idx, i in enumerate(num_lst):
        if i % 3 == 0:
            num_lst[idx] = 'Fizz'
        elif i % 5 == 0: 
            num_lst[idx] = 'Buzz'
        elif i % 3 == 0 and i % 5 == 0: 
            num_lst[idx] = 'FizzBuzz'
    
    print(num_lst)
fizz_buzz()

# fizz_buzz()
# from collections import Counter
# def count_characters(string):
#     '''
#     Return a dictionary which contains
#     a count of the number of times each character appears in the string.
#     Characters which with a count of 0 should not be included in the
#     output dictionary.

#     FOR FULL POINTS DON'T USE IMPORTS.

#     Parameters
#     ----------
#     string: str

#     Returns
#     -------
#     dict
#         A dictionary with counts of each character in string
#     '''
#     d = Counter()
#     for i in string: 
#         d += i
#     print(d)
# count_characters('aabccc')


# def merge_dictionaries(d1, d2):
#     '''Returns a new dictionary containing all the keys from d1 and d2 with
#     their associated values. If a key is in both dictionaries, the new value is
#     the sum of the two values from d1 and d2.

#     FOR FULL POINTS DON'T USE IMPORTS AND MAXIMUM ONE LOOP.

#     Parameters
#     ----------
#     d1, d2: dictionary, dictionary

#     Returns
#     -------
#     dictionary
#     '''
#     d3 = {}
#     for k, v in d1.items():
#         for k2, v2 in d2.items(): 
#             if k in d2.keys(): 
#                 d1[k] = v + v2

#     d3 = d2.update(d1)

    # def cookie_jar(a, b):
    # '''
    # There are two jars of cookies.
    # Each has chocolate and peanut butter cookies.
    # Input 'a' is the fraction of cookies in Jar A which are chocolate.
    # Input 'b' is the fraction of cookies in Jar B which are chocolate.
    # A jar is chosen at random and a cookie is drawn.
    # The cookie is chocolate.
    # Return the probability that the cookie came from Jar A.

    # Parameters
    # ----------
    # a: float
    #     Probability of drawing a chocolate cooking from Jar A
    # b: float
    #     Probability of drawing a chocolate cooking from Jar B

    # Returns
    # -------
    # float
    #     Conditional probability that cookie was drawn from Jar A given
    #     that a chocolate cookie was drawn.    
    # '''
    # prob = (0.5 * a * 0.5)/(0.5* (0.5)*a + (0.5* b))

    # def boolean_indexing(arr, minimum):
    # '''Return an array of only the elements of "arr" that are greater than
    # or equal to "minimum".

    # FOR FULL POINTS DON'T USE LOOPS OR LIST COMPREHENSIONS.

    # Parameters
    # ----------
    # arr: NumPy array  
    # minimum: int

    # Returns
    # -------
    # NumPy array
    #     Of elements of arr that are >= minimum

    # >>>boolean_indexing(np.array([[3, 4, 5], [6, 7, 8]]), 7)
    # array([7, 8])
    # '''
    # arr[arr >= minimum]

    # boolean_indexing(np.array([[3, 4, 5], [6, 7, 8]]), 7)