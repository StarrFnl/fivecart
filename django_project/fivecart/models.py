from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.


class User(models.Model):
    user_name = models.TextField()

    def __str__(self):
        return self.user_name

class Company(models.Model):
    company_name = models.TextField()

    def __str__(self):
        return self.company_name

class BookWriter(models.Model):
    book_writer = models.TextField()

    def __str__(self):
        return self.book_writer

class Book(models.Model):
    title = models.TextField()
    book_writer = models.ForeignKey(BookWriter, related_name="writer", on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, related_name="company", on_delete=models.SET_NULL, null=True)
    book_date = models.TextField()
    is_classic = models.BooleanField(null=True)

    def __str__(self):
        return self.title


class Report(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="book", on_delete=models.CASCADE)
    report_date = models.TextField()
    report_text = models.TextField()
    keywords = models.TextField()
    keyword_type = models.TextField()

    def date_validate(self, date_input, date_format):
        try:
            datetime.strptime(date_input, date_format)
            return True
        except ValueError:
            return False

    def clean(self):
        # report_date 필드의 유효성 검사. 추후 추가
        if not self.user:
            raise ValidationError("유저 입력 필요")
        if not self.book:
            raise ValidationError("도서 입력 필요")
        if not self.date_validate(self.report_date, "%Y/%m/%d"):
            raise ValidationError("날짜 확인 필요")
        if not self.report_text:
            raise ValidationError("본문 확인 필요")

    def save(self, *args, **kwargs):
        # 모델 인스턴스를 저장하기 전에 clean 메소드를 호출하여 유효성 검사 및 정제를 수행
        self.clean()
        super(Report, self).save(*args, **kwargs)


# def convert_and_update_data():
#     data_to_update = Book.objects.all()
#     print(data_to_update)
#
#     for item in data_to_update:
#         date_string = item.book_date
#         try:
#             date_object = datetime.strptime(date_string, '%Y/%m/%d').date()
#             item.date_field = date_object
#             item.save()
#             print(date_object)
#         except ValueError:
#             print(f"Invalid date format: {date_string}")
#
# convert_and_update_data()