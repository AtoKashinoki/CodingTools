

from CodingTools.Config import read, write, ConfigManager

PATH = "./conf.cnf"


if __name__ == '__main__':
    config = read(PATH)
    print(config)
    write(PATH, config)
    config = ConfigManager(PATH)
    print(config)
    ...
