from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price', 'description')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        # check title is alpabet
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi harflardan tashkil topgan bo'lishi kerak"
                }
            )

        # check title and author is alfabet
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Muallifi va kitob sarlavhasi bir xil bo'lgan kitobni yuklay olmaysiz"
                }
            )

        return data


    def validate_price(self, price):
        if price< 0 or price>999999999:
            raise ValidationError({
                "status": False,
                "message": "Narx kiritishda xatolik"
            })


    def validate_isbn(self,isbn):
        if not isbn.isdigit():
            raise ValidationError({
                "status": False,
                "message": "Isbn xato kiritildi"
            })
        else:
            print("Successfully")
#  Bu Serializer ni uzida qilingan

# class BookSerializers(serializers.Serializer):
#     title=serializers.CharField(max_length=200)
#     subtitle=serializers.CharField(max_length=200)
#     author=serializers.CharField(max_length=150)
#     isbn=serializers.CharField(max_length=100)
#     price=serializers.DecimalField(max_digits=50,decimal_places=2)
#     description=serializers.CharField()
