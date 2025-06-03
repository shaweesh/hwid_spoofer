import subprocess

def read_registry_value(path, name):
    """يقرأ قيمة من الـ Registry"""
    try:
        output = subprocess.check_output(f'reg query "{path}" /v {name}', shell=True)
        lines = output.decode().splitlines()
        for line in lines:
            if name in line:
                return line.strip().split()[-1]
        return None
    except subprocess.CalledProcessError:
        return None

def write_registry_value(path, name, value):
    """يكتب قيمة إلى الـ Registry"""
    try:
        subprocess.run(f'reg add "{path}" /v {name} /d {value} /f', shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def delete_registry_value(path, name):
    """يحذف قيمة من الـ Registry"""
    try:
        subprocess.run(f'reg delete "{path}" /v {name} /f', shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
