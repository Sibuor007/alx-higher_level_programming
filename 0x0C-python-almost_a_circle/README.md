Python - Almost a circle

In this project, I applied Python object-oriented programming skills by
	implementing three interconnected classes to represent rectangles and
	squares. I developed a custom test suite using the `unittest` module to
	verify the functionality of each class.

The three classes utilized various Python tools, including import statements,
	exception handling, private attributes, getter/setter methods,
	class/static methods, inheritance, file input/output (I/O), `args` and
	`kwargs` usage, as well as JSON and CSV serialization/deserialization.
	Unittesting was employed to ensure the correctness of the implemented classes.

Tests:
- tests/test_models: This folder contains independently-developed test files.
  - test_base.py
  - test_rectangle.py
  - test_square.py

Classes:

Base:
Represents the base class for all other classes in the project.
	It includes private class attribute `__nb_objects = 0`, a public instance
	attribute `id`, and a class constructor. Other features include static
	methods for JSON string serialization, class methods for saving/loading
	objects to/from files, and methods for CSV serialization/deserialization.
	Additionally, there is a static method for drawing rectangles and squares
	in a GUI window using the `turtle` module.

Rectangle:
Represents a rectangle and inherits from the `Base` class.
	It features private instance attributes `__width`, `__height`, `__x`, and
	`__y`, each with its own getter/setter methods. The class constructor
	validates input attributes, and methods include area calculation,
	displaying the rectangle on `stdout`, updating attributes, and converting
	the object to a dictionary.

Square:
Represents a square and inherits from the `Rectangle` class.
	The class constructor is adjusted to set both width and height using the
	`size` attribute. Additional methods for updating and converting to a
	dictionary are implemented.
