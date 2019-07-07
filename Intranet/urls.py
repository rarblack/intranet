"""SocarProject URL Configuration

The `urlpatterns` list routes URLs to views. For more view please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import sys

# ADMIN
urlpatterns = [
    path('admin', admin.site.urls),
]

urlpatterns += [
    path('accounts', include('django.contrib.auth.urls')),
]

# DASHBOARD
urlpatterns += [
    re_path(r'^$|home', include(('Dashboard.urls', 'Dashboard'), namespace='dashboard'))
]

# DASHBOARD
urlpatterns += [
    path('dashboard', include(('Dashboard.urls', 'Dashboard'), namespace='dashboard'))
]

# DEPARTMENTS
urlpatterns += [
    path('department', include(('Departments.urls', 'Departments'), namespace='department'))
]

# DIRECTORY
urlpatterns += [
    path('directory', include(('Directory.urls', 'Directory'), namespace='directory'))
]

# DOCUMENT LIBRARY
urlpatterns += [
    path('document-library', include(('DocumentLibrary.urls', 'DocumentLibrary'), namespace='doclib'))
]

# # EVENTS
# urlpatterns += [
#     path('//events', include(('Events.urls', 'events'), namespace='events'))
# ]

# GUEST-CONTROL
urlpatterns += [
    path('guest-control', include(('GuestControl.urls', 'GuestControl'), namespace="guestcontrol")),
]

# HELP DESK
urlpatterns += [
    path('help-desk', include(('HelpDesk.urls', 'HelpDesk'), namespace='helpdesk')),
]

# HUMAN-RESOURCES
urlpatterns += [
    path('human-resources', include('HumanResources.urls')),
]

# LUNCHROOM
# urlpatterns += [
#     path('self-service/lunchroom', include(('Lunchroom.urls', 'Lunchroom'), namespace='lunchroom'))
# ]

# MANAGEMENT
# urlpatterns += [
#     path('management', include(('Management.urls', 'Management'), namespace='management'))
# ]

# NEWS
urlpatterns += [
    path('news', include(('News.urls', 'News'), namespace='news')),
]

# PEOPLE ON BOARD
# urlpatterns += [
#     path('people-on-board', include('PeopleOnBoard.urls')),
# ]

# SETTINGS
# urlpatterns += [
#     path('self-service/settings', include(('Settings.urls', 'Settings'), namespace='settings'))
# ]

# TRANSPORTATION
urlpatterns += [
    path('self-service/transportation', include(('Transportation.urls', 'Transportation'), namespace='transportation')),
]

# WAREHOUSE
urlpatterns += [
    path('self-service/warehouse', include(('Warehouse.urls', 'Warehouse'), namespace='warehouse')),
]


# EXTRA SETTINGS
DEV_SERVER = (len(sys.argv) > 1 and sys.argv[1] == 'runserver')

if DEV_SERVER:
    admin.site.site_url = 'http://localhost:8000/dashboard'
    admin.site.site_header = 'Socar-AQS Intranet ADMIN DEVELOPMENT'
    admin.site.site_title = 'Socar-AQS Intranet DEVELOPMENT'
    admin.site.index_title = 'Site administration DEVELOPMENT'
    admin.empty_value_display = '**Empty**'
else:
    admin.site.site_url = 'http://inet.socar-aqs.local/dashboard'
    admin.site.site_header = 'Socar-AQS Intranet ADMIN'
    admin.site.site_title = 'Socar-AQS Intranet'
    admin.site.index_title = 'Site administration'
    admin.empty_value_display = '**Empty**'

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
