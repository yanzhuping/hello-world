# 导入时间包
import time
# 导入appium包
from appium import webdriver
from time import sleep
#告诉appium自动化相关的配置项
pzx_caps={
    # app配置必须要写的5个配置项
    # 1被测试app所处平台-安卓
    'platformName':'Android',
   # 2操作系统版本-安卓10，# 手机版本号Honor V10b
    'platformVersion':'10',
   #3设备名称可以随便写，但是要有：测试音乐
   'deviceName':'Honor V10b',
   #  获取app被测试系统的应用在命令提示符内输入appPackge+appActivity命令：adb shell dumpsys activity recents | findstr intent回车
   # 4appPackge包名app上的报名信息，通过上方命令获取
  # 'appPackge':'com.netease.cloudmusic',
    'appPackage' : 'com.netease.cloudmusic',
   #  5被测app的入口信息，通过上方命令获取
   'appActivity':'activity.LoadingActivity',
# 'appActivity':'io.dcloud.PandoraEntry',
    #  如下是防止app重置或者超时的设置
   # 禁止app自动化后重置
   'noRest':True,
   #  设置命令超时时间-3600秒一小时
   'newCommandTimeout':3600,
    # 指定驱动-UI2
    'automationName':'UiAutomator2'
}
# 启动被测系统app
driver = webdriver.Remote('http://localhost:4723/wd/hub',pzx_caps)
# 加入隐士等待时间(10)秒
driver.implicitly_wait(10)



print("已经启动app")
#进入app点击服务条款提示--同意，如果出现就点击不出现就不点
try:
    driver.find_element_by_id("com.netease.cloudmusic:id/agree").click()
except Exception as e:
    print("com.netease.cloudmusic:id/agree: \n")
    print(e);
    pass
# 云音乐权限申请,如果出现就点击不出现就不点
# driver.find_element_by_id("permissionGrant").click()
try:
    driver.find_element_by_id("com.netease.cloudmusic:id/permissionGrant").click()
except Exception as e:
    print("com.netease.cloudmusic:id/permissionGrant: \n")
    print(e);
    pass
# 是否允许访问照片文件--始终允许,如果出现就点击不出现就不点
try:
    driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
except Exception as e:
    print("com.android.permissioncontroller:id/permission_allow_button: \n")
    print(e);
    pass
# 点击同意用户协议
try:
    driver.find_element_by_id("com.netease.cloudmusic:id/agreeCheckbox").click()
except Exception as e:
    print("com.netease.cloudmusic:id/agreeCheckbox: \n")
    print(e);
    pass
#立即体验
try:
    driver.find_element_by_id("com.netease.cloudmusic:id/trial").click()
except Exception as e:
    print("com.netease.cloudmusic:id/trial: \n")
    print(e);
    pass

# 是否收听页面点击空白处代表不收听，
# 点击坐标可以参照我写的 tap方法，就是这个tap传的参数类型有点特殊，前面2个是坐标，后面500是500毫秒无所谓是点击持续时间。
time.sleep(5)
driver.tap([(600, 350)],500)


print("进入听音乐列表")



# 进入发现

# 点击每日推荐

# 获取前三首歌曲

