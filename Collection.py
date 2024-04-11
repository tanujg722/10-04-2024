from collections import namedtuple

# Create a named tuple class Point with fields x and y
Point = namedtuple('Point', ['x', 'y'])

# Create a Point object
p = Point(1, 2)

# Accessing fields using attribute names
print(p.x, p.y)  

# Accessing fields using index
print(p[0], p[1])  

# Unpacking the named tuple
x, y = p
print(x, y) 

# Converting named tuple to dictionary
print(p._asdict())  



from collections import deque

# Creating a deque
d = deque([1, 2, 3, 4])

# Append to the right
d.append(5)
print(d)  

# Append to the left
d.appendleft(0)
print(d)  

# Pop from the right
print(d.pop())  

# Pop from the left
print(d.popleft())  

print(d)  

from collections import ChainMap

# Define two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Create a ChainMap with dict1 and dict2
chain_map = ChainMap(dict1, dict2)

# Accessing keys
print(chain_map['a'])  
print(chain_map['b'])  
print(chain_map['c'])  

# Updating the first dictionary
dict1['a'] = 100

# ChainMap reflects the update
print(chain_map['a'])  

# In case want to acsess 2nd b value
value_of_2nd_b = chain_map.maps[1]['b']
print(value_of_2nd_b) 

from collections import Counter

# Create a Counter from a list
list1 = ['a', 'b', 'c', 'a', 'b', 'a']
counter = Counter(list1)

# Accessing counts
print(counter['a'])  
print(counter['b']) 
print(counter['c'])  

# Accessing all counts as a dictionary
print(dict(counter))  

# Update counts
list2 = ['a', 'b', 'c', 'a', 'd']
counter.update(list2)
print(counter)  

# Most common elements
print(counter.most_common(2))  

# Convert Counter object back to a list
updated_list = list(counter.elements())

print(updated_list)