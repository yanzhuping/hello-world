
# -*- coding:UTF-8 -*-
import sys
from libs.keywords_trans import *
from driver.driver import *
import traceback
from libs.global_vars import *

from selenium.common.exceptions import TimeoutException


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
        self.case_result = {'total': set(), 'failed': set()}
        # 存储元素选择器json
        self.ele_selector_store = {}

    def do_execute(self):
        if self.t_opt.get('func') == "create3d":
            create3d_auto_handler(self)
        elif self.t_opt.get('func') == "endphase":
            finish_phase_auto_handler(self)
        elif self.t_opt.get('func') == 'appcds':
            app_check_cds_handler(self)
        else:
            # 读取所有的用例
            file_list = list_dir(get_execute_dir(
                self.t_opt.get("test_case")))  # 将指定路径下的所有文件路径存储于列表中
            # 命令行读取到的level
            opt_level = str(self.t_opt.get("level",
                                           '-1'))  # 如果level字段为空，则默认给一个-1
            for file_path in file_list:
                # 读取excel中的用例
                print(file_path)
                case_list = read_excel(file_path)
                # index从0开始，case是读取的excel每一行的数据，类型是字典
                for index, case in enumerate(case_list):
                    case['keyexpression'] = case.get('selector')
                    case_id = case.get("id")
                    if len(self.case_store) != 0:
                        case_store_keys = list(self.case_store.keys())
                        # 取最后一个key
                        pre_caseid = case_store_keys[-1]
                        # 执行一个新的caseId（新用例）时，如果上个用例没有失败就在case_store删除保存的用例
                        if case_id not in case_store_keys and pre_caseid not in self.case_result.get(
                                "failed"):
                            self.case_store.pop(pre_caseid)
                    keywords = case.get("keywords")
                    # 根据key从json文件获取选择器
                    get_selector_val(self, case)
                    # 用例中的level项
                    case_level = format_digit_str(case.get("level"))
                    # 关键词存在并且用例的level和命令行指定的level一致（命令行没有指定level除外）
                    if keywords is not None and keywords != "" and (
                            opt_level == '-1' or opt_level == case_level):
                        try:
                            if self.case_store.get(case.get('id')) is None:
                                self.case_store[case.get('id')] = []
                            if case_id is not None and case_id != "":
                                self.case_result.get("total").add(case_id)
                            # 根据keywords触发相应的函数
                            globals().get(case.get("keywords") + "_handler")(
                                self, case)
                            try:
                                insert_img(
                                    self.driver, case_id, "{}_{}.png".format(
                                        case_id,
                                        len(self.case_store.get(case_id))))
                            except:
                                pass
                            # 保存相应的用例后面校验用  根据用例Id动态生成变量
                            self.case_store[case.get('id')].append(case)
                        except:
                            insert_img(
                                self.driver, case_id, "{}_{}.png".format(
                                    case_id,
                                    len(self.case_store.get(case_id))))
                            failed_desc = "用例Id：{id},步骤描述：{desc}，关键字：{keywords}，元素关键字：{keyexpression}，选择器：{selector},操作值：{val}".format(
                                **case)  # **case通过字典设置参数
                            traceback_info = traceback.format_exc()
                            print(failed_desc)
                            print(traceback_info)
                            self.case_result.get("failed").add(case_id)
                            case["traceback"] = traceback_info
                            self.case_store[case.get('id')].append(case)
                # print(uploadPhotoList)
                #将存在全局变量中global_var的照片删除
                for i in range(len(uploadPhotoList)):
                    # print(uploadPhotoList)
                    uploadPhotoList.pop()
                # print(uploadPhotoList)
                self.driver.quit()
                self.driver = browser()

            handle_case_result(self.case_result, self.case_store)

        print("---------------全部执行结束--------------------------------")
        self.driver.quit()


if __name__ == "__main__":
    main_handler = MainHandler()
    main_handler.do_execute()
