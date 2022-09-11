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


# data = {"msg": {
#             "date": "2022-08-08T11:31:56.505Z",
#             "amount": 0.1,
#             "eTime": "220808113232",
#             "author": "WINGIPAY",
#             "type": "W2A",
#             "holderID": "625e729988f4b9162086bed1",
#             "operator": "ThirdParty",
#             "narration": "",
#             "__v": 0,
#             "receivingHse": {
#                 "balAfter": "N/A",
#                 "result": {
#                     "msg": "Transaction successful.",
#                     "code": "00",
#                     "houseID": "625e729988f4b9162086bed1",
#                     "transactionID": "18590636311"
#                 },
#                 "country": "GH",
#                 "houseID": "625e729988f4b9162086bed1",
#                 "accountName": "N/A",
#                 "balBefore": "0.0",
#                 "mapID": "SAME_HOUSE",
#                 "mapName": "SAME_HOUSE",
#                 "refID": "WINGIPAYd96118f8-db52-44fa-9f0f-fb50467b23eb",
#                 "shortName": "WINGIPAY",
#                 "userID": "NOT_PROVIDED"
#             },
#             "sendingHse": {
#                 "balAfter": "123.98999999999995",
#                 "result": {
#                     "msg": "Transaction successful.",
#                     "code": "00",
#                     "system_msg": "",
#                     "system_code": "SUCCESSFUL",
#                     "transactionID": "18590636311"
#                 },
#                 "country": "GH",
#                 "houseID": "55df15fa12ece2fa3b91c54f",
#                 "balBefore": "123.88999999999996",
#                 "mapID": "COLLECTIONS",
#                 "mapName": "collections",
#                 "refID": "fjos10b6mujk",
#                 "shortName": "MTN",
#                 "userID": "0543418718"
#             },
#             "_id": "62f0f42c136bfe812b239082",
#             "msisdn": "NOT_PROVIDED",
#             "sTime": "220808113156",
#             "desc": "WINGIPAY sending debit request on MTN"
#         },
#         "code": "00"
#     }

# print(data["msg"]["sendingHse"]["result"]["system_code"])

# data = [
#           {
#               "sex": "Male",
#               "email": "pmarks1914@gmail.com",
#               "balance": -960,
#               "program": "DBS STATISTICS",
#               "currency": "GHS",
#               "fee_type": 1,
#               "mobileNo": "0206358827",
#               "accountNo": "01190001N",
#               "full_name": "DADZIE DERRICK ",
#               "last_name": "",
#               "studentId": "01190001N",
#               "first_name": "",
#               "sessionName": "Morning",
#               "admission_id": "01190001N",
#               "currentLevel": "NON-HND I",
#               "mobile_number": "0543418718",
#               "recipient_address": "0543418718"
#           },
#           {
#               "sex": "Male",
#               "email": "zee@gmail.com",
#               "balance": -960,
#               "program": "DBS STATISTICS",
#               "currency": "GHS",
#               "fee_type": 1,
#               "mobileNo": "0206358827",
#               "accountNo": "01190001N",
#               "full_name": "DADZIE DERRICK ",
#               "last_name": "",
#               "studentId": "01190001N",
#               "first_name": "",
#               "sessionName": "Morning",
#               "admission_id": "01190001N",
#               "currentLevel": "NON-HND I",
#               "mobile_number": "0543418718",
#               "recipient_address": "0543418718"
#           },
#           {
#               "sex": "Male",
#               "email": "zee@gmail.com",
#               "balance": -960,
#               "program": "DBS STATISTICS 000",
#               "currency": "GHS",
#               "fee_type": 1,
#               "mobileNo": "0206358827",
#               "accountNo": "01190001N",
#               "full_name": "DADZIE DERRICK 000",
#               "last_name": "",
#               "studentId": "01190001N",
#               "first_name": "",
#               "sessionName": "Morning",
#               "admission_id": "01190001N",
#               "currentLevel": "NON-HND I",
#               "mobile_number": "0543418718",
#               "recipient_address": "0543418718"
#           },
#           {
#               "sex": "Male",
#               "email": "jay@gmail.com",
#               "balance": -960,
#               "program": "DBS STATISTICS",
#               "currency": "GHS",
#               "fee_type": 1,
#               "mobileNo": "0206358827",
#               "accountNo": "01190001N",
#               "full_name": "DADZIE DERRICK ",
#               "last_name": "",
#               "studentId": "01190001N",
#               "first_name": "",
#               "sessionName": "Morning",
#               "admission_id": "01190001N",
#               "currentLevel": "NON-HND I",
#               "mobile_number": "0543418718",
#               "recipient_address": "0543418718"
#           },
#       ]
# customers = []
# for i in data:
#   # print(i["email"])
#   if customers == []:
#     customers.append(i)

