nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
nested_list2 = [['a', 'b', 'c', ['d', 'e', 'f', 'h', False, [1, 2, ['x', 'y', 'z'], None]]],
                ['d', 'e', 'f', 'h', False], [1, 2, None]]
nested_list3 = [[['a', 'b', 'c'], ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2']], [['d', 'e', 'f', 'h', False],
                ['d1', 'e1', 'f1', 'h1', False], ['d2', 'e2', 'f2', 'h2', False], ['d3', 'e3', 'f3', 'h3', False],
                ['d4', 'e4', 'f4', 'h4', False]], [1, 2, None]]


# Задание 1 (итератор для двухуровневого списка)
class FlatIterator:
    def __init__(self, two_level_list):
        self.two_level_list = two_level_list

    def __iter__(self):
        self.next_list = iter(self.two_level_list)
        self.next_item = iter([])
        return self

    def __next__(self):
        if self.next_list is None:
            raise StopIteration
        try:
            result = next(self.next_item)
        except StopIteration:
            list1 = next(self.next_list)
            self.next_item = iter(list1)
            result = next(self.next_item)
        return result


# Задание 2 (генератор для двухуровневого списка)
def flat_generator(two_level_list):
    for list_ in two_level_list:
        for item_ in list_:
            yield item_


# Подсказка из интернета - функция рекурсивного разворачивание списка. Навело на решение 4*
# def flatten(s):
#     if s == []:
#         return s
#     if isinstance(s[0], list):
#         return(flatten(s[0]) + flatten(s[1:]))
#     return(s[:1] + flatten(s[1:]))


# Попытка задания 3*. Разворачивание в плоский список списка любого уровня вложенности с помощью класса итератора.
# (не работает)
class FlatIteratorManyLevel:
    def __init__(self, many_level_list):
        self.many_level_list = many_level_list

    def __iter__(self):
        self.next_list = iter(self.many_level_list)
        self.next_item = iter([])
        return self

    def __next__(self):
        if self.next_list is None:
            raise StopIteration
        try:
            result = next(self.next_item)
        except StopIteration:
            list1 = next(self.next_list)
            self.next_item = iter(list1)
            result = next(self.next_item)
        if isinstance(result, list):  # ?? Как-то нужно обработать это условие, попытался через рекурсию
            x = FlatIteratorManyLevel(result).__iter__()
            return x.__next__()
        return result


# Задание 4*. Разворачивание в плоский список списка любого уровня вложенности с помощью функции генератора.
def flat_generator_many_level(many_level_list):
    for item_ in many_level_list:
        if isinstance(item_, list):
            yield from flat_generator_many_level(item_)
        else:
            yield item_


if __name__ == '__main__':
    # Задание 1. (Вывод двухуровневого списка с помощью класса итератора)
    print('Задание 1')
    for item in FlatIterator(nested_list):
        print(item, end=' ')

    print()
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print()

    # Задание 2. (Вывод двухуровневого списка с помощью функции генератора)
    print('Задание 2')
    for item in flat_generator(nested_list):
        print(item, end=' ')
    print()
    print()

    # Задание 3*. Не работает.
    print('Задание 3* (не работает)')
    print('nested_list2')
    for item in FlatIteratorManyLevel(nested_list2):
        print(item, end=' ')
    print()
    print('nested_list3')
    for item in FlatIteratorManyLevel(nested_list3):
        print(item, end=' ')
    print()
    print()

    # Задание 4*. Работает.
    print('Задание 4* (работает верно)')
    print('nested_list2')
    for item in flat_generator_many_level(nested_list2):
        print(item, end=' ')
    print()
    print('nested_list3')
    for item in flat_generator_many_level(nested_list3):
        print(item, end=' ')

