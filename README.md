# TRAM_DATA_TO_BVH
转换Tram算法中产生的坐标点数据以及旋转数据

- Program中放着用到的程序
- Research_Relative中放着研究转换的资料
- Sourcefile放着vimo_track_0.npy还有一些产生的数据结构预览数据

## 骨架数据转化

---
- [x] 通过散点图逆向出了smplx默认骨架数据矩阵每行与人体骨架的对应关系
- [x] 通过逆向手段逆向出bvh骨架每行JOINT与人体骨架的对应关系
- [x] 通过逆向手段逆向出了bvh骨架的层级关系
- [x] 制定出smplx绝对参考节点向bvh相对参考节点的转化逻辑   
- [x] 完成了smplx骨架数据到bvh骨架数据的转换
## 运动数据转化
---
- [x] 通过blender的帮助逆向出了bvh文件中20组运动数据的含义,顺规类型,所用角度单位
- [ ] 定位原文中能够转化的20组旋转矩阵
- [ ] 明确该旋转矩阵的顺规类型
- [ ] 
- [ ] 把程序模块化

---
## 后续改进
- [] 代码模块化
- [] 转化为C++代码进行性能优化
