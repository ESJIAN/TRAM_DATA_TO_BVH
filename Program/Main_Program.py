"""
运行环境:
torch版本为2.4.0
python版本为3.10
numpy版本1.23.5
scipu版本1.14.0
"""
import torch
import rotate_matrix2Euler_angle
from smplpose2bvhpose import smplpose_to_bvhpose
from writepose import  write_pose

origin_pose = torch.load("../Sourcefile/Pth_file/j3d.pth", weights_only=True)  # 读取节点坐标文件 （笛卡尔坐标系节点位置的tensor矩阵数据）
rotate = torch.load("../Sourcefile/Pth_file/pose.pth", weights_only=True)      # 读取旋转文件 （笛卡尔坐标系节点位置的每个节点欧拉相对偏转角）

# 创建BVH文件结构
global global_sample
bvh_header = """                
HIERARCHY
Root Hips
{
    01OFFSET 0.0 0.0 0.0 
    CHANNELS 6 Xposition Yposition Zposition Xrotation Yrotation Zrotation
    JOINT RightUpLeg
    {
        02OFFSET 0.0 0.0 0.0 
        CHANNELS 3 Xrotation Yrotation Zrotation
        JOINT RightLeg
        {
            05OFFSET 0.0 0.0 0.0 
            CHANNELS 3 Xrotation Yrotation Zrotation
            JOINT RightFoot
            {
                08OFFSET 0.0 0.0 0.0 
                CHANNELS 3 Xrotation Yrotation Zrotation
                End Site
                {
                    11OFFSET 0.0 0.0 0.0 
                }
            }
        }
    }
    JOINT LeftUpLeg
    {
        03OFFSET 0.0 0.0 0.0 
        CHANNELS 3 Xrotation Yrotation Zrotation
        JOINT LeftLeg
        {
            06OFFSET 0.0 0.0 0.0 
            CHANNELS 3 Xrotation Yrotation Zrotation
            JOINT LeftFoot
            {
                09OFFSET 0.0 0.0 0.0 
                CHANNELS 3 Xrotation Yrotation Zrotation
                End Site
                {
                    12OFFSET 0.0 0.0 0.0 
                }
            }
        }
    }
    JOINT Spine1
    {
        04OFFSET 0.0 0.0 0.0 
        CHANNELS 3 Xrotation Yrotation Zrotation
        JOINT Spine2
        {
            07OFFSET 0.0 0.0 0.0 
            CHANNELS 3 Xrotation Yrotation Zrotation
            JOINT Spine3
            {
                10OFFSET 0.0 0.0 0.0 
                CHANNELS 3 Xrotation Yrotation Zrotation
                JOINT Neck
                {
                    13OFFSET 0.0 0.0 0.0 
                    CHANNELS 3 Xrotation Yrotation Zrotation
                    End Site
                    {
                        16OFFSET 0.0 0.0 0.0 
                    }
                }
                JOINT LeftShoulder
                {
                    15OFFSET 0.0 0.0 0.0 
                    CHANNELS 3 Xrotation Yrotation Zrotation
                    JOINT LeftArm
                    {
                        18OFFSET 0.0 0.0 0.0 
                        CHANNELS 3 Xrotation Yrotation Zrotation
                        JOINT LeftForeArm
                        {
                            20OFFSET 0.0 0.0 0.0 
                            CHANNELS 3 Xrotation Yrotation Zrotation
                            JOINT LeftHand
                            {
                                24OFFSET 0.0 0.0 0.0 
                                CHANNELS 3 Xrotation Yrotation Zrotation
                                End Site
                                {
                                    22OFFSET 0.0 0.0 0.0 
                                }
                            }
                        }
                    }
                }
                JOINT RightShoulder
                {
                    14OFFSET 0.0 0.0 0.0 
                    CHANNELS 3 Xrotation Yrotation Zrotation
                    JOINT RightArm
                    {
                        17OFFSET 0.0 0.0 0.0 
                        CHANNELS 3 Xrotation Yrotation Zrotation
                        JOINT RightForeArm
                        {
                            19OFFSET 0.0 0.0 0.0 
                            CHANNELS 3 Xrotation Yrotation Zrotation
                            JOINT RightHand
                            {
                                23OFFSET 0.0 0.0 0.0 
                                CHANNELS 3 Xrotation Yrotation Zrotation
                                End Site
                                {
                                    21OFFSET 0.0 0.0 0.0 
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
MOTION
Frames: {num_frames}
Frame Time: {frame_time}
    """







