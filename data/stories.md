##get fee
*greeting
    -utter_greet

*get_reg{"reg_number":"0334"}
    -slot{"reg_number":"0345"}
    -utter_ask_key

*get_secret{"secretkey":"secret"}
    -slot{"secretkey":"secret"}
    -authenticate_user

*get_mood{"mood":"good"}
    -slot{"mood":"bad"}
    -get_mood
    -utter_ask_request

*get_fee
    -get_student_fee
    -utter_thanks

##get exam results
*greeting
    -utter_greet

*get_reg{"reg_number":"0334"}
    -slot{"reg_number":"0345"}
    -utter_ask_key

*get_secret{"secretkey":"secret"}
    -slot{"secretkey":"secret"}
    -authenticate_user

*get_mood{"mood":"good"}
    -slot{"mood":"bad"}
    -get_mood
    -utter_ask_request

*get_results
    -get_exam_results
    -utter_thanks

##Get status
*greeting
    -utter_greet

*get_reg{"reg_number":"0334"}
    -slot{"reg_number":"0345"}
    -utter_ask_key

*get_secret{"secretkey":"secret"}
    -slot{"secretkey":"secret"}
    -authenticate_user

*get_mood{"mood":"good"}
    -slot{"mood":"bad"}
    -get_mood
    -utter_ask_request

*get_enrollmentStatus
    -get_enrol
    -utter_thanks


