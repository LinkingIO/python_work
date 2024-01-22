import unittest

class AnonymousSurvey():
    """收集匿名调查问卷答案"""
    def __init__(self, question) -> None:
        """存储一个问题，并且初始化存储答案"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份问题调查答案"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        print(' - '.join(self.responses))

# #定义一个问题
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
        
# # 显示问题并存储答案
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while(True):
#     response = input('Language: ')
#     if response == 'q':
#         break
#     my_survey.store_response(response)
        
# # 显示调查结果
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()
        
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案是否符合"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Mandarin')

        self.assertIn('Mandarin', my_survey.responses)

    def test_store_three_responses(self):
        """测试 3 个答案是否正确"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['Mandarin', 'English', 'Japanise']

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()