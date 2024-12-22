"""
ASGI config for R-E-S-S project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# تحديد ملف الاعدادات الخاص بالمشروع كاعدادات افتراضية
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R-E-S-S.settings')

application = get_asgi_application()
