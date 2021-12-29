from Common.com_sql.eddid_sit_库链接 import SQL_Check
import json
from Config.cdms_config import *
SQL_Check = SQL_Check()


def get_code(phone):
    print("查询申请单的手机号码为为：{}".format(phone))
    sms_auth_code = SQL_Check.coonect_db_zh(database=sqldata_h5,
                               sql="SELECT created_date,receiver,metadata FROM push_message WHERE receiver LIKE '%{}%' ORDER BY created_date DESC LIMIT 1;".format(
                                  phone))
    return json.loads(sms_auth_code[0][2])["templateParam"]["sms_auth_code"]


# print("get_code:",json.dumps(get_code(19310250624)))

# print("get_code:",json.loads(get_code(19310250624))["templateParam"]["sms_auth_code"])
if __name__ == "__main__":
    print("get_code:",(get_code(19310250624)))