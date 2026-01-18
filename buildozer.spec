[app]

title = AI App
package.name = aiapp
package.domain = org.israr

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = kivy==2.3.0,cython==0.29.36


orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
