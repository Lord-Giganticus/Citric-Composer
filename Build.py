import subprocess
from os import path
import os

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