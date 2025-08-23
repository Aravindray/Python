# Python Keywords

### False
### None
### True
### and
### as
### assert
### async
### await
### break
### class
### continue
### def
### del
### elif
### else
### except
### finally
### for
### from
### global

Let's say we have 3 function nested inside one another, like below example, name variable is placed outside the functions but the inner score of function can able to access the variable no matter where the scopes ends with the help of global keyword

```py title:"global keyword example"
name = 'aravind'
def one():
	name = 'ray'
	def two():
		def three():
			global name
			print(name) # 'aravind'
		three()
		print(name) # 'ray'
	two()
	print(name) # 'ray'
one()
```

### if
### import
### in
### is
### lambda
### nonlocal
### not
### or
### pass
### raise
### return
### try
### while
### with
### yield


> [!tip] Do you know how to print all keywords in python?
> ```py
> import keyword
> print(keyword.kwlist)
> ```