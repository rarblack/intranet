from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

import sys

from .views.methods.home.views import render_home
from .views.methods.welcome.views import render_welcome
from .views.methods.common.views import render_home_or_welcome
from .views.classes.dashboard.views import DashboardTemplateView

urlpatterns = []

#                                                                                                                SINGLES
urlpatterns += [
    path('', render_home_or_welcome),
    path('welcome/', render_welcome, name='welcome'),
    path('home/', render_home, name='home'),

    path('intranet/dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
]


#                                                                                                         3RD PARTY APPS

# ADMIN
urlpatterns += [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# CKEDITOR
urlpatterns += [
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


#
# # DEPARTMENTS
# urlpatterns += [
#     path('department', include(('Departments.urls', 'Departments'), namespace='department'))
# ]
#
# # DIRECTORY
# urlpatterns += [
#     path('directory', include(('Directory.urls', 'Directory'), namespace='directory'))
# ]
#
# # DOCUMENT LIBRARY
# urlpatterns += [
#     path('document-library', include(('DocumentLibrary.urls', 'DocumentLibrary'), namespace='document_library'))
# ]

# # EVENTS
# urlpatterns += [
#     path('//events', include(('Events.urls', 'events'), namespace='events'))
# ]

# # GUEST-CONTROL
# urlpatterns += [
#     path('guest-control', include(('GuestControl.urls.urls', 'GuestControl'), namespace="guest_control")),
# ]
#
# # HELP DESK
# urlpatterns += [
#     path('help-desk', include(('HelpDesk.urls', 'HelpDesk'), namespace='help_desk')),
# ]


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
    path('intranet/news/', include(('News.urls.urls', 'News'), namespace='news')),
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
# urlpatterns += [
#     path('self-service/transportation', include(('Transportation.urls', 'Transportation'), namespace='transportation')),
# ]

# WAREHOUSE
# urlpatterns += [
#     path('self-service/warehouse', include(('Warehouse.urls', 'Warehouse'), namespace='warehouse')),
# ]


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
