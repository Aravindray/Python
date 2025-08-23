# JSON in Python

JSON stands for JavaScript Object Notation

```json title:"syntax"
{
	"name": "Aravind",
	"age": 25,
	"city": "Salem"
}
```

We can use JSON as database since JSON is similar to python dictionary we can work with JSON file easy in python. But before we need to convert it appropriately for example:

**To convert JSON string to Python Dictionary use**

```py title:"JSON to Python"
json.loads(json_string)  # loads - s stand for string
```

**To convert Python Dictionary to JSON use**

```py title:"Python to JSON"
json.dumps(py_dict) # dumps - s stand for string
```