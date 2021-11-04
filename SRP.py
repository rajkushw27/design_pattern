import os


class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text: str) -> None:
        self.count += 1
        text = text.rstrip()
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, index: int) -> None:
        del self.entries[index]
        self.count -= 1

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # def save(self, filename: str) -> None:
    #     with open(filename, 'w') as f:
    #         f.write(str(self))

    # def load(self, filename: str) -> None:
    #     with open(filename) as f:
    #         for line in f.readlines():
    #             self.add_entry(line)
    #     self.count = len(self.entries)

    # def load_from_web(self, url: str) -> None:
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal: Journal, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(str(journal))


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')

file = os.path.curdir + '/journal.txt'

PersistenceManager.save_to_file(j, file)

with open(file) as f:
    print(f.read())

# j.load("sample.txt")
#print(f'Journal Entries:\n{j}')
