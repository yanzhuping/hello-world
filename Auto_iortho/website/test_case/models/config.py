#配置文件
#=======================================================================================================================

#sit环境参数

username="yanzp0857"  #iortho账号

password="123456"   #iortho密码

url="https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas"  #iortho登录地址

crm_username = "shihm"  #crm账号

crm_password = "123456"   #crm密码

crmurl = "http://crm-web.sh-sit.eainc.com/crm/index.php?module=Home&action=index"   #crm登录地址

#=======================================================================================================================
#adv环境参数
adv_username="cesys13784"  #iortho账号

adv_password="123456"   #iortho密码

adv_url="https://iorthoadv.angelalign.com/cas/login?service=https://iorthoadv.angelalign.com/OPM/shiro-cas"  #iortho登录地址

adv_crm_username = "xuw"  #crm账号

adv_crm_password = "123456"   #crm密码

adv_crmurl = "https://cas.adv.eainc.com:8443/cas/login?service=http%3A%2F%2Fcrm-web.adv.eainc.com%2Fcrm%2Findex.php%3Fmodule%3Dea_case%26action%3DDetailView%26record%3D2246d0e3-3e00-f447-1128-5b3b051f6249"   #crm登录地址


#共有参数===================================================================================================================
product_num = 2  #产品类型，1是冠军版，2是标准版，3是儿童版，4是儿童+冠军

hospital = 1 #这是医疗机构，数字代表在列表中所处的位置，如无特殊要求，建议选择1，因为每个账号的医疗机构数量不一致但至少有1

#数据库参数==================================================================================================
host='192.168.37.113'

mysqluser='opm_sh_sit'

mysqlpasswd='opm_sh_sit'

dbName='test'     #数据库名

tableName='auto_names'

#测试报告发送模块参数======================================================================================
e_server='smtp.126.com'   #邮件发送协议，测试邮箱是网易126邮箱

e_user='helloyange@126.com'

e_password='test123'    #客户端授权码

e_sender='helloyange@126.com'

e_receives=['1405394548@qq.com']  #接收者，可以传入多个

