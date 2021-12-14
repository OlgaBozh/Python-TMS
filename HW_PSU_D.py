import json
import psutil


def decor(func):

    def get_cpu():
        cpu_info = func()
        json_cpu = json.dumps(cpu_info, separators=(" *** ", " = "))
        print(json_cpu)

        return json_cpu

    return get_cpu


def get_cpu():

    result = {
        "time_cpu": psutil.cpu_times(),
        "pers_cpu": psutil.cpu_percent(),
        "st_cpu": psutil.cpu_stats(),

    }
    return result

@decor
def show():
    cpu_info = get_cpu()

    return cpu_info


show()