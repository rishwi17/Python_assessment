class CustomException(Exception):
    def __init__(self,message):
        self.message = message



raise CustomException('My custom exception')
