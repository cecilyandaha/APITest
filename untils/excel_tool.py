#coding:utf-8
import xlrd
from untils.log_trace import *
from xlutils.copy import copy
from untils.load_conf import excel_config

class excel_tool():

    def __init__(self,excel_name):

        self.curr_excel = xlrd.open_workbook(excel_name)
        self.table = self.curr_excel.sheet_by_index(0)
        #print(self.table.cell(1,1).value)
        #实例化excel_config
        self.config = excel_config()
        self.rows = self.table.nrows
        self.excel_name = excel_name


    #获取用例编号
    def get_caseno(self,row):
        caseno = self.table.cell(row,self.config.caseno_col()).value
        if caseno:
            return caseno
        else:
            logging.info("case no is null")
            return None

    #获取用例名称
    def get_casename(self,row):
        casename = self.table.cell(row,self.config.casename_col()).value
        return casename

    #获取是否运行标志
    def get_runflag(self,row):
        run_flag = self.table.cell(row,self.config.isrun_col()).value
        return run_flag

    #获取用例级别
    def get_caselevel(self,row):
        caselevel = self.table.cell(row,self.config.level_col()).value
        return caselevel

    #获取请求url
    def get_caseurl(self,row):
        caseurl = self.table.cell(row,self.config.caseurl_col()).value
        return caseurl

    #获取请求body
    def get_casebody(self,row):
        case_body = self.table.cell(row,self.config.casebody_col()).value
        return case_body

    #获取header
    def get_headerflag(self,row):
        headerflag = self.table.cell(row,self.config.header_col()).value
        return headerflag

    #获取coocikes
    def get_cookiesflag(self,row):
        cookiesflag = self.table.cell(row,self.config.cookies_col()).value
        return cookiesflag

    #获取请求类型
    def get_methodtype(self,row):
        method_type = self.table.cell(row,self.config.reqtype_col()).value
        return method_type
    #获取预期结果
    def get_expectres(self,row):
        expect_res = self.table.cell(row,self.config.expectresult_col()).value
        return expect_res

    #获取测试结果
    def get_testres(self,row):
        test_res= self.table.cell(row,self.config.testresult_col()).value
        return test_res
    #获取操作符
    def get_operator(self,row):
        operator = self.table.cell(row,self.config.test_operator_col()).value
        return operator

    #回写测试结果到excel
    def write_testres(self,row,value):
        wbook = copy(xlrd.open_workbook(self.excel_name))
        sheet = wbook.get_sheet(0)
        sheet.write(row, self.config.testresult_col(), value)
        wbook.save(self.excel_name)
    #回写实际结果
    def write_actualres(self,row,value):
        wbook = copy(xlrd.open_workbook(self.excel_name))
        sheet = wbook.get_sheet(0)
        sheet.write(row, self.config.actualresult_col(), value)
        wbook.save(self.excel_name)