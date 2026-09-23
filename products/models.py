from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name="عنوان")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, verbose_name="عنوان")
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="کپشن")
    image = models.ImageField(upload_to="products/", verbose_name="عکس")
    price = models.PositiveBigIntegerField(verbose_name="قیمت")
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    discount_price = models.PositiveIntegerField(blank=True, null=True, verbose_name="تخفیف")
    stock = models.IntegerField(verbose_name="موجودی")
    
    class Meta:
         verbose_name_plural = "محصولات" 
         
         
    def __str__(self):
            return self.title