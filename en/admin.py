from django.contrib import admin
from en.models import PostModel, ContactModel, TopicModel



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







class ContactAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'subject', 'date')
    list_filter = ['date']
    fieldsets = [
        ('Contact', {'fields': ['sender_name', 'sender_email']}),
        ('Message', {'fields': ['subject', 'body']}),
        ('Date',    {'fields': ['date']})
    ]
admin.site.register(ContactModel, ContactAdmin)
