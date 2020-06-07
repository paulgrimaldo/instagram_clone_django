from django.contrib import admin
from posts.models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'photo', 'user')
    list_display_links = ('id', 'title')
    search_fields = (
        'title',
        'user__email',
        'user__first_name',
        'user__last_name',
        'profile__phone_number'
    )
    list_filter = (
        'title',
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )
    fieldsets = (
        ('Post Info', {
            'fields': ('title', 'photo')
        }),
        ('User info', {
            'fields': ('user', 'profile')
        }),
        ('Metadata', {
            'fields': ('created', 'modified')
        })
    )

    readonly_fields = ('created', 'modified')
