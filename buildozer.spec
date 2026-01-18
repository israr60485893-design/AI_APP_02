[app]
source.dir = .

title = AI Chat App
package.name = aichat
package.domain = org.example

source.include_exts = py,png,jpg,kv,json

version = 0.1

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b

android.permissions = INTERNET

android.archs = arm64-v8a,armeabi-v7a
