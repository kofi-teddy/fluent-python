# data = "12 / 24"

# card_data = data.split("/")
# card_expiration_month = card_data[0]
# card_expiration_day = card_data[1]


# def somecal(num1, num2, num3=0.00):
#     total=num1 + num2 + num3
#     print(total)
# somecal(2, 3)


# full_name = "Teddy Mawuli Agudogo"

# data = full_name.split(" ", 1,)
# print(data)
# if len(data) <= 2:
#     first_name = data[0]
#     last_name = data[1]
# else:
#     # first_name = data[0]
#     # last_name = data[1]
#     # other_names = 
#     pass

# data = {
#     "correlationId": "f7fc6c4ddfzhoo8888",
#     "merchant": "93690150",
#     "result": "SUCCESS",
#     "session": {
#         "aes256Key": "GF8d+giDk98YKgL3TKCQhEJGQ/3qEOEOOtGg7H4GUWg=",
#         "authenticationLimit": 5,
#         "id": "SESSION0002832084359E45047557E7",
#         "updateStatus": "NO_UPDATE",
#         "version": "ff1a112101"
#     }
# }

# print(data["result"])


# expiry = "01 / 39"
# card_data = expiry.replace(" ", "").split("/")

# print(card_data)

# redirectHtml = "<div id=\"redirectTo3ds1AcsSimple\" xmlns=\"http://www.w3.org/1999/html\"> <iframe id=\"redirectTo3ds1Frame\" name=\"redirectTo3ds1Frame\" height=\"100%\" width=\"100%\" > </iframe> <form id =\"redirectTo3ds1Form\" method=\"POST\" action=\"https://mtf.gateway.mastercard.com/acs/VisaACS/5025d258-aea0-4577-88e4-69f22437d66b\" target=\"redirectTo3ds1Frame\"> <input type=\"hidden\" name=\"PaReq\" value=\"eAFVkd1ugkAQhe9NfAfCveyygC5mWKPSqok21p/G9I7iFkkElB/FXvad+kJ9ku4i1vaG7Dmze5j5BnpltFdOPM3CJHZUXcOqwmM/2YZx4Kjr1WOLqj3WbMBql3LuLrlfpJzBjGeZF3Al3DoqsWjbtG1dZTDvL/iRQR3HRJpGAN2keJX6Oy/OGXj+cTB5Yialtm0BqiVEPJ24zDba9gZj3cKG/LSklgdA1zrEXsTZcNBXBlNlOplNVg8uoMoEPyniPL0wQimgm4Ai3bNdnh+yLkLn81k7i+nCg3fR/CQCJKuA7s3NC9lmJsYswy17d4N9MRpam/K0NoOX8OPNXLxuaELJswNI3oCtl3NGMCE6wbaiG12DdkkHUOWDF8me2Gi8VL4/v7Cmi0FqDw7yV/3rBen/1SBQp2IXFwlEDHNTwMtDEnMRKdj+ngHd2x6OJWE/FyxNC9OOJWF2TB3rtmRdFWRKKEAZAm0VIwUg+RTVaxRIqi0L59/2m40flXa1lw==\" /> <input type=\"hidden\" name=\"TermUrl\" value=\"https://mtf.gateway.mastercard.com/callbackInterface/gateway/f1edd78e51477ad86e3b0d4d9a405fdf3651c5bc6aaa7fdbbc5195244fa2a61d\" /> <input type=\"hidden\" name=\"MD\" value=\"\" /> </form> <script id=\"authenticate-payer-script\"> var e=document.getElementById(\"redirectTo3ds1Form\"); if (e) { e.submit(); if (e.parentNode !== null) { e.parentNode.removeChild(e); } } </script> </div>"

# print(redirectHtml.replace('\"', '"'))


# from base64 import b64decode

# from Cryptodome.Cipher import AES

