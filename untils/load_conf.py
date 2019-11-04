import  configparser

'''
read conf from setting.conf
@:parameter:identstr,value_type
value_type:"int" or "str"
'''
def lood_conf(identstr,value_type):
    cf = configparser.ConfigParser()
    cf.read("../config/settings.conf")

    idenlist = identstr.split('.')

    if value_type == "int":
        try:
         value = cf.getint(idenlist[0],idenlist[1])
         return  value
        except (configparser.NoSectionError ,configparser.NoOptionError) as e:
            print(e)
    if value_type == "str":
        try:
            value = cf.get(idenlist[0],idenlist[1])
            return value
        except (configparser.NoSectionError ,configparser.NoOptionError) as e:
            print(e)

'''
获取url，request body等的列号
'''
class excel_config():
    #获取用例编号的列
    def caseno_col(self):
        return lood_conf("excel.case_no","int")

    def casename_col(self):
        return lood_conf("excel.case_name","int")

    def isrun_col(self):
        #print(lood_conf("excel.is_run","int"))
        return lood_conf("excel.is_run","int")

    def level_col(self):
        return lood_conf("excel.case_level","int")

    def header_col(self):
        return lood_conf("excel.case_header","int")

    def cookies_col(self):
        return lood_conf("excel.case_cookies","int")

    def reqtype_col(self):
        return lood_conf("excel.req_type","int")

    def caseurl_col(self):
        return lood_conf("excel.case_url","int")

    def casebody_col(self):
        return lood_conf("excel.case_body","int")

    def expectresult_col(self):
        return lood_conf("excel.expect_result","int")

    def actualresult_col(self):
        return lood_conf("excel.actual_result","int")

    def testresult_col(self):
        return lood_conf("excel.test_result","int")

    def test_operator_col(self):
        return lood_conf("excel.operator","int")