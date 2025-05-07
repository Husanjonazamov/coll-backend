from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Foydalanuvchilar"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "icon": "group",
                "link": reverse_lazy("admin:bot_usermodel_changelist"),
            },
        ],
    },
    {
        "title": _("Bot"),
        "separator": True,  # Top border
        "items": [
            {   
                "title": _("O'qituvchilar"),
                "icon": "school",
                "link": reverse_lazy("admin:bot_teachermodel_changelist"),
            },
             {
                "title": _("Kategoryalari"),
                "icon": "category",
                "link": reverse_lazy("admin:bot_categorymodel_changelist"),
            },
        ],
    },
]
