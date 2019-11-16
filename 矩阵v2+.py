def sgn(a):
    if a>=0:
        return 1
    else:
        return -1
def r(a,b):
    if isinstance(a,int) and isinstance(b,int):
        c=a+b
    else:
        a0=len(str(a))-len(str(int(a)))-1
        b0=len(str(b))-len(str(int(b)))-1
        if a0>b0:
            b0=a0
        a1,b1=int(10**b0*a),int(10**b0*b)
        c=(a1+b1)/10**b0
    return c
def f(a):
    if a<0:
        return -a
    else:
        return a
def k(x,a):
    b=(' 0'*len(a)).split()
    for i in range(len(a)):
        if a[i]!=0:
            b[i]=x*a[i]
        else:
            b[i]=0
    return b
def F(q,w,p,a):
    z0,z=0,{}
    for i in range(q,w+1):
        if a[i][p]!=0:
            z[z0]=i
            z0+=1
        if z0==2:
            break
    else:
        b=a
        return b
    a0,b0,g,i=f(a[z[0]][p]),f(a[z[1]][p]),{},0
    if a0<b0:
        a0,b0,z0=b0,a0,-1
    if a0%b0==0:
        if z0==-1:
            a[z[0]],a[z[1]]=a[z[1]],a[z[0]]
        b=F(z[1],w,p,a)
        return b
    while b0>0:
        a0,b0,g[i],i=b0,a0%b0,a0//b0,i+1
    y0,y1,z1,z2=0,1,1,-g[0]
    for u in range(1,i):
        y0,y1,z1,z2=z1,z2,y0-g[u]*z1,y1-g[u]*z2
    if z0!=-1:
        d,e=y0,y1
    else:
        d,e=y1,y0
    for u in range(len(a[z[0]])):
        a[z[1]][u]=k(d*sgn(a[z[0]][p]),a[z[0]])[u]+k(e*sgn(a[z[1]][p]),a[z[1]])[u]
    b=F(z[1],w,p,a)
    return b
print('这是一个化简整数元素矩阵的程序。\n输入行数和列数时请输正整数，不然会报错。')
a=eval(input('矩阵行数:'))
b=eval(input('矩阵列数:'))
c,z={},0
print('输入每一行的{}个数时数中间用空格隔开。（按要求走哦，不然也会报错。。）'.format(b))
for i in range(a):
    c[i]=input('第{}行： '.format(i+1)).split()
    for j in range(b):
        c[i][j]=eval(c[i][j])
for i in range(a):
    o=1
    while o==1:
        d,o,h=0,0,i+z
        if h==b:
            h=-1
            break
        while c[i+d][h]==0:
            d+=1
            if i+d==a:
                o=1
                break
        else:
            c=F(i,a-1,h,c)
            for u in range(a-i-1):
                if c[a-1-u][h]!=0:
                    c[i],c[a-1-u]=c[a-1-u],c[i]
                    break
        if o==1:
            z+=1
    if h==-1:
        break
    for j in list(range(i))+list(range(i+1,a)):
        s=f(c[j][h])//f(c[i][h])
        if s>0:
            if c[j][h]*c[i][h]<0:
                s=-s
            for u in range(h,b):
                c[j][u]-=s*c[i][u]
print('其对应的一个阶梯型矩阵为：')
for i in range(a):
    for j in range(b):
        print('{:^7}'.format(c[i][j]),end='|')
    print()
n=0
while n<a:
    for i in range(n,a):
        for u in range(b):
            if c[a-1-i][u]!=0:
                x,y,u,n=a-1-i,u,-1,i+1
                break
        if u==-1:
            break
    else:
        n=-1
        break
    d={}
    for i in range(x):
        c[i][y],d[i]=0,c[i][y]
        for u in range(y+1,b):
            c[i][u]=r(c[i][u],-d[i]*c[x][u]/c[x][y])
if n!=-1:
    for i in range(a):
        for u in range(b):
            if c[i][u]!=0:
                if c[i][u]==1:
                    break
                else:
                    c[i]=k(1/c[i][u],c[i])
                    break
print('其对应的最简行阶梯矩阵近似为:')
for i in range(a):
    for j in range(b):
        print('{:^7.3f}'.format(c[i][j]),end='|')
    print()
