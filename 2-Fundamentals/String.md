# Python String

**Intro**

To change the case of the string data type we can use upper(), lower() and casefold() methods.

### upper()

upper() method change all the characters in a string to uppercase. For example

```py title:"upper()"
name = 'aravind'
name.upper() # 'ARAVIND'
```

### lower()

lower() method change all the characters in a string to lowercase. For example

```py title:"lower()"
name = 'ARAVIND'
name.lower() # 'aravind'
```

### casefold()

casefold() method change all the characters in a string to lowercase. For example

```py title:"casefold()"
name = 'RAY'
name.casefold() # 'ray'
```

> [!question] Wait, does lower() and casefold() method both are same?
>> [!todo] **Nope**, The main difference is that lower() method will not change all the character to lower case if the character is unicode, but casefold() method will convert the unicode to it's base form.
> ```py
> text  = 'Déjà Vuß'
> text.casefold() # déjà vuss
> text.lower() # déjà vuß
> ```