import os

ACTIVE_COLOR = (24 / 255, 133 / 255, 215 / 255, 1)
SE_COLOR = (24 / 255, 133 / 255, 215 / 255, .5)
BGCOLOR = (28 / 255, 36 / 255, 49 / 255, 1)
TEXT_COLOR = [1, 1, 1, 1]
ASSEST_PATH = os.path.join(os.getcwd(), "assest")
FONT_PATH = os.path.join(ASSEST_PATH, "SourceSansPro-Bold.ttf")
BACKGROUND_IMAGE = os.path.join(ASSEST_PATH, "background.png")
FONT_PATH_NORMAL = os.path.join(ASSEST_PATH, "SourceSansPro-Regular.ttf")
LOGIN_DB_PATH = os.path.join("data", "login.db")
IS_LOGIN = "login" if os.path.exists(LOGIN_DB_PATH) else "RegisterScreen"
ICON = os.path.join(ASSEST_PATH, "icon.png")


def getuser():
    if os.path.exists(LOGIN_DB_PATH):
        with open(LOGIN_DB_PATH, "r") as login_file:
            user_name = login_file.readline()
        login_file.close()
        return user_name
    else:
        return False


if IS_LOGIN:
    WIDTH = 370
    HEIGHT = 180
if not IS_LOGIN:
    WIDTH = 413
    HEIGHT = 230
A_HEIGHT = 230
A_WIDTH = 550
