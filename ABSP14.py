# the none value
# I can't understand it yet
'''This value-without-a-value can be helpful when you 
need to store something that won’t be confused for
a real value in a variable. One place where None is used 
is as the return value of print(). The print() function displays text on the screen,
but it doesn’t need to return anything in the same way len() or input() does. But since all function
calls need to evaluate to a return value, print() returns None.'''

spam = print('Hello!')

None == spam
print (None == spam)
'''Behind the scenes, Python adds return None to the end of any function
 definition with no return statement. This is similar to how a while or for
  loop implicitly ends with a continue statement. Also, if you use a return
   statement without a value (that is, just the return keyword by itself),
    then None is returned.'''