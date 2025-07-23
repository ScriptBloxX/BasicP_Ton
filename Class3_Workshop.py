#เฉลย Workshop class 3!
zombie = 100
bow = 15
gun = 100
axe = 85

while True:
    choose = input("1 Fight , 2 Exit: ")
    if choose == "1":
        print("Fight")
        attack_round = int(input("เลือกว่าจะโจมตีกี่รอบ: "))
        for i in range(attack_round):
            weapon = input("Press to choose your weapons -> bow / gun / axe: ")
            if weapon == "bow":
                zombie-=bow
            elif weapon == "gun":
                zombie-=gun
            elif weapon == "axe":
                zombie-=axe
            else:
                print("ไม่เลือกอาวุธ")
            print("HP ->",zombie)
            if zombie == 0:
                print("Zombie ตายแล้ววว")
                break
            elif zombie < 0:
                zombie = 20
                print("HP ติดลบ ตั้งค่า HP ใหม่เป็น:",zombie)
        if zombie > 0:
            print("จบรอบแล้ว Player ตาย")
        break        
    elif choose == "2":
        print("Exit")
        break
