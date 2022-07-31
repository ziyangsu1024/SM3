# SM3
sm3 encryption algorithm

一、小组成员及github账号名称

郎舒仪     wangwangxiaoxiaosul        
葛菲       ziyangsu1024


二、
项目简介：项目主要内容是SM3相关的加密、攻击以及一些优化方法的简单实现。
项目名称：SM3
完成人： 郎舒仪 201900210030
葛菲 201900460016

三、
完成的项目：SM3的加密，SM3长度扩展攻击，merkle tree简单实现，
pollard-s-rho的实现

未完成的项目：SM2加密，只完成了pollard_rho实现

有问题的项目及问题：


四、对每个项目：
A.具体的项目代码说明
B.运行指导(跑不起来的不算成功)
C.代码运行全过程截图(无截图无说明的代码不给分)
D.每个人的具体贡献说明及贡献排序(复制的代码需要标出引用)

1、SM3加密
（1）具体代码说明
①对所给消息进行填充，首先将比特“1”添加到消息末尾，再根据消息长度l添加k个“0”，其中k是满足l + 1 + k ≡ 448mod512 的最小的非负整数。末尾添加一个64位比特串，该比特串是l的二进制表示。则填充后的消息长度是512比特的整数倍。
②将填充后的消息根据512比特分组并迭代压缩，其中分组由填充后的分组进一步扩展得到。
③压缩函数中所用到的其它布尔函数，置换函数等由国密规定的标准得到。
④最后得到256比特的杂凑值。

（2）运行指导
运行仓库中的enc_sm3.py文件，其中输入为任意十六进制字符串，输出结果为256比特的杂凑值。

（3）结果截图

<img src="https://github.com/ziyangsu1024/SM3/blob/main/1.png" width="800" height="80" />

（4）贡献说明：葛菲

2、SM3长度拓展攻击
（1）具体代码说明：
①生成一个secret，先算出secret的sm3值
②根据sm3值分组后得到最后各个寄存器里的值
③在secret+padding之后附加一段消息，用上一步得到的寄存器里的值作为IV去加密附加的那段消息，得到m1
④再用sm3去加密secret+padding+m'，得到m2
⑤最后判断若m1和m2相等，则攻击成功

（2）运行指导
运行仓库里的sm3lengthattack.py文件，其中会调用store和store1两个库。最后会输出结果是否攻击成功。

(3)结果截图

<img src="https://github.com/ziyangsu1024/SM3/blob/main/2.png" width="600" height="120" />
 
(4)贡献说明：郎舒仪
           
              

3、merkletree实现
（1）具体代码说明：
将待加密的数据传入，然后构造merkle tree：
①对data blocks分别计算哈希值，这里选择了sha256作为加密算法
②每层两两计算获得hash值，用if len（lst）%2==0条件判断此层的block是奇数个还是偶数个。
③直至计算至最上一层，得到proof，最后输出结果和树高。

（2）运行指导：运行仓库中的merkletree.py文件即可，代码中传入了具体的明文，输出结果为最后proof和树高。

（3）结果截图：
 
<img src="https://github.com/ziyangsu1024/SM3/blob/main/3.png" width="800" height="80" /> 

（4）贡献者：郎舒仪

4、pollard-s-rho实现

（1）具体代码说明：
①通过一个函数f(x)=(x^2+a)%n来生成伪随机数,得到一个数列。在 modp下，若有两个数相同，那么这个数列会陷入循环节.
②在随机数列上选一些数与n求最大公约数，如果遇到环则跳出。

（2）运行指导：运行仓库中的pollard-s-rho.py文件，会显示输入一个p，随即输入一个大数，输出一个因子列表。

（3）结果截图：

<img src="https://github.com/ziyangsu1024/SM3/blob/main/4.png" width="600" height="120" />
 
（4）贡献者：葛菲  郎舒仪

