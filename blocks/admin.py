from django.contrib import admin
# Register your models here.
from .models import Profile,Book,Block,College,CommentRating,Category
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Block)
admin.site.register(CommentRating)
admin.site.register(College)
admin.site.register(Category)
class BlockInline(admin.TabularInline):
    model = Category.block.through
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
      BlockInline,
        )