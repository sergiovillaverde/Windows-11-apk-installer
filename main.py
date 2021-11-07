import os, sys

os.chdir(r'C:\Users\sergi\Documents\Android\ADB\platform-tools')
os.system('cmd /c "adb connect 127.0.0.1:58526"')

for app in sys.argv[1:]:
    os.system('cmd /c "adb install '+ app)