import getBudget

def test_get_budget_one():
    assert getBudget.getTotalBudget(
        [{
            'name': "John",
            'age': 21,
            'budget': 23000
        },
        {
            'name': "Steve",
            'age': 32,
            'budget': 40000
        },
        {
            'name': "Martin",
            'age': 16,
            'budget': 2700
        }]) == 65700

def test_get_budget_two():
    assert getBudget.getTotalBudget(
        [{
            'name': "John",
            'age': 21,
            'budget': 29000
        },
        {
            'name': "Steve",
            'age': 32,
            'budget': 32000
        },
        {
            'name': "Martin",
            'age': 16,
            'budget': 1600
        }]) == 62600

def test_get_budget_three():
    assert getBudget.getTotalBudget(
        [{
            'name': "John",
            'age': 21,
            'budget': 19401
        },
        {
            'name': "Steve",
            'age': 32,
            'budget': 12321
        },
        {
            'name': "Martin",
            'age': 16,
            'budget': 1204
        }]) == 32926

def test_get_budget_four():
    assert getBudget.getTotalBudget(
        [{
            'name': "John",
            'age': 21,
            'budget': 10234
        },
        {
            'name': "Steve",
            'age': 32,
            'budget': 21754
        },
        {
            'name': "Martin",
            'age': 16,
            'budget': 4935
        }]) == 36923