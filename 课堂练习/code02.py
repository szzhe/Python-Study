# encoding=utf-8


users = []

while True:
    str = input("请输入要操作的功能名称(find/list/add/delete/update/exit): ")

    if str == "add":
        print("请完善下述信息项")
        name = input("请输入用户名：")
        age = input("请输入年龄：")
        mobile = input("请输入联系方式：")

        user_tuple = (name,age,mobile)

        is_exists = False

        for user in users:
            if user[0] == name:
                print("添加用户失败，失败原因：用户名已存在")
                is_exists = True
                break
            
        if not is_exists:
            users.append(user_tuple)
            print("添加用户成功")

    elif str == "delete":
        str_name1 = input("请输入要删除的用户名：")
        if str_name1 in list_str:
            pass

    elif str == "exit":
        print("程序将退出，感谢使用")
        break
