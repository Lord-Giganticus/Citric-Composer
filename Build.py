import subprocess
from os import path
import os
import shutil
import sys

home_dir = path.dirname(__file__)

if os.getcwd() is not home_dir:
    os.chdir(home_dir)

commands = []


os.chdir("Citric Composer")
subprocess.call("nuget restore",shell=True)
for file in os.listdir(os.getcwd()):
    if file.endswith(".sln") is True:
        commands.append(f'msbuild "{path.abspath(file)}" -p:Configuration=Release')

os.chdir(home_dir)


os.chdir("Koopa Harmony")
subprocess.call("nuget restore",shell=True)
for file in os.listdir(os.getcwd()):
    if file.endswith(".sln") is True:
        commands.append(f'msbuild "{path.abspath(file)}" -p:Configuration=Release')

os.chdir(home_dir)

os.chdir("Retsuko Sound Tool")
subprocess.call("nuget restore",shell=True)
for file in os.listdir(os.getcwd()):
    if file.endswith(".sln") is True:
        commands.append(f'msbuild "{path.abspath(file)}" -p:Configuration=Release')


os.chdir(home_dir)

for command in commands:
    subprocess.call(command, shell=True)

os.chdir("Citric Composer\\Citric Composer\\bin\\Release")

subprocess.call('7z a "Citric Composer.zip" *.* -r', shell=True)

shutil.move("Citric Composer.zip", f"{home_dir}\\Citric Composer.zip")

os.chdir(f"{home_dir}\\Koopa Harmony\\Koopa Harmony\\bin\\Release")

subprocess.call('7z a "Koopa Harmony.zip" *.* -r', shell=True)

shutil.move("Koopa Harmony.zip", f"{home_dir}\\Koopa Harmony.zip")

os.chdir(f"{home_dir}\\Retsuko Sound Tool\\Retsuko Sound Tool\\bin\\Release")

subprocess.call('7z a "Retsuko Sound Tool.zip" *.* -r', shell=True)

shutil.move("Retsuko Sound Tool.zip", f"{home_dir}\\Retsuko Sound Tool.zip")

os.chdir(home_dir)

sys.exit(0)