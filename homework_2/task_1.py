class CyclicIterator:
    def __init__(self, container):
        self.container = container
        self.iter_container = iter(self.container)

    def __iter__(self):
        return self.iter_container

    def __next__(self):
        try:
            return next(self.iter_container)
        except StopIteration:
            print('h')
            return 'hoi'


def main():
    collections = [
        range(1, 4),
    ]
    for collection in collections:
        _range = CyclicIterator(collection)
        for i in _range:
            print(i)


main()
