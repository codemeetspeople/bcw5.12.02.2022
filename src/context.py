class open_file:
    def __init__(self, file_name, mode):
        self._file_name = file_name
        self._mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name, self._mode)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


if __name__ == '__main__':
    with open_file('task.in', 'r') as source:
        data = source.read()

    data = data.lower().capitalize()

    with open_file('task.out', 'w') as destination:
        destination.write(data)
