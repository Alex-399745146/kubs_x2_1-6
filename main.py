import random
counter = 0
a = random.randint(1, 6)
b = random.randint(1, 6)
print()
print()
if a == 1:
    print(' _______')
    print('|       |')
    print('|   *   |    ', a)
    print('|       |')
    print(' -------')
elif a == 2:
    print(' _______')
    print('| *     |')
    print('|       |    ', a)
    print('|     * |')
    print(' -------')
elif a == 3:
    print(' _______')
    print('| *     |')
    print('|   *   |    ', a)
    print('|     * |')
    print(' -------')
elif a == 4:
    print(' _______')
    print('| *   * |')
    print('|       |    ', a)
    print('| *   * |')
    print(' -------')
elif a == 5:
    print(' _______')
    print('| *   * |')
    print('|   *   |    ', a)
    print('| *   * |')
    print(' -------')
else:
    print(' _______')
    print('| *   * |')
    print('| *   * |    ', a)
    print('| *   * |')
    print(' -------')
if a == b:
    print('========= КУШ:', a, a, a, a)
    counter = a * 4
else:
    print('=========')
if b == 1:
    print(' _______')
    print('|       |')
    print('|   *   |    ', b)
    print('|       |')
    print(' -------')
elif b == 2:
    print(' _______')
    print('| *     |')
    print('|       |    ', b)
    print('|     * |')
    print(' -------')
elif b == 3:
    print(' _______')
    print('| *     |')
    print('|   *   |    ', b)
    print('|     * |')
    print(' -------')
elif b == 4:
    print(' _______')
    print('| *   * |')
    print('|       |    ', b)
    print('| *   * |')
    print(' -------')
elif b == 5:
    print(' _______')
    print('| *   * |')
    print('|   *   |    ', b)
    print('| *   * |')
    print(' -------')
else:
    print(' _______')
    print('| *   * |')
    print('| *   * |    ', b)
    print('| *   * |')
    print(' -------')
if counter != 0:
    print('ВСЕГО ХОДОВ ПРИ ВЫПОДЕНИИ КУША:', counter, 'раз')
print()
print()
