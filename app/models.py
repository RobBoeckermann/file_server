import os
from django.db import models
import datetime
import uuid


class CustomerImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=100)
    image = models.ImageField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Delete the image file from the server
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        super().delete(*args, **kwargs)