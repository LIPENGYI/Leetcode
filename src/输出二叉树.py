'''
Created on 2018��5��31��
# �����������͵���Ŀ�����ǲ����������ҹ��ɡ�ͨ��������������ǿ��Է��֣������ĸ߶�Ϊh�������������Ŀ����Ϊ2^h-1��
����ÿ�������ĸ��ڵ���±���Ϊ��
�����������±���е㡣 
# �����������㣬˼·��Ȼ�����������ˡ�����ͨ���Ƚ����������߶�
�ķ������õ����ö������ĸ߶ȣ������õ���ȣ�Ȼ��Ҫ�����������г�ʼ�������Ų�����������ķ�ʽ����˵��DFS���ȱ��������ĸ��ڵ㣬
�����ڵ��ֵд�������У��ٷֱ�����������������ܶ���ʼ�����������˳�������~

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
        #��ʼ��
        res = [["" for j in range(width)] for i in range(height)]
        def dfs_print(res,root,h,pos):
            if root:
                res[h-1][pos]='%d'%root.val
                dfs_print(res,root.left,h+1,pos-2**(height-h-1))
                dfs_print(res,root.right,h+1,pos+2**(height-h-1))
        dfs_print(res,root,1,width/2)
        return res
