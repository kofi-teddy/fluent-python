# Using python not operator



is_superuser = True
is_staff = False
is_admin = True


if not is_superuser and not is_staff and not is_admin:
    print('Account created successfully!')
else:
    print('Cannot create account. Please try again later')
