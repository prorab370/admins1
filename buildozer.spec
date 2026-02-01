[app]
title = QuizApp
package.name = quizapp
package.domain = org.quiz
version = 0.1

source.dir = .
source.include_exts = py

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.ndk = 25b

# ЖЁСТКО указываем SDK / NDK, чтобы buildozer
# НЕ СКАЧИВАЛ свой SDK с build-tools 36.x
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
