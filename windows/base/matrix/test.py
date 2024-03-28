import os, time
import numpy as np

rgb2xyz_1931=np.mat([[0.49,0.31,0.2],[0.177,0.812,0.011],[0,0.01,0.99]])

def test_rgb_2_xyz(input_rgb,M):
    print("----#测试转换矩阵，请传入[r,g,b],M----")
    print(input_rgb)

    input_rgb=input_rgb.T
    
    out=np.dot(M,input_rgb)
    out=out.T
    #print(out)
    X=out[0,0]
    Y=out[0,1]
    Z=out[0,2]
    x=X/(X+Y+Z)
    y=Y/(X+Y+Z)
    
    print("--->")
    print(X,Y,Z)
    print(x,y)
    print("------")

def rgb_2_xyz(rgb,white):
    # 已知xyz在rg坐标系中的坐标以及W的坐标
    #rgb=np.mat([[1.275,-0.278,0.003],[-1.739,2.767,-0.028],[-0.743,0.141,1.602]])
    #white=np.mat([[0.3333,0.3333,0.3333]])
    print("input:")
    print(rgb,white)
    
    #计算 RGB转XYZ的矩阵
    rgb2xyz=np.linalg.inv(rgb.T)
    #print(rgb2xyz)

    #计算归一化系数，根据等能白光的坐标不变
    whiteM=np.dot(rgb2xyz,white.T)
    k0=0.3333/whiteM[0,0]
    k1=0.3333/whiteM[1,0]
    k2=0.3333/whiteM[2,0]
    k=np.mat([[k0,0,0],[0,k1,0],[0,0,k2]])

    res=k*rgb2xyz
    print("in->out:")
    print(res)
    print("inverse:")
    print(np.linalg.inv(res))
    

def test_math():
    #测试网页中的矩阵结果
    # 已知xyz在rg坐标系中的坐标
    a=np.mat([[1.275,-0.278,0.003],[-1.739,2.767,-0.028],[-0.743,0.141,1.602]])
    m=np.mat([[0.9087,0.09123,0],[0.57492,0.41879,0.00629],[0.37093,0.00548,0.62359]])
    print(m*a)

def fill_rgb(r,g,b):
    r.append(1-r[0]-r[1])
    g.append(1-g[0]-g[1])
    b.append(1-b[0]-b[1])
    
def fill_w(w):
    w.append(1-w[0]-w[1])

def BT709_test(rgb_test):
    m_rgb_hdtv_limit=np.mat([ [0.213,0.715,0.072,0],[-0.117,-0.394,0.511,128],[0.511,-0.464,-0.047,128] ])
    m_yuv_hdtv_limit=np.mat([ [1,0,1.540,-197.12],[1,-0.183,-0.459,82.176],[1,1.816,0,-232.448] ])

    cont_off=np.array([1])
    rgb_test=np.r_[rgb_test,cont_off] #增加常量的数组列
    rgb_test=np.mat(rgb_test) #数组转为矩阵
    rgb_test=rgb_test.T
    yuv_test=m_rgb_hdtv_limit*rgb_test;
    print("-----BT709_test:input rgb->yuv->rgb-----------")
    print(type(rgb_test),rgb_test)
    print("---->yuv:")
    print(type(yuv_test),yuv_test)
    print("----------------")

    yuv_test=yuv_test.A #矩阵转为数组
    print(type(yuv_test),yuv_test)
    cont_off=np.array([[1]])
    yuv_test=np.vstack((yuv_test,cont_off)) #新增常量的行
    yuv_test=np.mat(yuv_test)
    print("---->rgb:")
    rgb_test=m_yuv_hdtv_limit*yuv_test
    print(rgb_test)
    print("-------BT709_test:end---------")

def hdmi_y2r():
    yuv_in=np.mat( [ [161,92,128,1],[135,169,83,1],[109,73,152,1],[112,169,145,1] ] )
    yuv_in=yuv_in.T
    print(yuv_in)

    rgb_ok=np.mat( [ [161,173,97],[72,153,208],[143,111,12],[136,87,185] ] )
    rgb_ok=rgb_ok.T
    print(rgb_ok)

    m_1=np.linalg.inv(yuv_in)
    res=rgb_ok*m_1


    #test_p=np.mat( [161,92,128,1] )
    #test_p=test_p.T
    #print(res * test_p)
    

    print(res)
    hdmi_m=np.mat( [ [1,0,1.4007],[1,-0.332,-0.6965],[1,1.77,0] ] )
    offset=np.mat( [[ -178 ],[132],[-223 ]] )
    hdmi_m_=np.linalg.inv(hdmi_m)

    
    m_yuv_hdtv_limit=np.mat([ [1,0,1.540],[1,-0.183,-0.459],[1,1.816,0] ])
    bt709_offset=np.mat( [ [-197.12],[82.176],[-232.448] ] )
    
    m_csc=hdmi_m_ * m_yuv_hdtv_limit
    offset_csc=hdmi_m_ *(bt709_offset-offset)
    print(m_csc,offset_csc)
    
    test_p=np.mat( [16,128,235] ).T
    print("bt709 right:")
    print(m_yuv_hdtv_limit * test_p + bt709_offset )
    print("268_fix:")
    print(hdmi_m *(m_csc* test_p+offset_csc) + offset)
    

if "__main__" == __name__:

    print("----bt601 ntsc 30hz:----")
    r=[0.63,0.340]
    g=[0.31,0.595]
    b=[0.155,0.070]
    w=[0.3127,0.3290]
    fill_rgb(r,g,b)
    fill_w(w)
    rgb=np.mat([r,g,b])
    rgb_2_xyz(rgb,np.mat([w]))

    
    print("----bt709:----")
    r=[0.64,0.330]
    g=[0.30,0.600]
    b=[0.150,0.060]
    w=[0.3127,0.3290]
    fill_rgb(r,g,b)
    fill_w(w)
    rgb=np.mat([r,g,b])
    rgb_2_xyz(rgb,np.mat([w]))
    
    
    
    
    rgb_test=np.array( [180,223,16]  )
    BT709_test(rgb_test)
    
    hdmi_y2r()


