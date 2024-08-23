import math
import numpy as np
import torch



# Checks if a matrix is a valid rotation matrix.
# 输入numpy数组
def isRotationMatrix(R) :
    # 将python类型转化为ndraay对象
    R = np.asarray(R)
    # print(type(R))                                   #CHK
    # 函数计算矩阵R的转置Rt
    Rt = np.transpose(R)
    # 计算Rt和R的点积
    shouldBeIdentity = np.dot(Rt, R)
    # 计算I与shouldBeIdentity之间的差的Frobenius范数（元素平方和的平方根），结果存储在n中
    I = np.identity(3, dtype = R.dtype)
    # 计算I与shouldBeIdentity之间的差的Frobenius范数，结果存储在n中
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6

# Calculates rotation matrix to euler angles
# 返回ndarray对象
def rotationMatrixToEulerAngles(R) :
    assert(isRotationMatrix(R))
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
    singular = sy < 1e-6
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
    return np.array([x, y, z])



def rotate_matrix2Euler_angle(dic):
    """
    :param rotate_matrix: 3*3 rotation matrix
    :return: 3*1 Euler angle
    """
    # 目的,使用外循环结构遍历所有帧维度，然后在开一个循环遍历24个关节，在开一个循环遍历矩阵
    rotate_matrix_4 = dic['pred_rotmat']
    # 字典的键值对，其值存储的是torch.Tensor类，使用tensor类的索引方法
    #print(type(rotate_matrix_4))
    #print(type(rotate_matrix_4.shape[0]))
    for i in range(0,rotate_matrix_4.shape[0]):
        # 帧遍历
        # print(rotate_matrix_4[i, :, ])
        EulerAngles = ''
        for j in range(0,rotate_matrix_4.shape[1]):
            # 遍历每一帧的每一个节点3x3矩阵
            # print(rotate_matrix_4[i, j, :, :])                           # CHK：查看旋转矩阵数据
            # print(type(rotate_matrix_4[i, j, :, :].tolist()))            # CHK：查看数据类型
            temp = rotationMatrixToEulerAngles(rotate_matrix_4[i, j, :, :]).tolist()
            for k in range(0,3):
                if k == 2:
                    EulerAngles = EulerAngles+str(temp[k])
                else:
                    EulerAngles = EulerAngles+str(temp[k])+' '
        # print(EulerAngles)
    return EulerAngles







def transform(path,):
    file_path = path                              # 楼层的层级结构思想,只有嵌套文件夹能加深层级
    data = np.load(file_path, allow_pickle=True)  # allow_pickle=True 表示读取的npy文件为复杂的py对象转换而来的
    data = data.item()
    results = rotate_matrix2Euler_angle(data)
    return results



