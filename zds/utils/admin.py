from django.contrib import admin

from zds.utils.models import Alert, Licence, Category, SubCategory, \
    CategorySubCategory, Tag, HelpWriting


admin.site.register(Alert)
admin.site.register(Tag)
admin.site.register(Licence)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CategorySubCategory)
admin.site.register(HelpWriting)
