# encoding=utf-8


user = []
user_list = []

while True:
    str = input("请输入要操作的功能名称(find/list/add/delete/update/exit): ")

    if str == "add":
        print("请完善下述信息项")
        str_name = input("请输入用户名：")
        str_age = input("请输入年龄：")
        str_mobile = input("请输入联系方式：")

        user_tuple = (str_name,str_age,str_mobile)
        user.extend(user_tuple)
        print(user)

    if str == "delete":
        str_name1 = input("请输入要删除的用户名：")
        if str_name1 in list_str:
            pass

    if str == "exit":
    	break
