API that allows any user to upload an image in PNG or JPG format. This is my first project in Django Rest Framework, which took me all week to do.

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


UPLOAD IMAGE (http://127.0.0.1:8000/uploadimage/images/upload/)

example:
{
"username": "premium",
"password": "premium_password",
"image": "https://media.wired.com/photos/636eb5510ae5a121565fd729/4:3/w_1983,h_1487,c_limit/WI110122_FF_ForeverDogs_2400x1350_crop.jpg"
}