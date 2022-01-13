from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class AuthenticateUser(Action):
    def name(self):
        return "authenticate_user"
    def run(self, dispatcher, tracker, domain):
        #get slots
        user_reg = tracker.get_slot('reg_number')
        user_secret = tracker.get_slot('secretkey')

        #url setting
        base_url = 127.0.0.1:8000/api/v1/students/{user_reg}
        url = base_url.format(**{'reg':'user_reg'})

        #get url request data
        res = requests.get(url)

        try:
            api_username = res.json()['second_name']
            api_reg = res.json()['reg_number']
            api_secret = res.json()['secret_key']
            api_year = res.json()['current_year']
            api_course = res.json()['course']
            api_sem = res.json()['current_semester']

            if api_secret == user_secret:
                response = "Welcome {}, how is year {} of {} taking
                you?".format(api_username, api_year, api_course)
                dispatcher.utter_message(response)
            else:
                response = "Sorry, wrong input. Do you want to give it another
                go?"
                dispatcher.utter_message(response)
        except:
            api_message = res.json()
            response = "An {} occured, try again".format(api_message)
        return [SlotSet("user_reg", user_reg), SlotSet("api_year", api_year),
                SlotSet("api_sem", api_sem), SlotTest("api_course",
                    api_course)]

class GetStudentFee(Action):
    def name(self):
        return "get_student_fee"
    def run(self, dispatcher, tracker, domain):
        #get slots
        user_reg = tracker.get_slot('reg_number')

        #url setting
        base_url = 127.0.0.1:8000/api/v1/fee/{user_reg}
        url = base_url.format(**{'reg':'user_reg'})

        #get url request data
        res = requests.get(url)

        try:
            api_fee = res.json()['fee_balance']
            api_cleared = res.json()['cleared']
            api_user = res.json()['second_name']

            if api_cleared == true:
                response = "{}, you have cleared your fee balance, your current
                balance is {} Ksh".format(api_user, api_fee)
                dispatcher.utter_message(response)
            else:
                response = "You have a fee balance of {} Ksh, make sure you clear
                you balance to be allowed to sit for your final
                exams".format(api_fee)
                dispatcher.utter_message(response)
        except:
            api_message = res.json()
            response = "An {} occured, try again".format(api_message)
        return [SlotSet("api_fee", api_fee)]


class GetExamResults(Action):
    def name(self):
        return "get_exam_results"
    def run(self, dispatcher, tracker, domain):
        #get slots
        user_reg = tracker.get_slot('reg_number')

        #url setting
        base_url = 127.0.0.1:8000/api/v1/exam/results/{user_reg}
        url = base_url.format(**{'reg':'user_reg'})

        #get url request data
        res = requests.get(url)

        try:
            for a in res:
                api_grade = a.json()['grade']
                api_unit = a.json()['unit_title']
                api_score = a.json()['score']
                api_remark = a.json()['remark']
                api_user = a.json()['second_name']
                results = "Unit title: {}, Unit score: {}, Unit grade: {}, Unit
                remark:{}".format(api_unit, api_score, api_grade, api_remark)
                dispatcher.utter_message(results)

            if api_score > int(api_score):
                response = "What a great score in your exam, congrats {}".format(api_user)
                dispatcher.utter_message(response)
            else:
                response = "Dissapointing score, you get them next time"
                dispatcher.utter_message(response)
        except:
            api_message = res.json()
            response = "An {} occured, try again".format(api_message)
    return []



class GetEnrol(Action):
    def name(self):
        return "get_enrol"
    def run(self, dispatcher, tracker, domain):
        #get slots
        user_reg = tracker.get_slot('reg_number')

        #url setting
        base_url = 127.0.0.1:8000/api/v1/enrol/{user_reg}
        url = base_url.format(**{'reg':'user_reg'})

        #get url request data
        res = requests.get(url)

        try:
            api_status = res.json()['enrol_status']
            api_semester = res.json()['semester']
            api_user = res.json()['second_name']

            if api_status == true:
                response = "{}, you have registered , for semester
                {}".format(api_user, api_semester)
                dispatcher.utter_message(response)
            else:
                response = "You have not registered for semester
                {}".format(api_semester)
                dispatcher.utter_message(response)
        except:
            api_message = res.json()
            response = "An {} occured, try again".format(api_message)
        return [SlotSet("api_status", api_status)]

#class SetEnrol(Action):
#    def name(self):
#        return "set_enrol"
#    def run(self, dispatcher, tracker, domain):
#        #get slots
#        user_reg = tracker.get_slot('reg_number')
#
#        #url setting
#        base_url = 127.0.0.1:8000/api/v1/enrol/{user_reg}
#        url = base_url.format(**{'reg':'user_reg'})
#
#        #get url request data
#        res = requests.get(url)
#
#        try:
#            api_status = res.json()['enrol_status']
#            api_semester = res.json()['semester']
##            api_user = res.json()['second_name']
#
#            if api_status == true:
#                response = "{}, you have registered , for semester
#                {}".format(api_user, api_semester)
#                dispatcher.utter_message(response)
#            else:
#                response = "You have not registered for semester
#               {}".format(api_semester)
#              dispatcher.utter_message(response)
#        except:
#            api_message = res.json()
#            response = "An {} occured, try again".format(api_message)
#        return [SlotSet("api_status", api_status)]
#
#






