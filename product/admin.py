from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from .models import Category, Tag, Product


class ProductAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        exclude = ('slug', 'author')


class PostAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, PostAdmin)
