from crm_style.create_crm import *
import sys

t_opt=get_opt(sys.argv[1:])
print(t_opt)
g_config=get_golobal_config(t_opt.get("env"))

run(g_config.get('username'),g_config.get('password'),g_config.get('url'),
    g_config.get('institutions'),g_config.get('doctorname'),
    g_config.get('i_username'),g_config.get('i_password'),g_config.get('i_url'),g_config)


#参数来自于crm_style/config_1.ini,自己按需配置
#命令-
'''

普通单膜方案：
python work.py --env=iortho_sit --caseid=C01001475209 --num=3d
python work.py --env=iortho_adv --caseid=C01004991261 --num=3d

普通双膜方案：
python work.py --env=iortho_sit --caseid=C01001485592 --num=3d --dir=0
python work.py --env=iortho_adv --caseid=C01004991373 --num=3d --dir=0

cbct双膜
python work.py --env=iortho_sit --caseid=C01005845765 --num=3d --dir=9
python work.py --env=iortho_adv --caseid=C01004991261 --num=3d --dir=9

cbct单膜
python work.py --env=iortho_sit --caseid=C01005845765 --num=3d --dir=10
python work.py --env=iortho_adv --caseid=C01005845765 --num=3d --dir=10

双膜拔多牙：
python work.py --env=iortho_sit --caseid=C01004643704 --num=3d --dir=1

双膜拔单牙：
python work.py --env=iortho_sit --caseid=C01001454903 --num=3d --dir=2


双膜不拔牙：
python work.py --env=iortho_sit --caseid=C01004163194 --num=3d --dir=5


完整双膜拔牙，符合多重情况：
python work.py --env=iortho_sit --caseid=C01001372216 --num=3d --dir=6

单膜有乳牙
python work.py --env=iortho_sit --caseid=C01001455162 --num=3d --dir=7
python work.py --env=iortho_adv --caseid=C01004991362 --num=3d --dir=7

单膜拔多牙：
python work.py --env=iortho_sit --caseid=C01001456242 --num=3d --dir=3

单膜拔单牙：
python work.py --env=iortho_sit --caseid=C01001430907 --num=3d --dir=4

普通单膜方案带天使扣：
python work.py --env=iortho_sit --caseid=C01001381317 --num=3d




python work.py --env=iortho_adv --caseid=C01001485592 --num=质检不合格

python work.py --env=iortho_sit --caseid=C01001485592 --num=质检不合格

python work.py --env=iortho_sit --caseid=C01001363261 --num=质检合格
python work.py --env=iortho_sit --caseid=C01001398843 --num=不收治

python work.py --env=iortho_sit --caseid=C01001437353 --num=结束阶段

python work.py --env=iortho_sit --patientname=yanzp --num=新建硅胶
python work.py --env=iortho_sit --patientname=yanzp --num=新建口内照



python work.py --env=iortho_sit --caseid=C01001474466 --num=中期硅胶
python work.py --env=iortho_sit --caseid=C01001455083 --num=中期口内照

python work.py --env=iortho_adv --caseid=C01004967523 --num=病例照片不合格




单膜发货：
python work.py --env=iortho_sit --caseid=C01001475209 --num=3d --dir=8
#发货之前需要先3D方案且已经批准，单膜发货建议先运行单膜发货创建3D并批准
python work.py --env=iortho_sit --caseid=C01001404649 --num=发货

#创建一些简单的病例
python work.py --env=iortho_sit --num=冠军A6本阶段
python work.py --env=iortho_sit --num=冠军A6后续阶段
python work.py --env=iortho_sit --num=冠军非A6
python work.py --env=iortho_sit --num=标准
python work.py --env=iortho_sit --num=儿童
python work.py --env=iortho_sit --num=儿童A6
python work.py --env=iortho_sit --num=儿童加冠军
python work.py --env=iortho_sit --num=儿童加冠军A6
python work.py --env=iortho_sit --num=comfos

#创建makeit
创建makeit病例:caseNume是创建的案例格式，waitingtime是两个案例之间的间隔时间
python work.py --env=iortho_sit --num=makeit_3shape --caseNum=2 --Waitingtime=3
python work.py --env=iortho_sit --num=makeit_stl --caseNum=2 --Waitingtime=3


#####循环造3D,秦毛丁用
python work.py --env=iortho_sit --num=3d_2 --dir=3

注意：
如果是iortho_sit环境，可以不传入env参数，默认使用该环境
  即：python work.py --caseid=C12345678901 --num=3d --dir=1
  
如果是创建iortho_sit单膜3D方案，可以不传入dir参数，默认创建单膜
  即：python work.py --env=iortho_sit --caseid=C01001371204 --num=3d
  
创建iortho_sit线下病例，也可以不传入patientname参数，默认使用 线下+5位随机数 作为患者姓名
  即：python work.py --num=新建硅胶

'''


