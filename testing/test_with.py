from time import sleep

import yaml

if __name__ == '__main__':
    with open("./datas/calc2.yaml") as f:
        sleep(2)
        print("-------0.5秒----------")
        datas = yaml.safe_load(f)
        datas1 = datas["add"]
        add_datas_True = datas1["datas_True"]
        print(f"add_datas_True :{add_datas_True}")
        add_datas_True_1=add_datas_True[0]
        a=add_datas_True[0][0]
        print(f"a=={a}")