'''
python main.py --env=iortho_sit --test_case=execute/champion-mid-C.xlsx  --level=-1
自动创建3d
python main.py --env=iortho_sit --func=create3d --casecode=C01001487640 --phase=1 --type=1 --update
phase 1:新病例 2:中期
type 1:A7 2:A8 3:邻面去油
结束当前阶段
python main.py --env=iortho_sit --func=endphase --casecode=C01001264003

#海外版
python main.py --env=iortho_sit_web --test_case=execute/authority/foreign_account_authority.xls --level=1
#销售和职能
python main.py --env=iortho_sit_sale --test_case=execute/authority/sale_account_authority.xls --level=1
python main.py --env=iortho_sit_sale --test_case=execute/authority/staff_account_authority.xls --level=1
#助理
python main.py --env=iortho_sit_assistant --test_case=execute/authority/assistant_account_authority.xls --level=1
#高级助理
python main.py --env=iortho_sit_high_assistant --test_case=execute/authority/high_assistant_account_authority.xls --level=1
#医生
python main.py --env=iortho_sit --test_case=execute/authority/doctor_account_authority.xls --level=1
#makeit医生
python main.py --env=iortho_sit --test_case=execute/authority/makeit_assistant_authority.xls --level=1


#学生
python main.py --env=iortho_sit_student --test_case=execute/authority/graduate_student_authority.xls --level=1
#es
python main.py --env=iortho_sit_es --test_case=execute/es/es_doctor_account_authority.xls --level=1

冠军、标准、comfos新建阶段自动化
python main.py --env=iortho_sit --test_case=execute/newphase
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_stand_001.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_comfos_001.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_champion_NoA6_001.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_champion_A6_001.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_kid2_A6_002.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_kid2_A6_003.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_kid2_A6_004.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_kid2_A6Later_001.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_kid2_A6Later_002.xls
python main.py --env=iortho_sit --test_case=execute/newphase/newCase_kid2_A6Later_003.xls

完成阶段自动化
python main.py --env=iortho_sit --test_case=execute/finishphase/finish_1.xls
python main.py --env=iortho_sit --test_case=execute/finishphase/finish_2.xls
python main.py --env=iortho_sit --test_case=execute/finishphase/finish_3.xls
python main.py --env=iortho_sit --test_case=execute/finishphase/finish_4.xls

消息自动化
#所有的消息
python main.py --env=iortho_sit --test_case=execute/message_assert
#解绑机构和绑定机构消息验证
python main.py --env=iortho_sit --test_case=execute/message_assert/bindingMechanism.xls
python main.py --env=iortho_sit --test_case=execute/message_assert/unBindingMechanism.xls
#删除病例消息
python main.py --env=iortho_sit --test_case=execute/message_assert/deleteCase.xls
#创建医生并删除
python main.py --env=iortho_sit --test_case=execute/message_assert/deleteDoctor.xls
#完成病例
python main.py --env=iortho_sit --test_case=execute/message_assert/finishCase.xls
#3D相关的消息
python main.py --env=iortho_sit --test_case=execute/message_assert/plan3D.xls
#转诊，包括同一个医生的不同机构、同一个机构的不同医生
python main.py --env=iortho_sit --test_case=execute/message_assert/transferCase.xls

#儿童版新病例,配置在config.ini
python main.py --env=iortho_sit_qinmd --test_case=execute/newphase_kid/newCase_kid_001.xls
#儿童版中期
python main.py --env=iortho_sit_qinmd --test_case=execute/metaphase_gb_kid/metaphase_gb_kid_001.xls


消息自动化
python main.py --env=iortho_sit --test_case=execute/crmnews/ --level=1

##############################中期自动化############################################

中期AB套
python main.py --env=iortho_sit --test_case=execute/metaphase_ab
中期CD套
python main.py --env=iortho_sit --test_case=execute/metaphase_cd
中期冠军非A6+标准中期+comfos中期
python main.py --env=iortho_sit --test_case=execute/metaphase_common

中期自动化a套
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_a_001.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_a_002.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_a_003.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_a_004.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_a_005.xls

中期自动化b套
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_b_001.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_b_002.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_b_003.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_b_004.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_b_005.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_b_006.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_ab/champion_midCase_b_007.xls

中期自动化c套
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_c_001.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_c_002.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_c_003.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_c_004.xls

中期自动化d套
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_d_001.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_d_002.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_d_003.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_d_004.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_cd/champion_midCase_d_005.xls


成人版非A6中期
python main.py --env=iortho_sit --test_case=execute/metaphase_common/champion_midCase_NoA6_001.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_common/champion_midCase_NoA6_002.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_common/champion_midCase_NoA6_003.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_common/champion_midCase_NoA6_004.xls

标准版中期
python main.py --env=iortho_sit --test_case=execute/metaphase_common/stand_midCase_001.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_common/stand_midCase_002.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_common/stand_midCase_003.xls

comfos中期
python main.py --env=iortho_sit --test_case=execute/metaphase_common/comfos_midCase_001.xls
python main.py --env=iortho_sit --test_case=execute/metaphase_common/comfos_midCase_002.xls

############################iortho的相关功能##################################################
星标功能/存档功能
python main.py --env=iortho_sit --test_case=execute/iortho_fun
#星标功能
python main.py --env=iortho_sit --test_case=execute/iortho_fun/starflag.xls
#存档功能
python main.py --env=iortho_sit --test_case=execute/iortho_fun/archive.xls
#助理创建、删除功能
python main.py --env=iortho_sit --test_case=execute/iortho_fun/assistant.xls
#备注功能
python main.py --env=iortho_sit --test_case=execute/iortho_fun/note.xls
#各个入口进入3D批准方案、验证3D内的历史方案、矫治说明等按钮
python main.py --env=iortho_sit --test_case=execute/iortho_fun/3D_approve.xls
#各个入口意见反馈+3D超时重传模型
python main.py --env=iortho_sit --test_case=execute/iortho_fun/3D_feedback.xls


####################海外版病例流程###############################################################
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases
新建病例并且检验照片、cds加工单、收货记录
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases/overseas_champion_A6.xls
质检不合格
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases/overseas_QA.xls
病例资料待完善
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases/overseas_dataToBeImproved.xls
创建3D并批准
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases/overseas_3D.xls
普通标准版中期提交
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases/overseas_stand_midCase.xls
中期阶段创建3D方案并意见反馈
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases/overseas_mid_3D.xls
完成阶段
python main.py --env=iortho_sit_web --test_case=execute/overseas_cases/overseas_finish.xls
'''
