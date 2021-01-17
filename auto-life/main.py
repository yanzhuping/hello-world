# -*- coding:UTF-8 -*-
import sys
from libs.keywords_trans import *
from driver.driver import *
import traceback


class MainHandler:
    def __init__(self):
        # 读取命令行参数
        self.t_opt = get_opt(sys.argv[1:])
        # 根据参数读取配置
        self.g_config = get_golobal_config(self.t_opt.get("env"))
        self.driver = browser()
        # 存储用例
        self.case_store = {}
        # 存储用例执行过程的变量
        self.case_variable = {}
        # 用例执行结果
        self.case_result = {'total': set(), 'failed': set(), "failed_info": []}
        # 存储元素选择器json
        self.ele_selector_store = {}

    def do_execute(self):

        if self.t_opt.get('func') == "create3d":
            create3d_auto_handler(self)
        elif self.t_opt.get('func') == "endphase":
            finish_phase_auto_handler(self)
        else:
            p = Pinyin()
            # 读取所有的用例
            file_list = list_dir(get_execute_dir(
                self.t_opt.get("test_case")))   # 将指定路径下的所有文件路径存储于列表中
            # 命令行读取到的level
            opt_level = str(self.t_opt.get("level", '-1')
                            )     # 如果level字段为空，则默认给一个-1
            for file_path in file_list:
                # 读取excel中的用例
                case_list = read_excel(file_path)
                # print(case_list)
                # index从0开始，case是读取的excel每一行的数据，类型是字典
                for index, case in enumerate(case_list):
                    case_id = case.get("id")
                    keywords = case.get("keywords")
                    # 根据key从json文件获取选择器
                    get_selector_val(self, case)
                    # 用例中的level项
                    case_level = format_digit_str(case.get("level"))
                    # 关键词存在并且用例的level和命令行指定的level一致（命令行没有指定level除外）
                    if keywords is not None and keywords != "" and (opt_level == '-1' or opt_level == case_level):
                        try:
                            if self.case_store.get(case.get('id')) is None:
                                self.case_store[case.get('id')] = []
                            if case_id is not None and case_id != "":
                                self.case_result.get("total").add(case_id)
                            # 根据keywords触发相应的函数
                            globals().get(case.get("keywords")+"_handler")(self, case)
                            try:
                                insert_img(self.driver, case.get("id"),
                                       "{}_{}.png".format(index, p.get_pinyin(case.get("desc"), "")))
                            except:
                                pass
                            # 保存相应的用例后面校验用  根据用例Id动态生成变量
                            self.case_store[case.get('id')].append(case)
                        except:
                            try:
                                insert_img(self.driver, case.get("id"), "{}_{}.png".format(index, p.get_pinyin(case.get("desc"),"")))
                            except:
                                pass
                            failed_desc = "用例Id：{id},步骤描述：{desc}，关键字：{keywords}，选择器：{selector},操作值：{val}".format(
                                **case)  # **case通过字典设置参数
                            traceback_info = traceback.format_exc()
                            print(failed_desc)
                            print(traceback_info)
                            self.case_result.get("failed").add(case_id)
                            # self.case_result.get("failed_info").append(
                            #     {
                            #         "failed_desc": failed_desc,
                            #         "traceback": traceback_info
                            #     }
                            # )
                            case["traceback"] = traceback_info
                            self.case_store[case.get('id')].append(case)
            handle_case_result(self.case_result,self.case_store)

        print("---------------全部执行结束--------------------------------")
        self.driver.quit()




if __name__ == "__main__":
    main_handler = MainHandler()
    main_handler.do_execute()


# python main.py --env=iortho_sit --test_case=execute/champion-mid-C.xlsx  --level=-1
# 自动创建3d
# python main.py --env=iortho_sit --func=create3d --casecode=C01001287053 --phase=1 --type=1 --update
# phase 1:新病例 2:中期
# type 1:A7 2:A8 3:邻面去油
# 结束当前阶段
# python main.py --env=iortho_sit --func=endphase --casecode=C01001264003

#海外版
#python main.py --env=iortho_sit_web --test_case=execute/metaphase/foreign_account_authority.xls
#销售和职能
#python main.py --env=iortho_sit_sale --test_case=execute/metaphase/sale_account_authority.xls --level=1
#助理
#python main.py --env=iortho_sit_assistant --test_case=execute/metaphase/assistant_account_authority.xls
#高级助理
#python main.py --env=iortho_sit_high_assistant --test_case=execute/metaphase/high_assistant_account_authority.xls
#医生
#python main.py --env=iortho_sit --test_case=execute/metaphase/doctor_account_authority.xls