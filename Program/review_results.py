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
# 函数定义
def preview(data):
    #print(data)
    print(type(data))
    data = data.item()
    print(type(data))
    torch.set_printoptions(threshold=float('inf'))
    with open('../Sourcefile/DetaiData_in_npy/pred_cam.txt', 'w') as f:
        f.write(str(data['pred_cam']))
    with open('../Sourcefile/DetaiData_in_npy/pred_pose.txt', 'w') as f:
        f.write(str(data['pred_pose']))
    with open('../Sourcefile/DetaiData_in_npy/pred_shape.txt', 'w') as f:
        f.write(str(data['pred_shape']))
    with open('../Sourcefile/DetaiData_in_npy/pred_rotmat.txt', 'w') as f:
        f.write(str(data['pred_rotmat']))
    with open('../Sourcefile/DetaiData_in_npy/pred_trans.txt', 'w') as f:
        f.write(str(data['pred_trans']))
    with open('../Sourcefile/DetaiData_in_npy/frame.txt', 'w') as f:
        f.write(str(data['frame']))
    print("OK")




# 脚本主入口
if __name__ == '__main__':
    file_path = f'../Sourcefile/vimo_track_0.npy'
    data = np.load(file_path, allow_pickle=True)
    preview(data)