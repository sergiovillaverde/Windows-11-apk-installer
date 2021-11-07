# Windows 11 APK installer for Windows Subsystem for Android
_An easiest way to install APKs on Windows 11, just **drag** the .apk and **drop** it on this .py_

## Starting 🚀

_The following instructions will allow you to use this script on your machine._

### Prerequisites 📋
_You will need the following tools._

+ [ADB Drivers](https://developer.android.com/studio/releases/platform-tools)
+ [Windows Subsystem for Android](https://www.xda-developers.com/how-to-run-android-apps-on-any-windows-11-pc/)

_Also, you **must** change the path of the ADB drivers inside the quotes, **don't delete the r**._
```
os.chdir(r'C:\Users\sergi\Documents\Android\ADB\platform-tools')
```

## Installing APKs 🔧
_Open the **Windows Subsystem for Android** and launch the files options as shown on **Picture 1** or set the Subsystem resources to Continuous, as shown on **Picture 2**_
### Launch the files
![Picture 1](https://user-images.githubusercontent.com/62207304/140657696-53164e02-f0a3-4754-99a9-cbae8b751276.png)
### Continuous resources
![Picture 2](https://user-images.githubusercontent.com/62207304/140657709-32102df4-cc1f-41c7-b73c-1772924e422c.png)
### Drag and drop the .apk
_For installing the **.apk** just drag it and drop it on the **main.py**_
