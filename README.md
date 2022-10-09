# 한글 MBTI Backend

펀딩 시작 시 알림을 위해 정보를 수집하는 서비스입니다.

Flask를 통해 제작하였으며, Docker Container로 만들어 CloudType에 배포하였습니다.

## API 사용 방법

`POST` 형식으로 API 주소( https://api.mbti.hangeul.luna.codes/ )에 API Request를 보내면 코드 실행 결과가 반환됩니다.

Request 형식
```json
{
  "phoneNum": ""  /* 전화번호 */
}
```

 
 Response 형식
 ```json
{
  "phoneNum": ""  /* 저장된 전화번호 */
}
```
  - Status Code: `200` - 정상


## 개발을 위해선

Firebase Dashboard에서 Admin Key 파일을 다운받아 'firebase-adminkey.json' 이름으로 프로젝트 경로 제일 상단에 파일을 저장하여야 합니다.