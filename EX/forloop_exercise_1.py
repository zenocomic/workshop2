# จงเขียนคำสั่งเพื่อแสดงต้น christmas โดยใช้คำสั่ง for โปรแกรมสามารถกำหนดความสูงของต้น christmas ได้
n = int(input("height = "))
for i in range(n):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i+n-j):
        print('*', end='')
    print('')