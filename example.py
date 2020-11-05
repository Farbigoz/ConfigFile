from config import ConfigFile, ConfigElement

class AppConfigMap(ConfigFile):
    UserName = ConfigElement            #Default type = str
    UserAge = ConfigElement(type=int)   #Set var type

    Version = ConfigElement(default="1.0")              #Auto detect var type
    Creators = ConfigElement(default=["Popa", "Ivan"])
    Permissions = ConfigElement(default=999)
    Links = ConfigElement(default={"Hello": "World"})

    HomePath = ConfigElement(name="HOME_PATH", default="C:\\")  #'HOME_PATH[str] = C:\;' in config file
    
    Display = ConfigElement(name="DISPLAY", default="AsusBLA-BLA23")    #'DISPLAY[str] = ...;'
    DisplayInt = ConfigElement(name="DISPLAY", default=1)               #'DISPLAY[int] = ...;'

    FirstStart = ConfigElement(default=True)

AppConfig = AppConfigMap("app.cfg")

input("Look at app.cfg and press Enter")

print(AppConfig.UserName)       #None
print(AppConfig.UserAge)        #None
print(AppConfig.Permissions)    #999
print(AppConfig.HomePath)       #'C:\'
print(AppConfig.FirstStart)     #True

AppConfig.UserName = "Hatsune Miku"
AppConfig.Permissions = 131
AppConfig.HomePath = "D:\\"
AppConfig.FirstStart = False

print(AppConfig.UserName)       #'Hatsune Miku'
print(AppConfig.Permissions)    #131
print(AppConfig.HomePath)       #'D:\'
print(AppConfig.FirstStart)     #False

AppConfig.HomePath = 0          #TypeError (HomePath type = str)