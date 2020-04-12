# Get People Budget Exercise

In this exercise you have to write code in the file `getBudget.py` for calculating the budget of a list of people.

Each person will be represented by the dictionary object: 

```python
{ 
  name: "John",
  age: 21,
  budget: 23000 
},
```

and the `people` variable will hold a list of different multiple persons.

You should write the code inside the block from the method, and delete **pass** keyword, where it says `Your amazing code here`.

## Examples

```python
getBudgets([
  { name: "John", age: 21, budget: 23000 },
  { name: "Steve",  age: 32, budget: 40000 },
  { name: "Martin",  age: 16, budget: 2700 }
]) ➞ 65700

getBudgets([
  { name: "John",  age: 21, budget: 29000 },
  { name: "Steve",  age: 32, budget: 32000 },
  { name: "Martin",  age: 16, budget: 1600 }
]) ➞ 62600
```

## Local Test

For testing your code you must run: 

```sh
pytest

```

## Notes:

- You can read the test files, so you can have an idea of what is the expected result, but **do not edit them** please.

- The result must be a *Number*.

- **Extra points** if you use list-comprehension 😏

If you have any doubts, feel free to ask 😊

Good luck! 🚀

Made with 💚 for Hackademy 🇲🇽.