import math
import numpy as np




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
# 返回ndarray对象,输入(YZX)旋转矩阵输出X-Z-Y偏转欧拉角(角度制)
# 问题：猜测的旋转矩阵有24组数据，但是实际需要的就是19组的相对旋转数据，所以得从那24组筛选出正确的19组
# 问题：我猜测那个旋转矩阵是YZX型，但是初步验证似乎是错的
# 分析：先查找资料查找这个pred_rotmat数据的旋转矩阵类型，在去筛选出正确的19行
def rotationMatrixToEulerAngles(R) :
    assert(isRotationMatrix(R))

    # 返回的是弧度制角度
    x = math.atan(R[1,0]/R[0,0])
    y = math.atan(-R[2,0]/math.sqrt(1-R[2,0]**2))
    z = math.atan(R[2,1]/R[2,2])

    x = x*180/math.pi
    y = y*180/math.pi
    z = z*180/math.pi


    return np.array([z, y, x])





"""
输入：
    运动数据
功能：
    输出排列好的运动数据
"""
def write_rotate(dic):
    """
    :param rotate_matrix: 3*3 rotation matrix
    :return: 3*1 Euler angle
    """
    # 目的,使用外循环结构遍历所有帧维度，然后在开一个循环遍历24个关节，在开一个循环遍历矩阵
    rotate_matrix_4 = dic['pred_rotmat']
    # 字典的键值对，其值存储的是torch.Tensor类，使用tensor类的索引方法
    #print(type(rotate_matrix_4))
    #print(type(rotate_matrix_4.shape[0]))
    EulerAngles = ''
    for i in range(0,rotate_matrix_4.shape[0]):
        # 帧遍历
        # print(rotate_matrix_4[i, :, ])

        for j in range(0,rotate_matrix_4.shape[1]):
            # 遍历每一帧的每一个节点3x3矩阵
            # print(rotate_matrix_4[i, j, :, :])                           # CHK：查看旋转矩阵数据
            # print(type(rotate_matrix_4[i, j, :, :].tolist()))            # CHK：查看数据类型
            temp = rotationMatrixToEulerAngles(rotate_matrix_4[i, j, :, :]).tolist()
            for k in range(0,3):
                if k == 2:
                    EulerAngles = EulerAngles+str(temp[k])+' '
                else:
                    EulerAngles = EulerAngles+str(temp[k])+' '
        EulerAngles = EulerAngles+'\n'
        #print(EulerAngles)
    #print(EulerAngles)
    return EulerAngles



def transform(path):
    file_path = path                              # 楼层的层级结构思想,只有嵌套文件夹能加深层级
    data = np.load(file_path, allow_pickle=True)  # allow_pickle=True 表示读取的npy文件为复杂的py对象转换而来的
    data = data.item()
    results = write_rotate(data)
    return results




"""
测试代码
"""

if __name__ == '__main__':
    path = r'../Sourcefile/vimo_track_0.npy'
    results = transform(path)
    with open('../Outputfiles/transformed_rotate_data.txt', 'w') as f:
        f.write(results)