#   if i["email"] in customers.values():
#     pass
#   else:
#     customers.append(i)

  

# # print(customers["email"])
# for j in customers:
#   print(j["email"])


# customers = []
# # data.sort()
# for indx, val in enumerate(data):
#     if val['email'] == data[indx+1]['email']:
#         del data[indx]
#         # customers.apend
#         print(data)

# uniqueValues = set(data.values())

# print(uniqueValues)

# l = []
# for i in data:
#   if i["email"] not in l:
#       l.append(i)
  # if l == []:
  #   l.append(i)

  # for h in l:
  #   if i["email"] != h["email"]:
  #     l.append(i)

# print(l)

data = [
    {
        "id": "38b79d2d-3337-4fa6-9e1d-2a0db3ad4d4d",
        "reference_id": "WP185583182676047",
        "amount": "0.10",
        "note": "test transaction",
        "service": 6,
        "status_code": "PENDING",
        "source_metadata": {
            "first_name": "Cornelius",
            "last_name": "Ashley-Osuzoka",
            "email": "user@gmail.com",
            "mobile_number": "676064566",
            "recipient_address": "Immueble CiSo, Boulevard de la liberte, Akwa Douala"
        },
        "device_info": {
            "Content-Length": "428",
            "Content-Type": "application/json",
            "Authorization": "Api-Key d1AgnEwt.Ifca3nGHb4ZfsNpA2DCZ3UyqN8QjzJsz",
            "User-Agent": "PostmanRuntime/7.29.0",
            "Accept": "*/*",
            "Postman-Token": "109b7d5b-f36e-44e5-8809-bc36235aa113",
            "Host": "127.0.0.1:8007",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        },
        "external_account_id": "0208556743",
        "status_message": "Transaction is pending",
        "created_at": "2022-08-03T14:54:46.378348Z"
    },
    {
        "id": "9de7375f-93ee-47b4-9588-f201ca43249b",
        "reference_id": "WP540534948824086",
        "amount": "0.10",
        "note": "test transaction voda",
        "service": 6,
        "status_code": "PENDING",
        "source_metadata": {
            "first_name": "Cornelius",
            "last_name": "Ashley-Osuzoka",
            "email": "user@gmail.com",
            "mobile_number": "676064566",
            "recipient_address": "Immueble CiSo, Boulevard de la liberte, Akwa Douala"
        },
        "device_info": {
            "Content-Length": "433",
            "Content-Type": "application/json",
            "Authorization": "Api-Key d1AgnEwt.Ifca3nGHb4ZfsNpA2DCZ3UyqN8QjzJsz",
            "User-Agent": "PostmanRuntime/7.29.0",
            "Accept": "*/*",
            "Postman-Token": "a5b88a02-070a-4525-9cce-c7c8aa0483d9",
            "Host": "127.0.0.1:8007",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        },
        "external_account_id": "0208556743",
        "status_message": "Transaction is pending",
        "created_at": "2022-07-28T02:16:09.505629Z"
    },
    {
        "id": "5e309e57-6b01-492e-9b34-7db858edf15c",
        "reference_id": "WP560618341540211",
        "amount": "0.10",
        "note": "test transaction",
        "service": 6,
        "status_code": "PENDING",
        "source_metadata": {
            "first_name": "Cornelius",
            "last_name": "Ashley-Osuzoka",
            "email": "user@gmail.com",
            "mobile_number": "676064566",
            "recipient_address": "Immueble CiSo, Boulevard de la liberte, Akwa Douala"
        },
        "device_info": {
            "Content-Length": "402",
            "Content-Type": "application/json",
            "Authorization": "Api-Key d1AgnEwt.Ifca3nGHb4ZfsNpA2DCZ3UyqN8QjzJsz",
            "User-Agent": "PostmanRuntime/7.29.0",
            "Accept": "*/*",
            "Postman-Token": "41b4a585-c274-4698-9a66-2f05282fbfdb",
            "Host": "127.0.0.1:8007",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        },
        "external_account_id": "0208556743",
        "status_message": "Transaction is pending",
        "created_at": "2022-07-27T10:14:00.324431Z"
    },
    {
        "id": "e32cbb40-8b29-4f63-9bb0-47d0ea65e3f1",
        "reference_id": "WP542999506574261",
        "amount": "0.10",
        "note": "test transaction",
        "service": 6,
        "status_code": "FAILED",
        "source_metadata": {
            "first_name": "Cornelius",
            "last_name": "Ashley-Osuzoka",
            "email": "user@gmail.com",
            "mobile_number": "676064566",
            "recipient_address": "Immueble CiSo, Boulevard de la liberte, Akwa Douala"
        },
        "device_info": {
            "Content-Length": "402",
            "Content-Type": "application/json",
            "Authorization": "Api-Key d1AgnEwt.Ifca3nGHb4ZfsNpA2DCZ3UyqN8QjzJsz",
            "User-Agent": "PostmanRuntime/7.29.0",
            "Accept": "*/*",
            "Postman-Token": "85bd9f61-afdf-4260-9d8c-278240999199",
            "Host": "127.0.0.1:8007",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        },
        "external_account_id": "0208556743",
        "status_message": "Transaction is pending",
        "created_at": "2022-07-27T10:12:47.928455Z"
    },
    {
        "id": "f7839329-56d9-4b54-99ce-52e281d202ca",
        "reference_id": "WP381776181478976",
        "amount": "0.10",
        "note": "test",
        "service": 2,
        "status_code": "SUCCESSFUL",
        "source_metadata": None,
        "device_info": None,
        "external_account_id": "0558230944",
        "status_message": "",
        "created_at": "2022-07-26T14:22:41.120781Z"
    },
]


