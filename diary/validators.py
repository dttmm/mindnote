from django.core.exceptions import ValidationError


def validate_no_hash(value):
    if "#" in value:
        raise ValidationError("#을 사용할 수 없습니다", code="hash-err")


def validate_no_numbers(value):
    for i in value:
        if i.isdigit():
            raise ValidationError("숫자를 사용할 수 없습니다", code="num-err")


def validate_score(value):
    if value > 10 or value < 0:
        raise ValidationError("0부터 10사이의 숫자만 들어갈 수 있습니다.", code="score-err")
