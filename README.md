API that allows any user to upload an image in PNG or JPG format.

LOGIN (http://127.0.0.1:8000/accounts/login/)

{
"username": "basic",
"password": "basic_password"
}

{
"username": "premium",
"password": "premium_password"
}

{
"username": "enterprise",
"password": "enterprise_password"
}


UPLOAD IMAGE

example:
curl.exe -F "username=premium" -F "password=premium_password" -F "@path" http://127.0.0.1:8000/uploadimage/images/upload/