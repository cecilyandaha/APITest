from untils.log_trace import *
import json
class  CheckResult():
    def dict_value(self,key,actual):
        try:
            if key in actual:
                return actual[key]
            else:
                for keys in actual:

                    return self.dict_value(key,actual[keys])
        except Exception as e:
            logging.error(e)
            return None

    def out_dicOrStr(raw_msg):
        if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
            try:
                out_dic=json.loads(raw_msg, encoding='utf-8')
            except ValueError:
                return raw_msg
            return out_dic
        else:
            return str(raw_msg)

    def cmpdict(self,expect,actual,equal):
        logging.info("Begin to check result of  testcase.")
        expect=CheckResult.out_dicOrStr(expect)
        actual = CheckResult.out_dicOrStr(actual)
        is_dict = isinstance(expect,dict) and isinstance(actual,dict)
        is_str = isinstance(expect, str) and isinstance(actual, str)
        if is_dict:
            if equal == "equal":
                for key in expect.keys():
                    if expect[key] == self.dict_value(key,actual):
                        logging.info("%s is equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return True
                    else:
                        logging.error("%s is not equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return False

            if equal == "notequal":
                for key in expect.keys():
                    if key != self.dict_value(key,actual):
                        logging.info("%s is not equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return True
                    else:
                        logging.error("%s is equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return False

            else:
                logging.error("Operator :%s is not support now,you can define it in file[check_result.py]" %equal)

        elif is_str :
            if equal == "equal":
                if expect == actual:
                    logging.info("%s is equal to %s" % (expect, actual))
                    return True
                else:
                    logging.error("%s is not equal to %s" % (expect, actual))
                    return False
            if equal == "notequal":
                if expect != actual:
                    logging.info("%s is not equal to %s" % (expect, actual))
                    return True

                else:
                     logging.error("%s is equal to %s" %(expect,actual))
                     return False

        else:
            logging.error("Expect or actual  result is not dict,check it in  excel. ")



