
def list_subsract(lista, listb):
    rusult = [x - y for x, y in zip(lista, listb)]
    return rusult



"""
将输入SMPL的节点数据转换为BVH的节点数据
:param pose: TRAM的绝对节点数据
:return: BVH的相对节点数据
转换后的bvh节点数据矩阵每一行对应的JOINT与原来SMPLX模型数据矩阵每一行对应的JOINT相同
"""
# 参考TRAM第0帧骨架节点数据矩阵.png
# 参考SMPL默认节点数据--BVH数据点映射.png

def smplpose_to_bvhpose(pose):

    temple_pose = [[0, 0, 0] for _ in range(0, 24)]  # 使用二维列表推导表达式创建24x3列表矩阵
    temple_pose[-24] = [0,0,0]  # hips -24

    #print(f"{pose[0]}")                                                                        # CHK 查看TRAM输出骨架绝对坐标数据
    #print(f"hips -24:{temple_pose[-24]}\n")                                                    # CHK 查看写入BVH变量第一行数据
    for i in range(-22, -10, 3):
        if i == -22:
            temple_pose[i] = list_subsract(pose[0, i].tolist(), pose[0, -24].tolist())          # leftUpleg -22
            #print(f"leftUpleg -22:{temple_pose[i]}\n")                                         # CHK
            temple_pose[i - 1] = list_subsract(pose[0, i - 1].tolist(), pose[0, -24].tolist())  # rightUpleg -23
            #print(f"rightUpleg -23:{temple_pose[i-1]}\n")                                      # CHK
        else:
            temple_pose[i] = list_subsract(pose[0, i].tolist(), pose[0, i - 3].tolist())        # leftLowLeg -19 --- -13
            #print(f"leftLowLeg {i}:{temple_pose[i]}\n")                                        # CHK
            temple_pose[i - 1] = list_subsract(pose[0, i - 1].tolist(),pose[0, i - 4].tolist()) # rightLowLeg -20 --- -14
            #print(f"rightLowLeg {i-1}:{temple_pose[i-1]}\n")                                   # CHK

    for i in range(-21, -12, 3):
        if i == -21:
            temple_pose[i] = list_subsract(pose[0, i].tolist(), pose[0, -24].tolist())         # Spine1 -21
            #print(f"Spine1 -21:{temple_pose[i]}\n")                                           # CHK
        else:
            temple_pose[i] = list_subsract(pose[0, i].tolist(), pose[0, i - 3].tolist())       # Spine2 -18 ---  spine3 -15
            #print(f"Spine2/3 {i}:{temple_pose[i]}\n")                                          # CHK

    for i in range(-10, -4, 3):
        if i == -10:
            temple_pose[i - 2] = list_subsract(pose[0, i - 2].tolist(), pose[0, -15].tolist()) # neck -12
            #print(f"neck -12:{temple_pose[i-2]}\n")                                           # CHK
            temple_pose[i - 1] = list_subsract(pose[0, i - 1].tolist(), pose[0, -15].tolist()) # rightCollar -11

            #print(f"rightCollar -11:{temple_pose[i-1]}\n")                                    # CHK
            temple_pose[i] = list_subsract(pose[0, i].tolist(), pose[0, -15].tolist())         # leftCollar -10
            #print(f"leftCollar -10:{temple_pose[i]}\n")                                       # CHK

        else:
            temple_pose[i - 2] = list_subsract(pose[0, i - 2].tolist(), pose[0, i - 5].tolist())  # head -9
            #print(f"head -9:{temple_pose[i-2]}\n")                                               # CHK
            temple_pose[i - 1] = list_subsract(pose[0, i - 1].tolist(), pose[0, i - 4].tolist())  # rightUpArm -8
            #print(f"rightUpArm -8:{temple_pose[i-1]}\n")                                      # CHK
            temple_pose[i] = list_subsract(pose[0, i].tolist(), pose[0, i - 3].tolist())       # leftUpArm -7
            #print(f"leftUpArm -7:{temple_pose[i]}\n")                                         # CHK

    temple_pose[-5] = list_subsract(pose[0, -5].tolist(), pose[0, -7].tolist())                # leftfeLowArm -5
    #print(f"leftfeLowArm -5:{temple_pose[-5]}\n")                                             # CHK
    temple_pose[-6] = list_subsract(pose[0, -6].tolist(), pose[0, -8].tolist())                # rightfeLowArm -6
    #print(f"rightfeLowArm -6:{temple_pose[-6]}\n")                                            # CHK
    temple_pose[-1] = list_subsract(pose[0, -1].tolist(), pose[0, -5].tolist())                # leftHand -1
    #print(f"leftHand -1:{temple_pose[-1]}\n")                                                 # CHK
    temple_pose[-2] = list_subsract(pose[0, -2].tolist(), pose[0, -6].tolist())                # rightHand -2
    #print(f"rightHand -2:{temple_pose[-2]}\n")                                                # CHK
    temple_pose[-3] = list_subsract(pose[0, -3].tolist(), pose[0, -1].tolist())                # -3
    #print(f"-3:{temple_pose[-3]}\n")                                                          # CHK
    temple_pose[-4] = list_subsract(pose[0, -4].tolist(), pose[0, -2].tolist())                # -4
    #print(f"-4:{temple_pose[-4]}\n")                                                          # CHK
    #print(f"{temple_pose}")                                                                   # CHK
    return temple_pose
