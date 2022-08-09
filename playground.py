# customer_status = customer_wallet.account.status

# class StatusChoice():
#     ACTIVE = "Active"    

# customer_status = "Active"

# def check_status(customer_status):
#     # print(StatusChoice.ACTIVE)
#     # print(customer_status)
#     if customer_status is not StatusChoice.ACTIVE:
#         # print(StatusChoice.ACTIVE)
#         # print(customer_status)
#         # print(customer_status) 
#         return True


# customer_status = "Active"
# # check_status("Active")

# print(check_status(customer_status))

# The getattr() function returns the value of the specified attribute from the specified object.
# Use the "default" parameter to write a message when the attribute does not exist.
# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"


# x = getattr(Person, "no", "hello")
# print(x)


# class Booking():
#     PAYMENT_STATUSES = (
#         ('COM', 'PAYMENT_COMPLETE'),
#         ('INC', 'PAYMENT_INCOMPLETE'),
#         ('PAR', 'PAYMENT_PARTIALLY_COMPLETE'),
#     )


# print(Booking.PAYMENT_STATUSES[0][1])


# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(List[:2])


data = {"msg": {
            "date": "2022-08-08T11:31:56.505Z",
            "amount": 0.1,
            "eTime": "220808113232",
            "author": "WINGIPAY",
            "type": "W2A",
            "holderID": "625e729988f4b9162086bed1",
            "operator": "ThirdParty",
            "narration": "",
            "__v": 0,
            "receivingHse": {
                "balAfter": "N/A",
                "result": {
                    "msg": "Transaction successful.",
                    "code": "00",
                    "houseID": "625e729988f4b9162086bed1",
                    "transactionID": "18590636311"
                },
                "country": "GH",
                "houseID": "625e729988f4b9162086bed1",
                "accountName": "N/A",
                "balBefore": "0.0",
                "mapID": "SAME_HOUSE",
                "mapName": "SAME_HOUSE",
                "refID": "WINGIPAYd96118f8-db52-44fa-9f0f-fb50467b23eb",
                "shortName": "WINGIPAY",
                "userID": "NOT_PROVIDED"
            },
            "sendingHse": {
                "balAfter": "123.98999999999995",
                "result": {
                    "msg": "Transaction successful.",
                    "code": "00",
                    "system_msg": "",
                    "system_code": "SUCCESSFUL",
                    "transactionID": "18590636311"
                },
                "country": "GH",
                "houseID": "55df15fa12ece2fa3b91c54f",
                "balBefore": "123.88999999999996",
                "mapID": "COLLECTIONS",
                "mapName": "collections",
                "refID": "fjos10b6mujk",
                "shortName": "MTN",
                "userID": "0543418718"
            },
            "_id": "62f0f42c136bfe812b239082",
            "msisdn": "NOT_PROVIDED",
            "sTime": "220808113156",
            "desc": "WINGIPAY sending debit request on MTN"
        },
        "code": "00"
    }

print(data["msg"]["sendingHse"]["result"]["system_code"])