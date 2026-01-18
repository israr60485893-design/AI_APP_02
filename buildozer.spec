[app]
title = AI_APP_02
package.name = aiapp
package.domain = org.israr
version = 1.0


source.dir = .
source.include_exts = py,png,jpg,kv

entrypoint = main.py

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.build_tools_version = 33.0.2

android.permissions = INTERNET

arch = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
