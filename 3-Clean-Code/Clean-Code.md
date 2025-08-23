# Clean Code

## Naming Convenience

Recommended [naming convenience](https://peps.python.org/pep-0008/#naming-conventions) for defining a _function_, _modules (files)_, and _variables_ are use all **lower_cases** maybe use underscore for readability, for _class_ are **UpperCamelCase**, and for _packages_ are **lowercases** although the use of underscores is discouraged.

### Mutable and Immutable Objects

For *List*, *Set*, *Tuple*, and *Dictionary* objects name the variable in plural form for example foods, sports, list_of_things. So it's easy to loop the the element with singular form.

```py
foods = ['pizza', 'ice cream', 'pasta', 'burger']
for food in foods:
print(food)
```