# a = dict((v['external_account_id'],v) for v in data).values()

# print(a)

# del_key = 'source_metadata'
# for items in data:
#     if del_key in items:
#         del items[del_key]
# print(data)

# del_key = 'source_metadata'
# for items in data:
#     if del_key in items:
#         del items[del_key]
# print(data)

# for i in data:
#   if i.source_metadata == None:
#       i.surce_metadata = ""
#   if i.device_info == None:
#     i.device_info = ""

# a = dict((v['external_account_id'],v) for v in data).values()

# print(data.distinct())


# Please use this link to submit additional 
# information: https://grnh.se/r/4e1b0f7f5756a29b589d458aa64a11us.

# secret = "hhcjkdskja213nm,cne"

# msg = ""
# for char in secret:
#   msg += chr(ord(char) - 1)

#   print(msg)




# # Importing library
# import qrcode
 
# # Data to be encoded
# data = 'QR Code using make() function'
 
# # Encoding data using make() function
# img = qrcode.make(data)
 
# print(img)
# # Saving as an image file
# # img.save('MyQRCode1.png')




# from cryptography.fernet import Fernet
 
# # we will be encrypting the below string.
# message = "hello geeks"
 
# # generate a key for encryption and decryption
# # You can use fernet to generate
# # the key or use random key generator
# # here I'm using fernet to generate key
 
# key = Fernet.generate_key()
 
# # Instance the Fernet class with the key
 
# fernet = Fernet(key)
 
# # then use the Fernet class instance
# # to encrypt the string string must
# # be encoded to byte string before encryption
# encMessage = fernet.encrypt(message.encode())
 
# print("original string: ", message)
# print("encrypted string: ", encMessage)
 
# # decrypt the encrypted string with the
# # Fernet instance of the key,
# # that was used for encrypting the string
# # encoded byte string is returned by decrypt method,
# # so decode it to string with decode methods
# decMessage = fernet.decrypt(encMessage).decode()
 
# print("decrypted string: ", decMessage)




import rsa
 
# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)
 
# this is the string that we will be encrypting
message = "hello geeks"
 
# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),
                         publicKey)
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
print("decrypted string: ", decMessage)