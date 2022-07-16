import requests
import datetime
from mongo_service import *

class SmsService:

    @staticmethod
    def send_sms(otp, mob_no):
        flag = False
        rq_time = datetime.datetime.now()
        request = {"mob_no": mob_no}
        status = "FAILED"
        url = "https://www.fast2sms.com/dev/bulkV2?variables_values=" + otp + "&route=otp&numbers=" + mob_no
        payload = {}
        headers = {
            'authorization': 'OabjqYu4UDNRQL1Ei8zlTA65IfS07kPxMBhrwosnHd3Gm9FgJtL7blZkOSKhVzn0CoUd62QFtvI1cquf'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if response:
            if response.status_code == 200:
                status = "SUCCESS"
                flag = True

        rs_time = datetime.datetime.now()
        collection_name = "fast2_sms_trxn"

        MongoService.log_response("otp_service", rq_time, request, response, rs_time, url, status, collection_name)

        return flag
