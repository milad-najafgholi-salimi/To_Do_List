def user_choice():
        try:
            usr_select = int(input("Select: "))
            if usr_select in range(1,8):
                match usr_select:
                      case 1:
                            pass
                      case 2:
                            pass
                      case 3:
                            pass
                      case 4:
                            pass
                      case 5:
                            pass
                      case 6:
                            pass
                      case 7:
                            pass
            else:
                print("Invalid value\n")
                return False # in 'main.py' module, the while loop will break.
        except ValueError:
                print("Invalid value\n")

# کل این بخش کد باید حذف شود. زیرا دستور داریم که این کار را با کلاس Task_Manager انجام دهیم.
