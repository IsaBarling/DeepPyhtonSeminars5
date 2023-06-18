# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def split_path(abs_path: str) -> tuple:
    list_abs_path = abs_path.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[:-1])
    name = list_last_elem[0]
    extension = list_last_elem[1]
    return path, name, extension

abs_path = r'D:\IT theory\pytthon\Python-1.pdf'
print(split_path(abs_path))

