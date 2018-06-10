'''
Created on 2018年5月31日
# 碰到这种类型的题目，我们不妨先来找找规律。通过上面的例子我们可以发现，设树的高度为h，则输出的数组的宽度总为2^h-1；
并且每棵子树的根节点的下标总为其
左右子树的下标的中点。 
# 发现了这两点，思路自然就清晰起来了。首先通过比较左右子树高度
的方法来得到整棵二叉树的高度，进而得到宽度；然后将要输出的数组进行初始化。接着采用先序遍历的方式或者说是DFS，先遍历子树的根节点，
将根节点的值写入数组中，再分别遍历其左右子树，周而复始，这样问题就顺利解决了~

@author: Administrator
'''
class Solution(object):
    def print(self,root):
        import math
        def dfs(root,h):
            if root:
                return max(defs(root.left,h+1),dfs(root.right,h+1))
            else:
                return h
            
        height = dfs(root,0);
        width = 2**height-1;
        #初始化
        res = [["" for j in range(width)] for i in range(height)]
        def dfs_print(res,root,h,pos):
            if root:
                res[h-1][pos]='%d'%root.val
                dfs_print(res,root.left,h+1,pos-2**(height-h-1))
                dfs_print(res,root.right,h+1,pos+2**(height-h-1))
        dfs_print(res,root,1,width/2)
        return res
