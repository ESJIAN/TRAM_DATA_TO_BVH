"""
写入24个位姿到内存变量bvh_header中
"""


def write_pose(pose, sample):
    # print(f"{pose.shape[1]}")                      # CHK:shape[0]帧数 shape[1]关节数+1 shape[2]  shape[3]
    for i in range(0, 24):                           # 基于0的索引方法，索引最大值会比索引个数少一个
        temp_pose = pose[i]                          # 第0帧，第i行的三个数据，留空表示该维度全选
        list_temp_pose = temp_pose                   # 转换成为了一个二维列表
        #    print(f"{i+1}行"+str(list_temp_pose))    # CHK:查看各个关节的笛卡尔坐标系值
        character = ""

        """ 切片位姿列表中的一行三个笛卡尔坐标值 """
        for j in range(0, 3):
            character = character + str(list_temp_pose[j]) + ' '

        """ 构造条件表达式时明确条件变量与和他相联系的表示第几个变量的关系，然后通过锁定后者反推前者的分界条件 """
        if i > 8:
            index_string = str(i + 1) + "OFFSET 0.0 0.0 0.0"               # i=9~23时，索引字符表达式为 "数字OFFSET 0.0 0.0 0.0"
        else:
            index_string = "0" + str(i + 1) + "OFFSET 0.0 0.0 0.0"         # i=0~8时，索引字符表达式为 "0数字OFFSET 0.0 0.0 0.0"

        sample = sample.replace(index_string, "OFFSET" + " " + character)  # 修改完起始位姿数据
    return sample
