"""
预览vimo_track_0.npy中的数据结构
"""

import numpy as np
import torch

# vimo_track_0.npy 为以npy方式存储的python字典，这样做读取效率高
"""
    该字典组成如下，每个键的值的类型为Pytorch中的tensor张量类型
    'pred_cam': torch.cat(pred_cam),
    'pred_pose': torch.cat(pred_pose),
    'pred_shape': torch.cat(pred_shape),
    'pred_rotmat': torch.cat(pred_rotmat),
    'pred_trans': torch.cat(pred_trans),
    'frame': torch.cat(frame)
"""


# 函数定义,传入track.npy的文件路径，输出详细txt文件
def detail_preview(file_path):
    # 读取数据，读取的结果为ndarray对象
    data = np.load(file_path, allow_pickle=True)

    #print(data)                         # CHK
    print(type(data))

    # 将ndarray对象转化为字典
    data = data.item()
    print(type(data))
    torch.set_printoptions(threshold=float('inf'))
    with open('preview_detail_data_in_track_npy/pred_cam.txt', 'w') as f:
        f.write(str(data['pred_cam']))
    with open('preview_detail_data_in_track_npy/pred_pose.txt', 'w') as f:
        f.write(str(data['pred_pose']))
    with open('preview_detail_data_in_track_npy/pred_shape.txt', 'w') as f:
        f.write(str(data['pred_shape']))
    with open('preview_detail_data_in_track_npy/pred_rotmat.txt', 'w') as f:
        f.write(str(data['pred_rotmat']))
    with open('preview_detail_data_in_track_npy/pred_trans.txt', 'w') as f:
        f.write(str(data['pred_trans']))
    with open('preview_detail_data_in_track_npy/frame.txt', 'w') as f:
        f.write(str(data['frame']))
    print("Detail OK")

# 函数定义，传入track.npy的文件路径，输出概要txt文件
def overview(file_path):
    data = np.load(file_path, allow_pickle=True)
    data = data.item()
    with open('previe_overviewdata_in_track_npy.txt', 'w') as f:
        f.write(str(data))
    print("Preview Ok")



# 预览脚本
if __name__ == '__main__':
    file_path = r'vimo_track_0.npy'
    overview(file_path)
    detail_preview(file_path)
