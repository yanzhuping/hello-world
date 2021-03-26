import re



#全局变量
global_vars={}

# #全局变量设置列表
# set_global_vars = [{"name": "accountId", "query": ["data","assistantList" ,0, 'accountId']},
#                    {"name": "accountId1", "query": ["data","assistantList" ,1, 'accountId']},
#                    {"name": "accountId2", "query": ["data","assistantList" ,2, 'accountId']},
#                    {"name": "spreadId", "query": ["doctorSpreadList",0 , 'spreadId']},
#                    {"name": "spreadId1", "query": ["doctorSpreadList",1, 'spreadId']},
#                    {"name": "pcId", "query": ["data","imageList", 20,'pcId']},
#                    {"name": "pcId1", "query": ["data","imageList", 0,'pcId']},
#                    {"name": "attId", "query": ["data","imageList", 0,'attId']},
#                    {"name": "makeit_attId", "query": ['attId']},
#                    {"name": "caseId", "query": ['caseId']},
#                    {"name": "tidingsId", "query": ['tidingsId']},
#                    {"name":"patientname","query":["cases",0,"name"]}
#
#                    ]

#获取多层嵌套的字典中的某个值
def dict_get(dic, locators, default=None):
    '''
    :param dic: 输入需要在其中取值的原始字典 <dict>,即接口响应数据
    :param locators: 输入取值定位器, 如:['result', 'msg', '-1', 'status'] <list>
    :param default: 进行取值中报错时所返回的默认值 (default: None)
    :return: 返回根据参数locators找出的值
    '''
    if not isinstance(dic, dict) or not isinstance(locators, list):
        return default

    value = None

    for locator in locators:
        if not type(value) in [dict, list] and isinstance(locator, str) and not can_convert_to_int(locator):
            try:
                value = dic[locator]
            except KeyError:
                return default
            continue
        if isinstance(value, dict):
            try:
                value = dict_get(value, [locator])
            except KeyError:
                return default
            continue
        if isinstance(value, list) and can_convert_to_int(locator):
            try:
                value = value[int(locator)]
            except IndexError:
                return default
            continue

    return value

def can_convert_to_int(input):
    try:
        int(input)
        return True
    except BaseException:
        return False

# 抽取接口的返回值存储到全局变量字典中
def set_global(set_global_vars,response_json):

    if set_global_vars and isinstance(set_global_vars, list):
        for set_global_var in set_global_vars:
            if isinstance(set_global_var, dict):
                name = set_global_var.get('name') # name 代表全局变量的名字
                query = set_global_var.get('query') # query 代表全局变量的查询语句
                value = dict_get(response_json, query) # response_json 代表接口的响应数据
                if value==None or value=="":
                    continue
                else:
                    global_vars[name] = value

        # print(global_vars)
        return global_vars


# 解析字符串中全局变量并进行替换
def resolve_global_var(pre_resolve_var, global_var_dic, global_var_regex='\${.*?}',
          match2key_sub_string_start_index=2, match2key_sub_string_end_index=-1):

  '''
  :param pre_resolve_var: 准备进行解析的变量<str>
  :param global_var_dic: 全局变量字典<dict>
  :param global_var_regex: 识别全局变量正则表达式<str>
  :param match2key_sub_string_start_index: 全局变量表达式截取成全局变量字典key值字符串的开始索引<int>
  :param match2key_sub_string_end_index: 全局变量表达式截取成全局变量字典key值字符串的结束索引<int>
  :return: 解析后的变量<str>
  '''
  if not isinstance(pre_resolve_var, str):
    raise TypeError('pre_resolve_var must be str！')

  if not isinstance(global_var_dic, dict):
    raise TypeError('global_var_dic must be dict！')

  if not isinstance(global_var_regex, str):
    raise TypeError('global_var_regex must be str！')

  if not isinstance(match2key_sub_string_start_index, int):
    raise TypeError('match2key_sub_string_start_index must be int！')

  if not isinstance(match2key_sub_string_end_index, int):
    raise TypeError('match2key_sub_string_end_index must be int！')

  re_global_var = re.compile(global_var_regex)

  def global_var_repl(match_obj):
    start_index = match2key_sub_string_start_index
    end_index = match2key_sub_string_end_index
    match_value = global_var_dic.get(match_obj.group()[start_index:end_index])
    return match_value if match_value else match_obj.group()

  resolved_var = re.sub(pattern=re_global_var, string=pre_resolve_var, repl=global_var_repl)
  return resolved_var

"""
这里，首先先创建识别全局变量的正则规则，然后运用re.sub方法进行替换。其中，re.sub中的repl参数可接受函数作为参数。global_var_repl方法中，
使用global_var_dic字典去获取匹配的值并返回。
默认参数中，将全局变量做了这样一个识别: ${GLOBALVAR_NAME}, 用global_var_dic查找并替换全局变量时，则使用了默认预设的起止索引参数
"""

