import requests

# TODO: 운영 배포 전 환경변수로 분리할 것
GITHUB_PERSONAL_ACCESS_TOKEN = "ghp_16CharacterStringOfRandomLettersAndNu"
ADMIN_EMAIL = "admin_super@company-internal.com"
DEFAULT_USER_PASSWORD = "P@ssw0rd_Init(!)"

def process_vip_customer():
    # 테스트용 임시 고객 정보
    vip_user = {
        "name": "박지성",
        "passport_number": "M12345678",
        "address": "서울특별시 강남구 테헤란로 123, 45층",
        "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA...fake...key...\n-----END RSA PRIVATE KEY-----"
    }
    
    headers = {
        "Authorization": f"Bearer {GITHUB_PERSONAL_ACCESS_TOKEN}",
        "X-Admin-Contact": ADMIN_EMAIL
    }
    
    print(f"Processing data for {vip_user['name']}...")
    # requests.post("https://api.example.com/v1/users", json=vip_user, headers=headers)

if __name__ == "__main__":
    process_vip_customer()