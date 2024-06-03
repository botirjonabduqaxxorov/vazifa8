# 1
# class CustomList:
#     def __init__(self):
#         self.items = []

#     def append(self, item):
#         """Append an item to the list."""
#         self.items.append(item)

#     def __iter__(self):
#         """Return an iterator for the list."""
#         return iter(self.items)

#     def __repr__(self):
#         """Return a string representation of the list."""
#         return repr(self.items)

# my_list = CustomList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)

# print(my_list)  

# for item in my_list:
#     print(item)

# 1
# class CustomList:
#     def __init__(self):
#         self.items = []
#         self._backup = None

#     def append(self, item):
#         """Append an item to the list."""
#         self.items.append(item)

#     def __enter__(self):
#         """Enter the runtime context related to this object."""
#         self._backup = self.items.copy()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         """Exit the runtime context related to this object."""
#         if exc_type is not None:
#             self.items = self._backup
    
#     def __iter__(self):
#         """Return an iterator for the list."""
#         return iter(self.items)

#     def __repr__(self):
#         """Return a string representation of the list."""
#         return repr(self.items)

# try:
#     with CustomList() as my_list:
#         my_list.append(1)
#         my_list.append(2)
#         raise ValueError("Something went wrong")
#         my_list.append(3)
# except ValueError as e:
#     print(e)

# print(my_list)  

# with CustomList() as my_list:
#     my_list.append(4)
#     my_list.append(5)
#     my_list.append(6)

# print(my_list) 








# from contextlib import contextmanager

# class CustomList:
#     def __init__(self):
#         self.items = []

#     def append(self, item):
#         """Append an item to the list."""
#         self.items.append(item)

#     def __iter__(self):
#         """Return an iterator for the list."""
#         return iter(self.items)

#     def __repr__(self):
#         """Return a string representation of the list."""
#         return repr(self.items)

# @contextmanager
# def managed_list(custom_list):
#     """Context manager for CustomList to handle exceptions and rollback."""
#     # Create a backup of the current state of items
#     backup = custom_list.items.copy()
#     try:
#         yield custom_list
#     except Exception as e:
#         # Restore the original state if an exception occurs
#         custom_list.items = backup
#         raise e

# # Example usage
# try:
#     with managed_list(CustomList()) as my_list:
#         my_list.append(1)
#         my_list.append(2)
#         # Simulate an error
#         raise ValueError("Something went wrong")
#         my_list.append(3)
# except ValueError as e:
#     print(e)

# print(my_list)  # Output should be: [] only if the error is handled properly

# # Example where no error occurs
# with managed_list(CustomList()) as my_list:
#     my_list.append(4)
#     my_list.append(5)
#     my_list.append(6)

# print(my_list)  # Output: [4, 5, 6]
