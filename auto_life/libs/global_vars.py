import os
import libs.test_utils as test_utils

wait_to_get_selector_opt = {"selector": "", "is_need_refresh": False}

# 操作值为以下key时当前步骤不需要做暂存校验
NOT_CHECK_KEYLIST=("wait_for",)
SAVE_CHECK_PATH = os.path.join(test_utils.get_root_path(), "test_report", "screenshot", "save_check")
