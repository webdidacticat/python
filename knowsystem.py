from sys import platform

print(platform)
if platform == "linux" or platform == "linux2":
    # linux
    print("Linux")
elif platform == "darwin":
    # OS X
    print("MAC OS")
elif platform == "win32":
    # Windows...
    print("Windows")

#    System            platform value
#    AIX                   'aix'
#    Linux                'linux'
#    Windows              'win32'
#    Windows / Cygwin    'cygwin'
#    macOS               'darwin'
