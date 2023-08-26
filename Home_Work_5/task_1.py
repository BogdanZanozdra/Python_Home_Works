# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.


def file_info(path: str) -> tuple:
    *_, file = path.split('\\')
    name, extension = file.split('.')
    res = (path, name, extension)
    return res


print(file_info('C:\\Users\\User\\PycharmProjects\\pythonProject\\Home_Works\\Home_Work_5\\task_2.py'))

