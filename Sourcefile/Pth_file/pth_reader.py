"""
这是一个用于预览pth文件数据或者输出pth文件输出的子程序
"""

import torch

# 加载.pth文件
j3d = torch.load('j3d.pth')  # 人体骨架数据
pose = torch.load('pose.pth') # 姿态偏转数据
vert = torch.load('vert.pth') # 3D点数据
def privew_model(j3d,pose,vert):
    print(j3d)
    print(pose)
    print(vert)




def save_model(j3d,pose,vert):
    with open(r'preivew_data/j3d.txt', 'w') as f:
        for param_tensor in j3d:
            f.write(str(param_tensor.size()) + '\n')
            f.write(str(param_tensor) + '\n')
            f.write("\n")
    with open(r'preivew_data/pose.txt', 'w') as f:
        for param_tensor in pose:
            f.write(str(param_tensor.size()) + '\n')
            f.write(str(param_tensor) + '\n')
            f.write("\n")
    with open(r'preivew_data/vert.txt', 'w') as f:
        for param_tensor in vert:
            f.write(str(param_tensor.size()) + '\n')
            f.write(str(param_tensor) + '\n')
            f.write("\n")


if __name__ == '__main__':
    privew_model(j3d,pose,vert)
    save_model(j3d,pose,vert)