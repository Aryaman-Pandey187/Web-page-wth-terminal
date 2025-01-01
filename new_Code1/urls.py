"""
URL configuration for django_prakirn_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



from django.urls import path
from .views import login_view
from .views import source_info_page
from .views import target_env_page
from .views import target_env_login
from .views import target_info_page
from .views import details_verification_page_with_logging
# from .views import run_function
from .views import fetch_logs
from .views import  check_tasks_complete
from .views import last_page

urlpatterns = [
    path('', login_view, name='login'),                                         # prod-login-details-page
    path('source_info/', source_info_page, name='source_info_page'),            # prod database and table name - 
    path('target_env_page/', target_env_page, name='target_env_page'),          # gets dev/sit/oat ?? page
    path('target_env_login/', target_env_login, name='target_env_login'),       # target env login details
    path('target_info_page/', target_info_page, name='target_info_page'),       # target db and table details
    path('details_verification_page_with_logging/', details_verification_page_with_logging, name='details_verification_page_with_logging'),
    # path('run-function/', run_function, name='run_function'),
    path('fetch-logs/', fetch_logs, name='fetch_logs'),
    path('check-tasks-complete/', check_tasks_complete, name='check_tasks_complete'),
    path('last_page/', last_page, name='last_page')
]   
