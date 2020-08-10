from polygon import Polygon
import inspect


# object_args = (
#     (5,10)
#     ,(5,10)
#     ,(6,12)
# )

object_args = [
    (number1, number2) for number1 in range(6,9) for number2 in range(10,13)
]

print(f'args: {object_args}')

objects = [Polygon(arg1, arg2) for (arg1, arg2) in object_args]

for object_ in objects:
    print(object_)
    for item, value in inspect.getmembers(object_):
        if not item.startswith('_'):
            print(f'\t{item}: {value}')
    print('-' * 40)