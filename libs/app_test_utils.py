from time import sleep



#向上滑动
def swipeUp(driver, n=1):
    # 获取屏幕的size
    size = driver.get_window_size()
    # 获取屏幕宽度 width
    width = size['width']
    # 获取屏幕高度 height
    height = size['height']
    x1 = width * 0.5
    y1 = height * 0.7
    y2 = height * 0.5
    sleep(1)
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,200)
        sleep(5)
    return x1,y1

#向下滑动
def swipeDown(driver, n=1):
    # 获取屏幕的size
    size = driver.get_window_size()
    # 获取屏幕宽度 width
    width = size['width']
    # 获取屏幕高度 height
    height = size['height']
    x1 = width * 0.5
    y1 = height * 0.25
    y2 = height * 0.9
    sleep(1)
    for i in range(n):
        sleep(1)
        driver.swipe(x1, y1, x1, y2,200)
