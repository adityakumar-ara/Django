
# Create your models here.
from django.db import models

class my_Product(models.Model):
    # 1. Product ka naam (Jyada se jyada 255 character)
    product_name = models.CharField(max_length=255)
    
    # 2. Product ki keemat (10 digit tak, jisme 2 decimal number ho sakte hain)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # 3. Product ka lamba description
    product_description = models.TextField()
    
    # 4. Product ki photo (isey 'products/' naam ke folder mein save karega)
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)

    # Ye function Admin panel mein product ka naam dikhane ke liye hai
    def __str__(self):
        return self.product_name
