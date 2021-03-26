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
    'appPackage' : 'com.dianping.v1',
   #  5被测app的入口信息，通过上方命令获取
   'appActivity':'NovaMainActivity',
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
# 温馨提示--同意并继续
driver .find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()

# 休息5秒
# time.sleep(5)

# 大众点评权限管理--确定
driver .find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]").click()
# time.sleep(2)
# 点击进入美食
driver . find_element_by_xpath("//android.widget.RelativeLayout[@content-desc='美食']/android.widget.ImageView").click()
print("进入美食页面")
# 选择第一家进入详情页
driver .find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.LinearLayout/android.widget.RelativeLayout").click()
# 点击评价
driver .find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.TextView").click()
print("点击评价")
#滑动屏幕
start_x=500
start_y=1500
end_x=700
# 上下滑动x不变
time.sleep(2)
driver .swipe(start_x,start_y,start_x,end_x)
# 选择一家评论进入详情页
driver .find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout").click()
print("进入评论详情页")


#滑动屏幕
start_x=500
start_y=1500
end_x=700
# 上下滑动x不变
time.sleep(2)
driver .swipe(start_x,start_y,start_x,end_x)

print("查看评论加载完毕")


