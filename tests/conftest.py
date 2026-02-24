pytest_plugins = [
    "tests.data_mocks.mock_orm_obj",
    "tests.data_mocks.mock_data"
]
#pluggy lib says hi
#what a magic for pytest to seek for specifically named module
#and take in the same way specifically called variable
class Parent(object):
    def __init__(self, rank):
        self.Rank = rank

    Rank: int
class Object(Parent):
    Name: str
    def __init__(self, name, rank):
        self.Name = "Hoe"
        super.__init__(Object, self, rank=2)

print(Object(name="Hoe", rank=2).__dict__)
