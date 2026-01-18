[buildozer]
log_level = 2
warn_on_root = 1


[app]
title = AI App
package.name = aiapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1


[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.build_tools_version = 33.0.2

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

android.allow_backup = True


[app:android:debug]
android.debuggable = True
