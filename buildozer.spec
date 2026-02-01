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

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
