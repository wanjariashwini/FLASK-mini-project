import pymongo

class MongoDBConnection:
    @staticmethod
    def get_myconnection(database_name):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient[database_name]
        return mydb

    @staticmethod
    def get_mycollection(database_name, collection_name):
        mydb = MongoDBConnection.get_myconnection(database_name)
        my_collection = mydb[collection_name]
        return my_collection

DATABASE_NAME = "otp"


class MongoService:
    @staticmethod
    def log_response(service_name, rq_time, request, response, rs_time, url, status, collection_name):
        conn = MongoDBConnection.get_mycollection(DATABASE_NAME, collection_name)
        document = {"service_name": service_name,
                    "rq_time": rq_time,
                    "request": request,
                    "response": response,
                    "rs_time": rs_time,
                    "url": url,
                    "status": status
                    }
        conn.insert_one(document)



