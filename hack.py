###########################
#                         #
#         SUDO            #
#                         #
###########################


import sys
import os
import time
from random import randint
from art import *
import subprocess

def create_rickroll_directory(name, url, filename):
    rickroll_dir = os.path.join(os.getcwd(), 'rickroll')
    if not os.path.exists(rickroll_dir):
        os.makedirs(rickroll_dir)

    target_dir = os.path.join(rickroll_dir, name)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    bat_file_path = os.path.join(target_dir, f"{filename}")
    with open(bat_file_path, 'w') as bat_file:
        bat_file.write('@echo off\n')
        bat_file.write(f'start {url}\n')
        bat_file.write('exit\n')

    return bat_file_path




print("")
print(text2art('''SUDO HACK''', font="small"))
print("Based on BegulaLinux Kernel")
time.sleep(2.5)
print(" ")

command = ""

while True:
    command = input("$ ")
    command_with_opt = command[5::]
    command = command_with_opt[:4]

    if command.startswith("hack"):
        name = command_with_opt[5::]
        print("📈 Processing . . .")
        time.sleep(1.5)
        seed = randint(1, 99999999)
        print(f"📝 Seed of session: {seed}")
        print(f"🟢 Status: success, {name} has been hacked!")
    elif command_with_opt.startswith("rickroll") and not command_with_opt.endswith("begula") and not command_with_opt.endswith("beluga") and not command_with_opt.endswith("hecker") and not command_with_opt.endswith("pablo"):
        name = input(">>> Enter a name for rickroll: ")
        print("📈 Processing . . .")
        time.sleep(1.5)
        seed = randint(1, 99999999)
        create_rickroll_directory(name, "https://clck.ru/39bcmq", "rickroll.bat")
        print(f"📝 Seed of session: {seed}")
        print(f"🟢 Status: success, {name} has been rickrolled!")
    elif command_with_opt.startswith("meowroll") and not command_with_opt.endswith("begula") and not command_with_opt.endswith("beluga") and not command_with_opt.endswith("hecker") and not command_with_opt.endswith("pablo"):
        name = input(">>> Enter a name for meowroll: ")
        print("📈 Processing . . .")
        time.sleep(1.5)
        seed = randint(1, 99999999)
        create_rickroll_directory(name, "https://clck.ru/39me7d", "meowroll.bat")
        print(f"📝 Seed of session: {seed}")
        print(f"🟢 Status: success, {name} has been meowrolled!")
    elif command_with_opt.startswith("off discord"):
        print("📈 Processing . . .")
        time.sleep(1.5)
        seed = randint(1, 99999999)
        subprocess.run(["start", "https://clck.ru/39meLE"], shell=True)
        print(f"📝 Seed of session: {seed}")
        print(f"🟢 Status: success, discord has been offed in 1 second!")
    elif command_with_opt.startswith("github"):
        print("📈 Processing . . .")
        time.sleep(1.5)
        seed = randint(1, 99999999)
        subprocess.run(["start", "https://clck.ru/39mqSi"], shell=True)
        print(f"📝 Seed of session: {seed}")
        print(f"🟢 Status: success, we redirected to our GitHub!")
    elif command_with_opt.startswith("shutdown"):
        print("📈 Processing . . .")
        time.sleep(1.5)
        seed = randint(1, 99999999)
        subprocess.run(["shutdown", "-s"], shell=True)
        print(f"📝 Seed of session: {seed}")
        print(f"🟢 Status: success, your microwave turns off!")
    elif command_with_opt.startswith("quit") or command_with_opt.startswith("exit"):
        exit()

    else:
        print("👎 No command accsess or command not found!")