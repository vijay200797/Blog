# import pandas as pd
# data = {'ProductID': [101, 102, 103, 104],
#        'Price': [25, 30, 22, 35],
#        'Quantity': [10, 15, 8, 12]}
# df = pd.DataFrame(data)
# df['Total'] = df['Price'] * df['Quantity']
# result = df.groupby('Total')['ProductID'].count().reset_index()
# print(result)


# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# row_sums = arr.sum(axis=1)
# col_sums = arr.sum(axis=0)
# result = np.max(row_sums) - np.min(col_sums)
# print(result)


# import pandas as pd
# data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
#        'Sales': [100, 120, 90, 110]}
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])
# df['Moving Average'] = df['Sales'].rolling(window=2).mean()
# df['Moving Sum'] = df['Sales'].rolling(window=3).sum()
# result = df[['Date', 'Sales', 'Moving Average', 'Moving Sum']]
# print(result)



# import pandas as pd

# data = {'ProductID': [101, 102, 103, 104],
#         'Price': [25, 30, 22, 35],
#         'Quantity': [10, 15, 8, 12]}

# df = pd.DataFrame(data)
# df['Total'] = df['Price'] * df['Quantity']

# highest_total = df[df['Total'] == df['Total'].max()]
# lowest_total = df[df['Total'] == df['Total'].min()]

# result = highest_total.append(lowest_total)
# print(result)



# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side**2

# shapes = [Circle(5), Square(4)]
# for shape in shapes:
#     print(shape.area())

# import asyncio

# async def coro(n):
#     await asyncio.sleep(n)
#     return n
# async def main():
#     tasks = [asyncio.create_task(coro(i)) for i in range(3)]
#     results = await asyncio.gather(*tasks)
#     print(results)

# asyncio.run(main())



# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     elif exponent % 2 == 0:
#         result = power(base, exponent // 2)
#         return result * result
#     else:
#         result = power(base, (exponent - 1) // 2)
#         return base * result * result

# result1 = power(2, 4)
# result2 = power(3, 5)

# print(result1, result2)



# students = [
#     {'name': 'Alice', 'age': 20, 'score': 85},
#     {'name': 'Bob', 'age': 22, 'score': 90},
#     {'name': 'Charlie', 'age': 19, 'score': 78},
#     {'name': 'David', 'age': 21, 'score': 95}
# ]

# students.sort(key=lambda student: student['score'], reverse=True)
# top_student = students[0]['name']

# print(top_student)


# def mystery(n):
#     if n == 0:
#         return 0
#     return n + mystery(n // 2)

# result = mystery(10)
# print(result)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.print_list()



# data = [("Apple",9), ("Mango",6), ("Banana", 7)]

# di = { str(item[0]).lower():item[1] for item in data }
# print(di)

import asyncio

async def coro(n):
    print(f"Waiting Time {n}")
    await asyncio.sleep(n)
    return n
async def main():
    tasks = [asyncio.create_task(coro(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
print("Done")
