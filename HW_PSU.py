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
    cpu_template = "time_cpu : {time_cpu} | pers_cpu : {pers_cpu} | st_cpu : {st_cpu}"
    print(cpu_template.format(**kwargs['cpu']))
    info_template = "battery: {} | users: {} | memory: {}"
    print(info_template.format(kwargs["info"]["battery"], kwargs["info"]["users"], kwargs["info"]["memory"]))


def run():
    cpu = get_cpu()
    info = get_info()
    show(cpu=cpu, info=info)


if __name__ == "__main__":
    run()
