### Code to python >= 3.6
### Code to know module is or not found in PC

try:
    import datetime
except ModuleNotFoundError as err:
    ### Module Not Exist
    print(err)
    print("Install Module: ")
    exit(1)
### Module Exist
print("Module Found!!!")

try:
    import mymodule
except ModuleNotFoundError as err:
    ### Module Not Exist
    print(err)
    print("Install Module: ")
    exit(1)
### Module Exist
print("Module Found!!!")
