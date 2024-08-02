"""
运行环境:
torch版本为2.4.0
python版本为3.10
numpy版本<=2.x
"""
import torch

rotate=torch.load("j3d.pth", weights_only=True)
pose=torch.load("pose.pth", weights_only=True)


bvh_header = """
    HIERARCHY
    ROOT Hips
    {
        01OFFSET 0.0 0.0 0.0
        CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation
        JOINT Chest
        {
            02OFFSET 0.0 0.0 0.0
            CHANNELS 3 Zrotation Xrotation Yrotation
           JOINT Neck
            {
                03OFFSET 0.0 0.0 0.0
                CHANNELS 3 Zrotation Xrotation Yrotation
                JOINT Head
                {
                    04OFFSET 0.0 0.0 0.0
                    CHANNELS 3 Zrotation Xrotation Yrotation
                    End Site 
                    {
                        05OFFSET 0.0 0.0 0.0
                    }
                }
                JOINT LeftCollar
                {
                    06OFFSET 0.0 0.0 0.0
                    CHANNELS 3 Zrotation Xrotation Yrotation
                    JOINT LeftUpArm
                    {
                        07OFFSET 0.0 0.0 0.0
                        CHANNELS 3 Zrotation Xrotation Yrotation
                        JOINT LeftLowArm
                        {
                            08OFFSET 0.0 0.0 0.0
                            CHANNELS 3 Zrotation Xrotation Yrotation
                            JOINT LeftHand
                            {
                                09OFFSET 0.0 0.0 0.0
                                CHANNELS 3 Zrotation Xrotation Yrotation
                                End Site
                                {
                                    10OFFSET 0.0 0.0 0.0
                                }
                            }
                        }
                    }
                }
                JOINT RightCollar
                {
                    11OFFSET 0.0 0.0 0.0
                    CHANNELS 3 Zrotation Xrotation Yrotation
                    JOINT RightUpArm
                    {
                        12OFFSET 0.0 0.0 0.0
                        CHANNELS 3 Zrotation Xrotation Yrotation
                        JOINT RightLowArm
                        {
                            13OFFSET 0.0 0.0 0.0
                            CHANNELS 3 Zrotation Xrotation Yrotation
                            JOINT RightHand
                            {
                                14OFFSET 0.0 0.0 0.0
                                CHANNELS 3 Zrotation Xrotation Yrotation
                                End Site
                                {
                                    15OFFSET 0.0 0.0 0.0
                                }
                            }
                        }
                    }
                }
            }
        }
        JOINT LeftUpLeg
        {
            16OFFSET 0.0 0.0 0.0
            CHANNELS 3 Zrotation Xrotation Yrotation
            JOINT LeftLowLeg
            {
                17OFFSET 0.0 0.0 0.0
                CHANNELS 3 Zrotation Xrotation Yrotation
                JOINT LeftFoot
                {
                    18OFFSET 0.0 0.0 0.0
                    CHANNELS 3 Zrotation Xrotation Yrotation
                    End Site
                    {
                        19OFFSET 0.0 0.0 0.0
                    }
                }
            }
        }
        JOINT RightUpLeg
        {
            20OFFSET 0.0 0.0 0.0
            CHANNELS 3 Zrotation Xrotation Yrotation
            JOINT RightLowLeg
            {
                21OFFSET 0.0 0.0 0.0
                CHANNELS 3 Zrotation Xrotation Yrotation
                JOINT RightFoot
                {
                    22OFFSET 0.0 0.0 0.0
                    CHANNELS 3 Zrotation Xrotation Yrotation
                    End Site
                    {
                        23OFFSET 0.0 0.0 0.0
                    }
                }
            }
        }
    }
    MOTION
    Frames: {num_frames}
    Frame Time: {frame_time}
    
    """


def write_pose(pose, sample):

    for i in range(0, pose.shape[1]):
        temp_pose=pose[0,i,0:1:1,]         # 获取到了一个二维的tensor变量
        list_temp_pose=temp_pose.tolist()  # 转换成为了一个二维列表
        character=""
        for j in range(0,3):
            character=character+str(list_temp_pose[0][j])+' '
        if i>10 or i==10:
            index_string = str(i + 1)+"OFFSET 0.0 0.0 0.0"
        else:
            index_string = "0"+str(i + 1)+"OFFSET 0.0 0.0 0.0"

        sample=sample.replace(index_string,"OFFSET"+" "+character)   # 修改完起始位姿数据
    return sample


def write_rotate(rotate, sample):
    character = " "
    for i in range(0, rotate.shape[0]): # 遍历纵向旋转数据
        for j in range(0, rotate.shape[1]):# 遍历行旋转数据
            for k in range(0, rotate.shape[2]): # 遍历列旋转数据
                list_temp_rotate=rotate[i, j, k].tolist()
                character = character + str(list_temp_rotate) + ' '
        character = character + '\n'
        character = character + ' '
    return character




global global_sample


if __name__ == "__main__":
    # 示例调用函数将数据写入 BVH 文件

    # 获取了起始位姿数据
    global_sample = write_pose(pose, bvh_header)
    # 获取了帧数
    global_sample = global_sample.replace("Frames: {num_frames}", f"Frames: {rotate.shape[0]}")
    # 获取了旋转数据
    global_sample = global_sample+write_rotate(rotate, global_sample)

    txt=open("simple.bvh", 'w')
    txt.write(global_sample)
    txt.close()




# 标准的bvh文件OFFSET如果被索引基本上都一样，所有的OFFSET都会被同时索引，我们可以事先给OFFSET前添加索引标志，在调用replace方法的时候替换为原样
# 文件内数字索引最好以01，02这样的方式定位索引名字，要不然以1....11会发现第一个和第11个字符会被索引订正两次
# temp_sample=sample.replace(index_string,"OFFSET"+" "+character)该内存变量无法完成增量修改，每修改一次覆盖原有内容
# 改成sample=sample.replace(index_string,"OFFSET"+" "+character) 即可
