#Import the sys module to access system-specific functions & parameters
import sys
import logging

def error_message_detail(error,error_detail:sys):
    #exc_info()retuns a tuple of three values (type, value , traceback)
    #ignorning the first two values  we only use traceback
    _,_,exc_tb =error_detail.exc_info()

    #Get the file name where the error occurred
    file_name=exc_tb.tb_frame.f_code.co_filename

    #Construct the error message with the filename, lineno , error msg
    error_message="Error occurred in python script name[{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        '''
        Constructor for the CustomException class

        ARGS:
        error_message(str):the msg associated with the exception
        error_detail(sys):Additional details aboutthe error, i.e a traceback obj

        '''

        # Call the constructor of the superclass(Exception) and pass theerror msg to it
        super().__init__(error_message)

        # Generate a detail error msg using error_message_detail
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        '''
        String representation method for the CustomException class

        REturns a str detailed msg
        '''
        return self.error_message
    
      
    
