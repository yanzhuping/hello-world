import sys
from appium import webdriver

from libs.app_keywords_trans import *
from libs.test_utils import desired_caps_android
import traceback


class MainHandler:
    def __init__(self):
        # 读取命令行参数
        self.t_opt = get_opt(sys.argv[1:])
        # 根据参数读取配置
        self.g_config = get_golobal_config(self.t_opt.get("env"))
        # 存储用例
        self.case_store = {}
        # 存储用例执行过程的变量
        self.case_variable = {}
        # 用例执行结果
        self.case_result = {'total': set(), 'failed': set(), "failed_info": []}
        self.ele_selector_store = {}
        # app配置必须要写的5个配置项


        # # 禁止app自动化后重置
        # 'noRest';True,
        #
        # # 设置命令超时延长时间-单位秒
        # 'newcommandTimeout';3600,

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps_android)

        # self.driver.implicitly_wait(10)
        # # from selenium import webdriver
        # opt = webdriver.ChromeOptions()
        # opt.add_experimental_option('w3c', False)
        # driver = webdriver.Chrome(chrome_options=opt)

    def do_execute(self):
        file_list = list_dir(get_execute_dir(
            self.t_opt.get("test_case")))  # 将指定路径下的所有文件路径存储于列表中

        # 命令行读取到的level
        opt_level = int(self.t_opt.get("level", -1))  # 如果level字段为空，则默认给一个-1
        for file_path in file_list:
            # 读取excel中的用例
            case_list = read_excel(file_path)
            # print(case_list)
            for index, case in enumerate(
                    case_list):  # index从0开始，case是读取的excel每一行的数据，类型是字典
                # print(case)
                case_id = case.get("id")
                keywords = case.get("keywords")
                # 根据key从json文件获取选择器
                get_selector_val(self, case)
                # 用例中的level项
                case_level = case.get("level")
                # 关键词存在并且用例的level和命令行指定的level一致（命令行没有指定level除外）
                if keywords is not None and keywords != "" and (
                        opt_level == -1 or opt_level == case_level):
                    try:

                        if self.case_store.get(case.get('id')) is None:
                            self.case_store[case.get('id')] = []
                        if case_id is not None and case_id != "":
                            self.case_result.get("total").add(case_id)
                        # 根据keywords触发相应的函数
                        globals().get(case.get("keywords") + "_handler")(self,
                                                                         case)
                        # insert_img(self.driver, case.get("id"), "{}_{}.png".format(index, case.get("desc")))
                        # 保存相应的用例后面校验用  根据用例Id动态生成变量
                        exec("self.case_store['{}'].append(case)".format(
                            case.get('id')))
                    except:
                        failed_desc = "用例Id：{id},步骤描述：{desc}，关键字：{keywords}，选择器：{selector},操作值：{val}".format(
                            **case)  # **case通过字典设置参数
                        traceback_info = traceback.format_exc()
                        print('faileds', failed_desc, traceback_info)
                        self.case_result.get("failed").add(case_id)
                        self.case_result.get("failed_info").append({
                            "failed_desc":
                            failed_desc,
                            "traceback":
                            traceback_info
                        })
        handle_case_result(self.case_result, self.case_store)

        print("---------------全部执行结束--------------------------------")
        # self.driver.quit()

        # driver.quit()


if __name__ == "__main__":
    main_handler = MainHandler()
    main_handler.do_execute()
print("执行完毕，感谢观赏，谢谢！")
'''
python app.py --env=iortho_sit_1 --test_case=execute/demo/appNewCase.xlsx --level=1
新建病例提交
python app.py --env=iortho_sit_znh --test_case=execute/demo/appNewCase11-16.xlsx --level=1
病例已提交编辑病例在提交
python app.py --env=iortho_sit_znh --test_case=execute/demo/appNewCase.xlsx --level=2

# python app.py --env=iortho_sit_1 --test_case=execute/demo2/appNewCase11-16.xlsx --level=1
# python app.py --env=iortho_sit_1 --test_case=execute/demo2/3D-android.xlsx --level=1
python main.py --env=iortho_sit --func=create3d
python work.py --env=iortho_sit --caseid=C01001365678 --num=3d
python work.py --env=iortho_adv --caseid=BC01000032139 --num=3d

python app.py --env=iortho_sit_1 --test_case=execute/demo2/appNewCase12-15-ios.xlsx
python app.py --env=iortho_sit_1 --test_case=execute/demo2/newcase-android.xlsx --level=1
python app.py --env=iortho_sit_1 --test_case=execute/demo2/save_check.xls --level=1 
python app.py --env=iortho_sit_1 --test_case=execute/demo2/crm_check.xls --level=1 


python app.py --env=iortho_sit_1 --test_case=execute/app_newphase/newCase_kid2_A6_004.xls --level=1
#打开3d方案
python app.py --env=iortho_sit --test_case=execute/app/app_3d/3d_click.xls --level=1
python app.py --env=iortho_sit --test_case=execute/demo2/3D-android.xlsx --level=1


python app.py --env=iortho_sit --test_case=execute/app_newphase/test.xlsx --level=1


python app.py --env=iortho_sit --test_case=execute/app_authority/app_doctor_account_authority.xls --level=1
python app.py --env=iortho_sit --test_case=execute/app_authority/app_sale_account_authority.xls --level=1
python app.py --env=iortho_sit --test_case=execute/app_authority/app_graduate_student_authority.xls --level=1
python app.py --env=iortho_sit --test_case=execute/app_authority/app_assistant_account_authority.xls --level=1

################app成人版新建阶段##########################################################################
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_A6_001.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_A6_002.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_A6_003.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_A6_004.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_A6Later_001.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_A6Later_002.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_A6Later_003.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_champion_NoA6.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_comfos.xlsx --level=1
python app.py --env=iortho_sit --test_case=execute/app_newphase/app_newCase_stand.xlsx --level=1
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


python app.py --env=iortho_sit --test_case=execute/app_authority/app_doctor_account_authority.xls --level=1
python app.py --env=iortho_sit --test_case=execute/app_authority/app_sale_account_authority.xls --level=1



'''
