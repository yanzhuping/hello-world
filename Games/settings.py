class Settings():
    '''存储游戏所有设置类'''
    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #飞船速度设置
        self.ship_speed_factor = 1.5