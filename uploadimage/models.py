from django.db import models
from django.utils import timezone
from PIL import Image
from io import BytesIO
import time
import hashlib


class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    thumbnail_200 = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_400 = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    original_link = models.URLField(null=True, blank=True)
    expiring_link = models.URLField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def generate_thumbnail(image_data, size):
        """Generate a thumbnail from an image and return it as bytes."""
        with BytesIO(image_data) as image_buffer:
            # Open the image using Pillow
            image = Image.open(image_buffer)
            # Resize the image to the desired thumbnail size
            image.thumbnail(size)
            # Convert the thumbnail image to bytes
            with BytesIO() as output_buffer:
                image.save(output_buffer, format='JPEG')
                thumbnail_bytes = output_buffer.getvalue()
            return thumbnail_bytes


    def generate_expiring_link(self, expiration_time):
        # Get the current time
        current_time = int(time.time())

        # Calculate the expiration timestamp
        expiration_timestamp = current_time + expiration_time

        # Generate a random string for the token
        token = hashlib.sha256(str(time.time()).encode()).hexdigest()

        # Create the expiring link URL
        expiring_link_url = f"/images/{self.id}/expiring-link/{token}/{expiration_timestamp}"

        return expiring_link_url

    def save(self, *args, **kwargs):
        # Generate thumbnail sizes
        self.thumbnail_200 = self.generate_thumbnail(self.image_file, 200)
        self.thumbnail_400 = self.generate_thumbnail(self.image_file, 400)

        # Generate links
        self.original_link = self.image_file.url
        self.expiring_link = self.generate_expiring_link(self.image_file.url, self.expiration_date)

        super(Image, self).save(*args, **kwargs)

    def set_expiration_date(self, seconds):
        self.expiration_date = timezone.now() + timezone.timedelta(seconds=seconds)

    def __str__(self):
        return self.image_file.name
