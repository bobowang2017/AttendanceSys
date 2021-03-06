# -*- coding: utf-8 -*-
"""
Django settings for AttendanceSys project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1jaqc)^qqma0^wm=5*&w636ijspmoyh=3l=j74+fc&sqc$5f!f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'django.contrib.staticfiles',
    'apply_app',
    'user_app',
    'attendance_app',
    'common',
    'portal',
    'user_email',
    'middleware',
    'test_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AttendanceSys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '/portal/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AttendanceSys.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'attendance',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "portal/static"),
)

# 这个是默认设置，Django 默认会在 STATICFILES_DIRS中的文件夹 和 各app下的static文件夹中找文件
# 注意有先后顺序，找到了就不再继续找了
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)


# QQ邮箱的配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
# QQ邮箱的STMP服务器
EMAIL_HOST = 'smtp.qq.com'
# QQ邮箱的STMP端口号
EMAIL_PORT = 25
EMAIL_HOST_USER = '286803430'
# QQ邮箱授权码，要在QQ邮箱中进行设置
EMAIL_HOST_PASSWORD = 'vixyayhaxomabhfb'
# 默认发送者
DEFAULT_FROM_EMAIL = '286803430@qq.com'



# Github授权账户信息
# Client ID
# aef5d906236d4189a88c
# Client Secret
# 1c486bb65d968a9de4f08d49a526521f9ed1a792
# https://github.com/login/oauth/authorize?client_id=aef5d906236d4189a88c&scope=user


# django-oauth-toolkit
CLIENT_ID = 'eMyP228IZ6GzoInXDriznEEiPkWjpkmUzpCa24E2'
CLIENT_SECRET = 'mqJQ74fwuUFTZZ7gkLkAGAiQapG8GwIoStpfT0fiptzb0jvXOxQVvgIHaBlYi6rpwNhdXjNNd9TUEhnXAV1KPUt6Z4BeCfg1qJM9QUVfT4OFxEReYKAMMurICNvYzEEF'
REDIRECT_URL = '/callback'
AUTU_URL = 'o/authorize'
# http://localhost:8000/o/authorize?response_type=code&client_id=eMyP228IZ6GzoInXDriznEEiPkWjpkmUzpCa24E2&redirect_uri=http://localhost:8000