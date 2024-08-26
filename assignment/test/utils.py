from io import BytesIO
from requests.models import Response
import json


def get_mock_exchange_api_response():
    """
    Method to create sample response from the API with the new structure
    """
    mock_api_response = Response()
    mock_api_response.status_code = 200

    # สร้าง dictionary ตามโครงสร้างที่ต้องการ
    response_data = {'base': 'THB', 'result': {'KRW': 38.69}}

    # แปลง dictionary เป็น JSON string และเข้ารหัสเป็น bytes
    json_data = json.dumps(response_data).encode('utf-8')

    # ใส่ข้อมูลลงใน BytesIO object
    mock_api_response.raw = BytesIO(json_data)

    # กำหนด _content เพื่อให้ .json() ทำงานได้
    mock_api_response._content = json_data

    return mock_api_response


# ทดสอบฟังก์ชัน
example = get_mock_exchange_api_response().json()
print(type(example), example)