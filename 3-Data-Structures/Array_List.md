## Array in Python

### Intro

A python list is mutable object which store collections of different datatype in order.

```py title:syntax
variable = [element1, element2, ...]
```

### Accessing Element(s)

We can access python list element by index method, Index starts at 0 (zero).

```py title:"Accessing Element(s)"
friuts = ['Apple', 'Jackfruit', 'Mango', 'Orange', 'Pineapple']
			0           1          2        3           4

# To access first element from the list
print(fruits[0]) #Apple

# To acess last element from the list
print(fruits[-1]) #Pineapple
```

### del, pop(), remove(), clear()

To delete an element from the list use we can use three methods

For example to delete grape we can use del keyword along with it's index

```py
del fruits[2]
print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange', 'Pineapple', 'Jackfruit']
```

To remove the last element from the list we can use **pop()** method and this method also return the removed value, so we can stored the removed element and do some operations if needed

```py
fruits.pop() # Jackfruit
print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange', 'Pineapple']
```

We can also use pop method to remove other elements from the list by specifying the index of that element, if we want the returned element to preform some operation.

```py
fruits.pop(1)
print(fruits) # ['Apple', 'Mango', 'Orange', 'Pineapple']
```

What if you don't know the index of the element that you want to remove, we can just use the remove() method

```py
fruits.remove('apple')

Traceback (most recent call last):
File "<pyshell#16>", line 1, in <module>
	fruits.remove('apple')
ValueError: list.remove(x): x not in list
```

Wow! An error, **Don't forget python is case-sensitive**. 

```py
fruits.remove('Apple')
print(fruits) # ['Mango', 'Orange', 'Pineapple']
```

> [!question] Question: Does remove() method return an removed element?, let's check it out
>> [!todo] Answer: No, remove() method doesn't return the removed element
>```py
> element = fruits.remove('Mango')
> print(element) # None
> print(fruits) # ['Orange', 'Pineapple']
> ```

### Modifying (Updating)

To update an element from the list get the element by using index method and add the new element to replace.

```py
fruits[1] = 'Banana'
print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange', 'Pineapple']
```

### append(), insert(), extend()

To add a new element into to list we can use two methods

append() - which insert the new element at the end of the list and 
insert() - which insert the new element at the specified index

```py title:"Syntax and examples:"
fruits.append('Jackfruit')
print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange', 'Pineapple', 'Jackfruit']

fruits.insert(2, 'Grape')
print(fruits) # ['Apple', 'Banana', 'Grape', 'Mango', 'Orange', 'Pineapple', 'Jackfruit']
```

### len()

To find out how many elements are presented in a list we can use len() method.

```py
print(len(fruits)) # 2
```

### count()

### 	sorted(), sort(reverse=True), reverse()

### Slicing [:], copy()

### Comprehensions

### random.shuffle()

### Index()

### Looping techniques

### Comparing sequences

### Operators in list +, *

### Advantages of List

- It's easy to select random elements from an array because elements are live next to each other in memory slot, (For example in Linked list, elements are not stored in next to each other in memory. So if we have to find the 5th element from the linked list, we have to go through 1 to 4 to get the 5th element) briefly reading an element from a list is lot faster O(1) times.

### Disadvantages  of List

- Array / List elements are live next to each other in memory slot, so if we want to add new element in the memory but if the adjacent slot is occupied we have to move all the elements to new slot where sufficient space is available for old elements and new one. So **adding** new element in array / list will **take O(n)** time if next slot is occupied or not.
- Like above point, **Deleting** an element from the list will also take extra time, if we have to delete the 5th index element in the list of 10, we use the del list[5] but from index 6 to 9 will move up to the memory slot, so it will take **O(n)** times.