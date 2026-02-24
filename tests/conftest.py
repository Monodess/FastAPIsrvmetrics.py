pytest_plugins = [
    "tests.data_mocks.mock_orm_obj",
    "tests.data_mocks.mock_data"
]
#pluggy lib says hi
#what a magic for pytest to seek for specifically named module
#and take in the same way specifically called variable

class Parent:
    # __slots__ = ("x", "y")
    def __init__(self, rank):
        self.Rank = rank

class Object(Parent):

    def __init__(self, name, rank):
        super().__init__(rank)
        self.Name = "Hoe"

print(Parent(rank=1).__dict__.values())
print(Object(name="Hoe", rank=24).__dict__.pop("Name"))
print(Object(name="Hoe", rank=24).__dict__.pop("Rank"))
obj = Object(name="Hoe", rank=24)
# obj.__dict__.pop("Rank")
print(obj.__dict__)
obj.__dict__.popitem()
print(obj.__dict__)

