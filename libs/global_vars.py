import os
import libs.test_utils as test_utils

wait_to_get_selector_opt = {"selector": "", "is_need_refresh": False}

# 操作值为以下key时当前步骤不需要做暂存校验
NOT_CHECK_KEYLIST = ("wait_for", "assert", "switch_to")

APP_NOT_CHECK_KEYSLIST = ("app_sleep", 'get_webview', 'switch_to_cur_win',
                          '间隙的矫治', '邻面去釉', '预留个别间隙', '3shape')

SAVE_CHECK_PATH = os.path.join(test_utils.get_root_path(), "test_report",
                               "screenshot", "save_check")
APP_SAVE_CHECK_PATH = os.path.join(test_utils.get_root_path(), "test_report",
                                   "screenshot", "app_save_check")
uploadPhotoList = []
