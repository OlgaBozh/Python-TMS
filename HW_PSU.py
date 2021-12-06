import psutil


def get_cpu():
    result = {}
    result.update(
        time_cpu=psutil.cpu_times(),
        pers_cpu=psutil.cpu_percent(),
        st_cpu=psutil.cpu_stats()
    )
    return result


def get_info():
    result = {
        "battery": psutil.sensors_battery(),
        "users": psutil.users(),
        "memory": psutil.virtual_memory()
    }
    return result


def show(**kwargs):
    print(kwargs["cpu"])
    print(kwargs["info"])


def run():
    cpu = get_cpu()
    info = get_info()
    show(cpu=cpu, info=info)


if __name__ == "__main__":
    run()
