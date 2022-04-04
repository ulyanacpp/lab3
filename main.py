from stack import Stack


class SortT:
    def __init__(self):
        self._input_data = Stack()
        self._way_one = Stack()
        self._way_two = Stack()

    def input_data_from_keyboards(self):
        while True:
            try:
                value = int(input('Введите 1 - первый тип, 2 - второй тип, 3 - для завершения> '))
                if value == 3:
                    return
                if value != 1 and value != 2:
                    print('Вводить надо цифры от 1 до 3!!!!')
                else:
                    self._input_data.push(value)
            except ValueError:
                print('ЦИФРЫ НАДО ВВОДИТЬ, А НЕ БУКВЫ')

    def input_from_file(self, file_path):
        with open(file_path, ) as file:
            for word in file:
                self._input_data.push(int(word))

    def sort_train(self):
        for train in self._input_data:
            if train == 1:
                self._way_one.push(train)
            else:
                self._way_two.push(train)

    def print_result(self):
        print('Путь первый')
        for way_one in self._way_one:
            print(way_one)

        print('Путь второй')
        for way_two in self._way_two:
            print(way_two)


if __name__ == '__main__':
    sort_t = SortT()
    sort_t.input_from_file("train.txt")
    sort_t.sort_train()
    sort_t.print_result()

