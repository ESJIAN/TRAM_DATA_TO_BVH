# TRAM_DATA_TO_BVH
**程序主要实现转换Tram算法中产生的坐标点数据以及旋转数据，并且写了一些子程序去预览转换过程中产生的数据**





- Program中放着用到的程序
- Research_Relative中放着研究转换的资料
- Sourcefile放着vimo_track_0.npy还有一些产生的数据结构预览数据

## Step1：骨架数据转化

---
- [x] 通过散点图逆向出了smplx默认骨架数据矩阵每行与人体骨架的对应关系
- [x] 通过逆向手段逆向出bvh骨架每行JOINT与人体骨架的对应关系
- [x] 通过逆向手段逆向出了bvh骨架的层级关系
- [x] 制定出smplx绝对参考节点向bvh相对参考节点的转化逻辑   
- [x] 完成了smplx骨架数据到bvh骨架数据的转换
## Step2：运动数据转化
---
- [x] 通过blender的帮助逆向出了bvh文件中20组运动数据的含义,顺规类型,所用角度单位
- [ ] 定位原文中能够转化的20组旋转矩阵
> - 猜想：
>> - 猜想1：旋转矩阵来源于vimo_track_0.npy中的pred_rotmat (错误)
>> - 猜想2：旋转数据来源于步骤四产生的pose.pth (正确,为24x3的欧拉偏转阵)
>> - 猜想3：旋转数据来源于步骤四构造smpl时候产生的body_pose数据 (正确，为24x3x3的偏转矩阵)
> - 验证：
>> - 验证猜想3：
>>> - 分析1：猜想3的数据是一个23x3的矩阵|不知道每一矩阵的数据用途-->无法筛选出正确的19个用于描述旋转的矩阵
>>> - 尝试：找寻文献研究SMPL的骨架驱动
>>>> - 发现1：SMPL描述旋转用了1+23个点，如果不算根节点的旋转，那就是23个点，而bvh旋转数据一共1+19组，其中第一组是根节点的绝对偏转，其他才是描述点的相对偏转
>>>> - 子猜想：猜测SMPL的旋转矩阵组的出现次序与其骨架节点出现的次序是互相匹配的，也就是说第一个旋转矩阵组描对应描述第一个骨架节点坐标其他类比推理
>>>> - 子分析：先画出旋转矩阵与控制所控制的对应节点对应关系图，然后根据bvh实际中偏转的19个点来选择需要使用哪些组的旋转矩阵
>>>> - 发现2: pose.pth文件就是欧拉偏转角矩阵文件，把发现一的猜想和分析转移到发现2进行
>>>> - 子分析：pose旋转数据根需要保留-24行(该行描述根节点对绝对参考点的旋转情况)，不需要-22，-23-21行，不需要-10，-11，-12行
>>> - 分析2：无法得出猜想3的旋转矩阵的顺规类型-->不能构造旋转矩阵转化表达式-->无法求解XZY顺规的欧拉偏转阵
>>> - 分析3：重新明确目的——找到pose旋转数据转化为bvh旋转数据的方法
>>>  
>>>> 2.构造pose24条旋转数据到bvh20条旋转数据的映射关系——
>>>> 
>>>>      2.0研究SMPL的pose数据每一行含义(
>>>>      2.1每一行控制哪个节点旋转？
>>>>      2.2去掉哪六行？
>>>>      2.3怎么重排行顺序？
>>>>      2.4怎么重排列顺序？


---
## Step3：后续改进
- [ ] 代码模块化
- [ ] 转化为C++代码进行性能优化
# 任务总结
## 学习到的知识
- 模块化代码管理
- 代码批注的使用
  - 版本批注
  - 犯错批注
  - 变量检查批注
  - 函数描述批注(输入、输出、功能)
# 本项目逆向学习路线
- 熟悉BVH文件骨架数据，从上到下每一行对应实际骨架图的哪个节点
- 熟悉BVH动作数据，一共20x3组
   - 熟悉每一组数据的含义，表示位移还是旋转
   - 熟悉BVH动作数据使用的顺规和度量单位
- 熟悉TRAM数据流
- 熟悉SMPLX
  - 熟悉SMPLX骨架数据，从上到下每一组骨架数据对应实际骨架的哪个节点
  - 熟悉SMPLX旋转数据，从上到下每一组旋转数据控制的是实际骨架的哪个节点
