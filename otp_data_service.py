import mysql.connector
import random
import uuid
from datetime import datetime
from fast2_sms_service import *


class MySQLConnector:
    conn = None
    cursor = None

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            # port="3",
            user="root",
            password="root",
            database="Employee_management"
        )
        self.cursor = self.conn.cursor()


class OTPOperation:

    @staticmethod
    def send_otp(input_request, user):
        status = False
        if input_request:
            otp_method = input_request.get("otp_method")
            transaction_id = uuid.uuid4()
            transaction_details = str(transaction_id) + " " + user
            if otp_method == "sms":
                mdn = input_request.get("mdn")
                otp = random.randint(100000, 999999)
                status = SmsService.send_sms(otp, mdn)
                now = datetime.now()
                date_time = now.strftime("%d-%m-%Y T %H:%M:%S:%f")
                if status:
                    session_key = uuid.uuid4()
                    record = {"txn_id": transaction_details, "session_key": session_key, "status":"success",
                              "date_time": date_time}
                    return record
                else:
                    record = {"txn_id": transaction_details, "status": "failed", "date_time": date_time}
                    return record
            else:
                email = input_request.get("email")
                otp = random.randint(100000, 999999)
                status = EmailService.send_email(otp, email)
                now = datetime.now()
                date_time = now.strftime("%d-%m-%Y T %H:%M:%S:%f")
                if status:
                    session_key = uuid.uuid4()
                    record = {"txn_id": transaction_details, "session_key": session_key, "status": "success",
                              "date_time": date_time}
                    return record
                else:
                    record = {"txn_id": transaction_details, "status": "failed", "date_time": date_time}
                    return record

    @staticmethod
    def send_message(input_request):
        email = input_request.get("email_id")
        name = input_request.get("user_name")
        file1 = open("otp.txt", "r")
        OTP = file1.readline()
        print(OTP)
        file1.close()

        if email and OTP:
            return True
        else:
            return False

    @staticmethod
    def otp_validate(otp_data):
        status = False
        if otp_data:
            otp = otp_data.get("otp")
            status = False
            file1 = open("otp.txt", "r")
            OTP = file1.readline()
            print(OTP)
            file1.close()
            # OTP = int(OTP)
            if otp == OTP:
                status = True
                return status
            else:
                return status

        return status

    @staticmethod
    def is_user_valid(auth):
        if auth:
            username = auth.get("username")
            password = auth.get("password")
            data = {"username": "pankaj", "password": "pankaj@123"}
            if username == data.get("username") and password == data.get("password"):
                return True
            else:
                return False

        return False
