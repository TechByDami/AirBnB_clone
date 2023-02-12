# 0x00. AirBnB clone - The console
 Foundations > Higher-level programming > AirBnB clone

..............................................................................
..............................................................................
 
 
## First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called [ BaseModel ]) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB ([ User, State, City, Place… ]) that inherit from [ BaseModel ]
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update

(hbnb)
(hbnb) 
(hbnb)quit
$ 
```

But also in non-interactive mode: (like the Shell project in C)

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
EOF  all  count  create  destroy  help  nothing  quit  show  update
(hbnb) 
$
```

All tests should also pass in non-interactive mode: 

> $ echo "python3 -m unittest discover tests" | bash
```
.......
----------------------------------------------------------------------
Ran 52 tests in 0.021s

OK
```


## Tasks

## 0. README, AUTHORS  [ README.md, AUTHORS ]
  Write a README.md:
  * description of the project
  * description of the command interpreter:
  how to start it
  how to use it
  * You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS)
  * You should use branches and pull requests on GitHub - it will help you as team to organize your work

## 1. Be PEP8 compliant!   [  ... ]

  Write beautiful code that passes the PEP8 checks. 

## 2. Unittests   [ tests/ ]
  All your files, classes, functions must be tested with unit tests
  > python3 -m unittest discover tests 
 **Warning:**
Unit tests must also pass in non-interactive mode:
  > echo "python3 -m unittest discover tests" | bash 
 
 
## 3. BaseModel  [ models/base_model.py, models/__init__.py, tests/ ]
  Write a class BaseModel that defines all common attributes/methods for other classes:
* [ models/base_model.py ]
* Public instance attributes:
   id: string - assign with an uuid when an instance is created:
   you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
   the goal is to have unique id for each BaseModel
[ created_at: ] datetime - assign with the current datetime when an instance is created
[ updated_at: ] datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
* __str__: should print: [<class name>] (<self.id>) <self.__dict__>
* Public instance methods:
[ save(self): ] updates the public instance attribute updated_at with the current datetime
[ to_dict(self): ] returns a dictionary containing all keys/values of __dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class name of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel 

 you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
> ./test_base_model.py

## 4. Create BaseModel from dictionary  [ models/base_model.py, tests/ ]
 Previously we created a method to generate a dictionary representation of an instance (method to_dict()).
 Now it’s time to re-create an instance with this dictionary representation.
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
> ./test_base_model_dict.py

## 5. Store first object  [ models/__init__.py, models/base_model.py, tests/ ]
  Now we can recreate a BaseModel from another one by using a dictionary representation:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'> 
```
Now the flow of serialization-deserialization will be:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
> ./test_save_reload_base_model.py

## 6. Console 0.0.1  [ console.py  ]
  Write a program called console.py that contains the entry point of the command interpreter:
* You must use the module cmd
* Your class definition must be: class HBNBCommand(cmd.Cmd):
* Your command interpreter should implement:
[ quit ] and [ EOF ] to exit the program
[ help ] (this action is provided by default by [ cmd ] but you should keep it updated and documented as you work through tasks)
a custom prompt: [ (hbnb) ]
an empty line + [ ENTER ] shouldn’t execute anything
* Your code should not be executed when imported
> ./console.py
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
$
```

## 7. Console 0.1    [ console.py ]
Update your command interpreter (console.py) to have these commands:
* [create] : Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
If the class name is missing, print ** class name missing ** (ex: $ create)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
* [show] : Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ show)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
* [destroy] : Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ destroy)
If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
* [all] : Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
The printed result must be a list of strings (like the example below)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
* [update] : Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
Usage: update <class name> <id> <attribute name> "<attribute value>"
If the class name is missing, print ** class name missing ** (ex: $ update)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com")
id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
> ./console.py
```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
...
show BaseModel 49faff9a-6318-451f-87b6-910505c55907
...
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
...
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
...
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```
## 8. First User  [ models/user.py, models/engine/file_storage.py, console.py, tests/ ]
  Write a class User that inherits from BaseModel:
* models/user.py
* Public class attributes:
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string
  Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.
> cat file.json ; echo ""
> ./test_save_reload_user.py

## 9. More classes!  [ models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/ ]
  Write all those classes that inherit from BaseModel:
* State (models/state.py):
Public class attributes:
name: string - empty string
* City (models/city.py):
Public class attributes:
state_id: string - empty string: it will be the State.id
name: string - empty string
* Amenity (models/amenity.py):
Public class attributes:
name: string - empty string
* Place (models/place.py):
Public class attributes:
city_id: string - empty string: it will be the City.id
user_id: string - empty string: it will be the User.id
name: string - empty string
description: string - empty string
number_rooms: integer - 0
number_bathrooms: integer - 0
max_guest: integer - 0
price_by_night: integer - 0
latitude: float - 0.0
longitude: float - 0.0
amenity_ids: list of string - empty list: it will be the list of Amenity.id later
* Review (models/review.py):
Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string

## 10. Console 1.0  [ console.py, models/engine/file_storage.py, tests/ ]
  Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

## 11. All instances by class name  [ console.py ]
  Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().
> $ ./console.py
>(hbnb) User.all()

## 12. Count instances   [ console.py ]
  Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().
$ ./console.py
(hbnb) User.count()
2
(hbnb) 

## 13. Show  [ console.py ]
  Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).
Errors management must be the same as previously.
$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.show("Holberton")
** no instance found **
(hbnb) 

## 14. Destroy  [ console.py ]
  Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).
Errors management must be the same as previously
$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Holberton")
** no instance found **
(hbnb) 

## 15. Update  [   ]
  Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).
Errors management must be the same as previously.
./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")

## 16. Update from dictionary   [ console.py ]
  Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).

Errors management must be the same as previously.
./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")


## 17. {'first_name': "John", "age": 89})   [ tests/test_console.py ] 

Contributors:
1. Agboola Olawale
2. Godwin Williams
..........................................................................................................................
