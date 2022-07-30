import hashlib

def hash_data(data, hash_function = 'sha256'): #使用sha256进行加密
    "hash function"
    hash_function = getattr(hashlib, hash_function)
    data = data.encode('utf-8')
    return hash_function(data).hexdigest()

def concat_and_hash_list(lst, hash_function = 'sha256'):
    lst1 = []                   #将最后的输出存在lst1中
    for i in lst:
        lst1.append(hash_data(i))
    # print(lst1)

    assert len(lst1)>2     #直到最后只剩下一个的时候停止
    n = 0                  #merkle树高度
    while len(lst1) >1:
        n += 1
        if len(lst1)%2 == 0:     #当此层的叶子节点为偶数个时，两两进行哈希，求出进一层的值
            v = []
            while len(lst1) >1 :
                a = lst1.pop(0)
                b = lst1.pop(0)
                v.append(hash_data(a+b, hash_function))
            lst1 = v
        else:           #当此层为奇数个时
            v = []
            l = lst1.pop(-1)
            while len(lst1) >1 :
                a = lst1.pop(0)
                b = lst1.pop(0)
                v.append(hash_data(a+b, hash_function))
            v.append(l)
            lst1 = v
    return lst1, n+1     #输出结果和树高


l = ['a', 'b', 'c',"d"]
print(concat_and_hash_list(l))
