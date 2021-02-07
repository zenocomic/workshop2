#1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while

multitable = 12
while multitable >= 2:
    print("   [{}]".format(multitable))
    value = 1
    while value < 12:
        print("{} * {} : {}".format(multitable, value, value * multitable))
        value += 1
    multitable -= 1
    print("-----------------")
#2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
set = 12
for multitable in range(2, 13):
    print("   [{}]".format(set))
    for value in range(1, 13):
        print("{} * {} : {}".format(set, value, value * set))
    set -= 1    
    print("-----------------")