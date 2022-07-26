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
class Person:
  name = "John"
  age = 36
  country = "Norway"


x = getattr(Person, "no", "hello")
print(x)