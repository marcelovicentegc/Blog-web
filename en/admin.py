from django.contrib import admin
from en.models import PostModel, TopicModel



class TopicAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_filter = ['date']
    fieldsets = [
        ('Topic name',  {'fields': ['name']})
    ]
admin.site.register(TopicModel)






class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'title', 'date')
    list_filter = ['date']
    fieldsets = [
        ('Text',    {'fields':  ['topic', 'title', 'body']}),
        ('Image',   {'fields':  ['image']}),
        ('Date',    {'fields':  ['date']})
    ]
admin.site.register(PostModel, PostAdmin)