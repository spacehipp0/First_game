balls = [1, 2, 3, 4]
weapons = [11, 22 ,3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("ball :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons : ", weapon_val)
        if ball_val == weapon_val: #충돌 체크
            print("공과무기가 충돌")
            break 

    else:
        continue
    break

    # if 조건 : 
    #     동작
    # else:
    #     그 외의 동작

# for 바깥조건:
#     바깥동작
#     for 안쪽조건:
#         안쪽동작
#         if 충돌하면:
#             break
#     else:
#         continue
#     break