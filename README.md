#0x00. AirBnB clone - The console
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

And also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

### List of commands :scroll:

- create: Creates a new instance of the selected class, saves it (to the JSON file) and prints the id. Usage: create classname. Example:

```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```

- show: Prints the string representation of an instance based on the class name and id. Usage: show classname id or classname.show(id in string format). Example:

```
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) BaseModel.show(49faff9a-6318-451f-87b6-910505c55907)
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

- destroy: Deletes an instance based on the class name and id, and saves the change into the JSON file. Usage: destroy classname id or classname.destroy(id in string format). Example:

```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) BaseModel.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) show BaseModel 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
** no instance found **
```

- all: Prints all string representation of all instances based or not on the class name. Usage: all classname or classname.all() or all. Example:

```
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) BaseModel.all()
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

- update: Updates an instance based on the class name and id by adding or updating attribute, and saves the changes into the JSON file. Usage: update classname id attributename attributevalue or classname.update(id, attributename, attribute value in string format). Example:

```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
```

update also works with a dictionary as an input. Usage: classname.update(id in string format, dictionary)

```
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
```

- count: returns the number of instances of a class. Usage: classname.count(). Example:

```
(hbnb) User.count()
2
```

- To exit the console you can use quit or EOF commands:

```
(hbnb) quit
$ 
```
or
```
(hbnb) EOF

$
```

## Database - storage :package:  

First abstracted storage engine of the project: File storage.

Every time is launched the program, this restores all objects created before. Storing them into a file named 'file.json'.

-   Python doesn’t know how to convert a string to a dictionary (easily)
-   It’s not human readable
-   Using this file with another program in Python or other language will be hard.

So, because of that are converted the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

## Tests :heavy_check_mark:

### 2. Unittests

All the files, classes, functions are tested with unit tests

```
python3 -m unittest discover tests
```



Unit tests also work in non-interactive mode:

```
echo "python3 -m unittest discover tests" | bash

