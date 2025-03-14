import sys
from src.logger import logging

def error_message_detail(error_detail:sys):    #error detail is present inside sys
    exc_type , exc_value ,exc_traceback = sys.exc_info()  #exc_tb -> file,line of exception
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{}] line number [{}] error message [{}]".format(
        file_name,exc_traceback.tb_lineno, str(exc_value)   
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_detail:sys):
        super().__init__("An error occured")
        self.error_message = error_message_detail(error_detail)

    def __str__(self):
        return self.error_message


"""
Test if its working
if __name__ =="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(sys)
"""