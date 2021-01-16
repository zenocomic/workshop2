#จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "I am the best programmer"
print(len(string))
#จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "I am the best programmer"
print(string[0])
#จงเขียนคำสั่งเพื่อแสดง "best" ของข้อความ "I am the best programmer"
print(string[9:12])
#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ไม่มี space
print(string.split(" "))
#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมใหญ่ทั้งหมด
print(string.upper())
#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมเล็กทั้งหมด
print(string.lower())
#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ถูกแทนที่อักษร e ด้วย z ทั้งหมด
print(string.replace("e", "z")) #gg ez
#จงเติมคำในช่องว่าเพื่อแสดงชื่อ
myname = "tatchai"
txt = "{} is the best programmer"
print(txt.format(myname))