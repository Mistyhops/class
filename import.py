from classCat import Cat

c1 = Cat('Барон', 'мальчик', '2 года')
c2 = Cat('Сэм', 'мальчик', '2 года')

print('Имя первого кота:', c1.name)
print('Пол первого кота:', c1.sex)
print('Возраст первого кота:', c1.age)
print('')
print('Имя второго кота:', c2.name)
print('Пол второго кота:', c2.sex)
print('Возраст второго кота:', c2.age)
print('-'*15)

print('Имя первого кота:', c1.getName())
print('Пол первого кота:', c1.getSex())
print('Возраст первого кота:', c1.getAge())
print('')
print('Имя второго кота:', c2.getName())
print('Пол второго кота:', c2.getSex())
print('Возраст второго кота:', c2.getAge())












