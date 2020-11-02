from model.sqlmodel import ReadAll
from controller.pandacontroller import panda_connect
from model.sqlmodel import ReadAll2


if __name__ == "__main__":
    ReadAll()
    panda_connect()
    ReadAll2()

