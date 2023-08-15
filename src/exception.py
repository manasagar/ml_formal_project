import sys
import logging

def error_message_details(error, exc_info):
    _, _, exc_tb = exc_info
    file_path = exc_tb.tb_frame.f_code.co_filename
    error_message = f"An error occurred in pythonscript of name [{file_path}] in line [{exc_tb.tb_lineno}] error [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, exc_info=error_details)
        
    def __str__(self):
        return self.error_message

# if __name__ == '__main__':
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.basicConfig(level=logging.INFO)  # Configure logging
#         logging.info("Logging has started")
#         raise CustomException(str(e), sys.exc_info())
