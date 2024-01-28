from django.contrib import admin
from .models import CustomerImage
from django.utils.safestring import mark_safe
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class CustomerImageAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date_uploaded', 'display_image', 'download_image')
    ordering = ('-date_uploaded',)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')

    display_image.short_description = 'Image'

    def download_image(self, obj):
        return mark_safe(f'<a href="{obj.image.url}" download>Download</a>')

    download_image.short_description = 'Download'

    actions = ['download_selected_images']

    def download_selected_images(self, request, queryset):
        response = HttpResponse(content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="selected_images.zip"'

        import zipfile
        import os
        from io import BytesIO

        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zipf:
            for image in queryset:
                image_path = image.image.path
                zipf.write(image_path, os.path.basename(image_path))

        response.write(zip_buffer.getvalue())
        zip_buffer.close()
        return response

    download_selected_images.short_description = 'Download selected images'

admin.site.register(CustomerImage, CustomerImageAdmin)
