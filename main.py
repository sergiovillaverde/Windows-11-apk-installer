import os, sys

os.chdir(r'Your ADB drivers')
os.system('cmd /c "adb connect 127.0.0.1:58526"')

for app in sys.argv[1:]:
    os.system('cmd /c "adb install '+ app)
