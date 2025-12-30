# def func(n):
#     a=[]
#     for i in range(n):
#         a.append(i)
#     return a
# gen=func(3)
# print(type(gen),gen)

# using generator
# def func(n):
#     for i in range(n):
#         yield i
    
# gen=func(3)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# defaultdict
# from collections import defaultdict

# d=defaultdict(int)
# d['a']+=1
# d['b']+=2
# print(d)

# Basic decorator
# def my_decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

#Python's pdb module
# import pdb

# def divide(a,b):
#     pdb.set_trace()
#     return a/b

# result=divide(10,0)
# print(result)

import logging
logging.basicConfig(
filename="app.log",
filemode="w", # Overwrite each run; use "a" to append
level=logging.DEBUG,
format="%(asctime)s- %(levelname)s- %(message)s"
)
logging.debug("this is debug message")
logging.info("Program started")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("this is critical message ")