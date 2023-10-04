# f = open('1.txt')
# s = f.readline() + '***'
# # Определите количество AF-подстрок длиной от 7 до 10 символов.
# # '***' чтобы не выйти за ранж, с ними последние 6 элементов строки мы все равно проверяем
# # идем по строке. если текущий символ А, то ищем символ на расстоянии 6-9 от него
# cnt = 0
# for i in range(len(s) - 9):
#     if s[i] == 'A' and s[i +6] == 'F':
#         cnt += 1
#     if s[i] == 'A' and s[i +7] == 'F':
#         cnt += 1
#     if s[i] == 'A' and s[i +8] == 'F':
#         cnt += 1
#     if s[i] == 'A' and s[i + 9] == 'F':
#         cnt += 1
# print(cnt)

# f = open('1.txt')
# s = f.readline().split('A')[1:]
# minn = 10**6
# # срезом убираем первый эоемент, который всегда начинается НЕ с А
# for x in s:
#     k = x.find('F')
#     # например CCDF индекс F == 3, а длина строки включая А == 5, поэтому к + 2
#     if k + 2 < minn and k != 0 and k != -1:
#         minn = k + 2
# print(minn)

# f = open('1.txt')
# s = f.readline().split('D')[1:-1]
# # первый и последний элемент не будет заканчиваться D, поэтому срез делаем
# minn = 10**6
# for x in s:
#     k = len(x)
#     if k  != 0 and k < minn:
#         minn = k
# print(minn + 2)

# f = open('1.txt')
# s = f.readline()
# k = 0
# minn = 10**6
# for x in s:
#     if x == 'D':
#         k += 1
#     else:
#         if k != 0:
#             minn = min(minn, k)
#         k = 0
# print(minn)

# f = open('1.txt')
# s = f.readline()
# cnt = 0
# for i in range(len(s)//2):
#     # чтобы два раза одно и то же число не считать дважды, то в ранже делим на 2
#     if s[i] == s[-i-1]:
#         cnt += 1
# print(cnt)

# f = open('1.txt')
# s = f.readline()
# cnt_palindrome = 0
# for i in range(len(s) - 4):
#     if s[i:i+5] == s[i:i+5][::-1]:
#             # в срезе до i+5(а не i+4), потому что мы доолжны включая последний элемент отбирать числа
#         cnt_palindrome += 1
# print(cnt_palindrome)

# f = open('1.txt')
# s = f.readline()
# k = 1
# maxx = 0
# for i in range(len(s) - 1):
#     if s[i] < s[i+1]:
#         k += 1
#         if k > maxx:
#             maxx = k
#     else:
#         k = 1
# print(maxx)

# f = open('1.txt')
# s = f.readline()
# k = 1
# num = 0
# maxx = 0
# for i in range(len(s) - 1):
#     if s[i] < s[i+1]:
#         k += 1
#         if k > maxx:
#             num = i + 1 - k + 1 + 1
#             maxx = k
#     else:
#         k = 1
# print(num)

