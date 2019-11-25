import pygame
from Games.settings import Settings
from Games.ship import Ship
import Games.game_functions as gf
from pygame.sprite import Group
from Games.games_stats import GameStats
from Games.button import Button

def run_game():

    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建play按钮
    play_button = Button(ai_settings,screen,"play")
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()

    #创建外形人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)


run_game()