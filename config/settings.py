"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-a)km611c)h%xhb*(or6(ebam366-myllvk7e2jbwc*4pqp1$g'

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
    
    "whitenoise.runserver_nostatic",
    
    'django.contrib.staticfiles',
    
    # Our apps
    "blog",
    "accounts",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    "whitenoise.middleware.WhiteNoiseMiddleware",
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath("templates"))],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# Previously, we configured our static files by creating a dedicated static folder, pointing
# STATICFILES_DIRS to it in our config/settings.py file, and adding { % load static % } to our
# base.html template. But since Django won’t serve static files in production, we need a few extra
# steps.
# The first change is to use Django’s collectstatic command which compiles all static files
# throughout the project into a singe directory suitable for deployment. Second, we must set the
# STATIC_ROOT114 configuration, which is the absolute location of these collected files, to a folder
# called staticfiles. And third, we need to set STATICFILES_STORAGE115, which is the file storage
# engine used by collectstatic.

# OLD
# STATIC_URL = '/static/'

# NEW, Deployable
STATIC_URL = '/static/'
# Adding a configuration to look for static folder beyond app/static default like we do with templates. We want it to look into our root folder.
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
# After adding the above, we run 'python manage.py collectstatic'
# The above command creates a new staticfiles folder which contains our original css file and the files for the admin stuff. The above code must be run everytime (compile) before each new deployment.
# We'll use a package called WhiteNoise to server the static files in production.
# pipenv install whitenoise

# With whitenoise we need to make 3 updates
# • add whitenoise to the INSTALLED_APPS above the built-in staticfiles app
# See top of file
# • under MIDDLEWARE add a new line for WhiteNoiseMiddleware
# See top of file
# • change STATICFILES_STORAGE to use WhiteNoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# After the above 3 changes, run collectstatic again as our STATICFILES_STORAGE was changed

# TO SUMMARIZE
# Static files are quite confusing to newcomers, so as a brief recap here are the steps we’ve
# executed so far in our Blog site. First, for local development back in Chapter 5, we created top-level static folder and updated STATICFILES_DIRS to point to it. In this chapter, we
# added configurations for STATIC_ROOT and STATICFILES_STORAGE before running collectstatic
# for the first time, which compiled all our static files across the entire project into a single
# staticfiles folder. Finally, we installed whitenoise, updated INSTALLED_APPS, MIDDLEWARE, and
# STATICFILES_STORAGE, and re-ran collectstatic.

# To redirect users after a successful login
# The below will redirect the user to our 'home' template.
LOGIN_REDIRECT_URL = "home"
# Redirect link for logging out
LOGOUT_REDIRECT_URL = "home"
