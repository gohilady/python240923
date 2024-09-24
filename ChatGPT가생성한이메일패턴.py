import re

# 이메일 주소 패턴 정의
#raw string notation : 가공하지 않은 문자열
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 이메일 유효성 검사 함수
def is_valid_email(email):
    if re.match(email_pattern, email):
        return True
    return False

# 샘플 이메일 주소
sample_emails = [
    "valid.email@example.com",  # 유효한 이메일
    "invalid.email@.com",       # 잘못된 이메일 (도메인 이름 없음)
    "another.valid-email_123@sub.domain.org",  # 유효한 이메일
    "invalid-email@domain..com", # 잘못된 이메일 (연속된 점)
    "invalid@domain@domain.com", # 잘못된 이메일 (이중 @)
    "valid-email+test@domain.co.uk", # 유효한 이메일
    "invalid-email@domain",      # 잘못된 이메일 (최상위 도메인 없음)
    "123456@numbers.com",        # 유효한 이메일
    "user.name@domain-.com",     # 잘못된 이메일 (도메인에 잘못된 대시)
    "name@domain..com",          # 잘못된 이메일 (연속된 점)
    "normal@domain.com"          # 유효한 이메일
]

# 샘플 이메일 유효성 검사 결과 출력
for email in sample_emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