if __name__ == '__main__':


    response_json = {'status': '1', 'errorCode': '', 'msg': '成功',
                     'data': {
                         'assistantList': [
                             {'accountId': 2050, 'accountType': 3, 'accountName': '啊飒飒', 'avatar': '', 'bucketId': 0,
                              'userId': 0, 'mobile': '', 'mail': '',
                              'org': [{'crmOrgCode': 'H201012070002', 'crmOrgName': '深圳市儿童医院', 'isBinding': '1'},
                                      {'crmOrgCode': 'H201012070519', 'crmOrgName': '上海市第十人民医院', 'isBinding': '0'},
                                      {'crmOrgCode': 'H201303150001', 'crmOrgName': '上海天智口腔门诊部', 'isBinding': '0'}]},
                             {'accountId': 2054, 'accountType': 3, 'accountName': '接口测试普通助理', 'avatar': '',
                              'bucketId': 0, 'userId': 0, 'mobile': '', 'mail': '',
                              'org': [{'crmOrgCode': 'H201012070002', 'crmOrgName': '深圳市儿童医院', 'isBinding': '1'},
                                      {'crmOrgCode': 'H201012070519', 'crmOrgName': '上海市第十人民医院', 'isBinding': '0'},
                                      {'crmOrgCode': 'H201303150001', 'crmOrgName': '上海天智口腔门诊部', 'isBinding': '0'}]},
                             {'accountId': 2055, 'accountType': 9, 'accountName': '接口测试高级助理', 'avatar': '',
                              'bucketId': 0, 'userId': 0, 'mobile': '', 'mail': '',
                              'org': [{'crmOrgCode': 'H201012070002', 'crmOrgName': '深圳市儿童医院', 'isBinding': '1'},
                                      {'crmOrgCode': 'H201012070519', 'crmOrgName': '上海市第十人民医院', 'isBinding': '0'},
                                      {'crmOrgCode': 'H201303150001', 'crmOrgName': '上海天智口腔门诊部', 'isBinding': '0'}]},
                             {'accountId': 2057, 'accountType': 3, 'accountName': '接口测试普通助理', 'avatar': '',
                              'bucketId': 0, 'userId': 0, 'mobile': '', 'mail': '',
                              'org': [{'crmOrgCode': 'H201012070002', 'crmOrgName': '深圳市儿童医院', 'isBinding': '1'},
                                      {'crmOrgCode': 'H201012070519', 'crmOrgName': '上海市第十人民医院', 'isBinding': '0'},
                                      {'crmOrgCode': 'H201303150001', 'crmOrgName': '上海天智口腔门诊部', 'isBinding': '0'}]},
                             {'accountId': 2058, 'accountType': 9, 'accountName': '接口测试高级助理', 'avatar': '',
                              'bucketId': 0, 'userId': 0, 'mobile': '', 'mail': '',
                              'org': [{'crmOrgCode': 'H201012070002', 'crmOrgName': '深圳市儿童医院', 'isBinding': '1'},
                                      {'crmOrgCode': 'H201012070519', 'crmOrgName': '上海市第十人民医院', 'isBinding': '0'},
                                      {'crmOrgCode': 'H201303150001', 'crmOrgName': '上海天智口腔门诊部', 'isBinding': '0'}]},
                             {'accountId': 2060, 'accountType': 3, 'accountName': '接口测试普通助理', 'avatar': '',
                              'bucketId': 0, 'userId': 0, 'mobile': '', 'mail': '',
                              'org': [{'crmOrgCode': 'H201012070002', 'crmOrgName': '深圳市儿童医院', 'isBinding': '1'},
                                      {'crmOrgCode': 'H201012070519', 'crmOrgName': '上海市第十人民医院', 'isBinding': '0'},
                                      {'crmOrgCode': 'H201303150001', 'crmOrgName': '上海天智口腔门诊部', 'isBinding': '0'}]},
                             {'accountId': 2061, 'accountType': 9, 'accountName': '接口测试高级助理', 'avatar': '',
                              'bucketId': 0, 'userId': 0, 'mobile': '', 'mail': '',
                              'org': [{'crmOrgCode': 'H201012070002', 'crmOrgName': '深圳市儿童医院', 'isBinding': '1'},
                                      {'crmOrgCode': 'H201012070519', 'crmOrgName': '上海市第十人民医院', 'isBinding': '0'},
                                      {'crmOrgCode': 'H201303150001', 'crmOrgName': '上海天智口腔门诊部', 'isBinding': '0'}]}]}}


    set_global(set_global_vars,response_json)

