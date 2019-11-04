import  logging
filename = "../report/test_case_run.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s1 %(filename)s [line:%(lineno)d]  %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=filename,
                    filemode='w')