# def write_rotate(rotate, sample):
#     character = ""
#     print(f"{rotate[0,0,:]}")                    #
#     for i in range(0, rotate.shape[0]):          # 遍历纵向旋转数据
#         #print(str(rotate.shape[0]))             # CHK：查看帧位置
#         for j in range(0, rotate.shape[1]):      # 遍历行旋转数据
#             #print(str(rotate.shape[1]))         # CHK：查看行位置
#             for k in range(0, rotate.shape[2]):  # 遍历列旋转数据
#                 #print(str(rotate.shape[2]))     # CHK：查看列位置
#                 list_temp_rotate = rotate[i, j, k].tolist()
#                 #print(list_temp_rotate)         # CHK：查看拼接的旋转欧拉角1x3矩阵
#                 character = character + str(list_temp_rotate) + ' '
#             #print(f"旋转数据写入进度：{(i + 1) / (rotate.shape[0] + 1) * 100:.1f}%")
#
#         character = character + '\n'
#         character = character + ''
#     return sample + character

def write_rotate(path , sample):
    result = rotate_matrix2Euler_angle.transform(rotate)
    result = sample + result
    return result




"""
函数入口
"""
if __name__ == "__main__":
    #print(f"{origin_pose[0,:,:]}")                           # CHK:查看24个关节的绝对笛卡尔坐标系值

    # 将SMPL默认模型的24个绝对笛卡尔坐标系值转化为相对值
    pose = smplpose_to_bvhpose(origin_pose)

    # 写入起始位姿数据
    print("写入骨架数据\n")
    global_sample = write_pose(pose, bvh_header)
    print("骨架建立完毕\n")
    # 写入旋转数据
    print("写入旋转数据\n")
    global_sample = write_rotate(rotate, global_sample)
    print("旋转数据写入完毕\n")
    # 写入帧数
    print("写入帧数\n")
    global_sample = global_sample.replace("Frames: {num_frames}", f"Frames: {rotate.shape[0]}")
    print("帧数写入完毕\n")
    # 写入帧时间
    print("写入帧时间\n")
    global_sample = global_sample.replace("Frame Time: {frame_time}", f"Frame Time: {0.3}")
    print("帧时间写入完毕\n")

    try:
        bv_fileh = open("../simple.bvh", 'w')
        bv_fileh.write(global_sample)
        bv_fileh.close()
        print("BVH文件写入成功")

        # with open("simple.txt", 'w') as f:  # CHK:查看写入的数据
        #     f.write(global_sample)
        #     print("txt文件写入成功")
    except Exception:
        print("BVH文件写入失败")

"""已完成目标一"""

# 标准的bvh文件OFFSET如果被索引基本上都一样，所有的OFFSET都会被同时索引，我们可以事先给OFFSET前添加索引标志，在调用replace方法的时候替换为原样
# 文件内数字索引最好以01，02这样的方式定位索引名字，要不然以1....11会发现第一个和第11个字符会被索引订正两次
# temp_sample=sample.replace(index_string,"OFFSET"+" "+character)该内存变量无法完成增量修改，每修改一次覆盖原有内容
# 改成sample=sample.replace(index_string,"OFFSET"+" "+character) 即可

# 文件格式转化思路：分析两者文件的异同，将二者的数据结构进行对比，找到相同点，将相同点进行替换，将不同点进行添加，最后将替换好的bvh数据流写入文件

"""问题二"""
# 现象: 读取的bvh数据流错误,造成blender加载的动作文件不符合常理
#      根本原因在于骨骼JOINTS名字不匹配--已经逆向找到项目使用的骨骼节点模板
# 分析: 分析演示的动画文件判断加载转换的数据出现了什么问题
# 目的: 找到正确的bvh数据流对应的tensor张量矩阵
# 解决: 1.找寻新的坐标文件
#      2.找到新的旋转值
# 执行：分析算法脚本的输入输出数据流
"""问题三"""
# 现象：模型骨架严重错位
# 分析：TRAM调用的SMPL默认模型的节点数据都是绝对笛卡尔坐标系数据，但是bvh用的是相对与父节点的数据
# 目的：获取对应JOINT对应的相对于父节点的数据
# 解决：1.找到SMPL节点数据矩阵每一行对应的JOINT
#      2.将绝对参考系数据转化为相对参考系数据
# 执行：
"""问题四"""
# 现象：无法直接获取欧拉偏转角数据
# 分析：原有数据格式为3x3矩阵数据，无法直接利用
# 目的：获取可用的欧拉角数据矩阵
# 解决：构造线性变换函数转化欧拉角数据的函数