# encryptedData_ciphertext = b64decode("u4KOYzoqM47LZ6rzRDg9+owGTcL77gB7zQHn7aeQfgGDU/HGenAXyfK1fnWF/r/tls8WS0V5x3oPWpNQgKyLm/CyYeqjs433Wi9vX5GabOyeXtrTDAGha/VL6l1g0+GfyWdR3py4b5IBd14SvthYGuCyR8jdNhwU//nuIDTOPH8E8bIfbioO/n3m02S3EdEpv/xK9MQVnOsdTuk2uca2GMlfi3SWG0d6siOx7iGTbY86lajU/7J4v+HZcL1QqxmnkQUXijZaSgZyLN2C+H41tOmAbq7mf2A2gRwU6vovnDPq49IZIlyH5J93VWzp3E7HBa7VHejpZz0mtuNOSn7JWoVcdk2JDU+E2eT8bZVUIHRMmKSeKXg1a9a9xy2U7iMBab6TRkzdxnc820NHWT+dqYsUZKZdBB2XRBPamh87tWKJ2opzisPVaTkrfKNlR93LY3J738UpLEEcsUR+SrML5P9NaCuuNSPEjG+ljS3RixuS86WC6AOflwqWCIebRSJuJFn18wFyhTIM2UurnzooWDA2k8CyIpo9zJoaBNhL4rt3tXveDCJKLn/R5ot0VcXUcnoCGd1oZT19S1ocZpEErRFUHau9cyurTg==")

# encryptedData_nonce = b64decode("mhslvFRE+HqAAA6V")
# encryptedData_tag = b64decode("ZMcxCsEksMo2jNvDaT++DA==")
# aes256key =  b64decode("wwPd2eQbm6/bVSWDgufb/P5PQ56qOh1pDMTlLhK5XEo=")

# # from Crypto.Cipher import AES


# # rev_obj = AES.new(aes256key, encryptedData_nonce, encryptedData_tag)
# # decrypted_text = rev_obj.decrypt(encryptedData_ciphertext)
# # print('The decrypted text', decrypted_text.decode('utf-8'))

#  # create the cipher config
# cipher = AES.new(aes256key, AES.MODE_GCM, nonce=encryptedData_nonce)

# # decrypt the cipher text
# decrypted = cipher.decrypt_and_verify(encryptedData_ciphertext, encryptedData_tag)

# print(decrypted)


# data = {
#     "authentication": {
#         "3ds": {
#             "acsEci": "05",
#             "authenticationToken": "gIGCg4SFhoeIiYqLjI2Oj5CRkpM=",
#             "transactionId": "dTHoHt8gKX1/MxRGWi86Yrr+k8k="
#         },
#         "3ds1": {
#             "paResStatus": "Y",
#             "veResEnrolled": "Y"
#         },
#         "acceptVersions": "3DS1,3DS2",
#         "amount": 0.10,
#         "channel": "PAYER_BROWSER",
#         "payerInteraction": "REQUIRED",
#         "purpose": "PAYMENT_TRANSACTION",
#         "redirect": {
#             "domainName": "mtf.gateway.mastercard.com"
#         },
#         "time": "2022-12-14T10:21:49.628Z",
#         "version": "3DS1"
#     }
# }

# print(data["authentication"]["3ds"]["transactionId"])



################################################################
################################################################
# check if a key exist in a json block
kyc  = {
        "is_developer": "True",
        "postal_address": "P.O. Box 2022",
        "bank_name": "Stanbic Bank",
        "bank_account": "3143210789732000",
        "bank_branch": "Tema",
        "business_TIN": "wt2132131",
        "NID_director_1": "12132123412432",
        "NID_director_2": "12131314222626",
        "gps": "GT1213121",
        "business_name": "Bakeries 2020",
        "business_type": "Sole Prorietorship",
        "business_address": "business_address",
        "business_email": "tayebo4867@tebyy.com"
    }


if "is_developer" in kyc and "postal_address" in kyc and "bank_name" in kyc and "bank_account" in kyc and "bank_branch" in kyc and "business_TIN" and "NID_director_1" in kyc and "NID_director_2" in kyc and "gps" in kyc and "business_name" in kyc and "business_type" in kyc and "business_address" in kyc and "business_email" in kyc:
    print("yes")
else:
    print("no")