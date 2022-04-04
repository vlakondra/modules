# modules
learn modules


## Обязательно добавить Python-extension

## Создать 2 файла в папке scripts:
- script1.py
- script2.py

В файле  script2.py создать константу и функцию.
```
LEARN_MOD = 'Изучаем модули.  Script1.py'

def print_arg( x : int): 
    '''Печатаем аргумент функции
    '''
    print(f"Печатаем arg: {x}. Script1.py")
```

В файле script2.py импортировать модуль script1 и использовать его
элементы:

```
import script1
#импортируем и используем script1

print(script1.LEARN_MOD)
script1.print_arg()
```
#### Вызов
```
python scripts/script2.py
```
