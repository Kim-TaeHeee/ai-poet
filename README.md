# 인공지능 시인 (AI Poetry Generator)

한국어 시를 생성하는 Streamlit 기반 웹 애플리케이션입니다.

## 프로젝트 소개

이 애플리케이션은 OpenAI의 GPT-4o-mini 모델과 LangChain 프레임워크를 사용하여 사용자가 입력한 주제에 대한 아름다운 한국어 시를 자동으로 생성합니다.

## 주요 기능

- 🎨 사용자 정의 주제로 시 생성
- 🔐 안전한 API 키 관리 (사이드바에서 입력)
- 💬 직관적인 사용자 인터페이스
- ⚡ 실시간 시 생성

## 기술 스택

- **Frontend**: Streamlit
- **LLM Framework**: LangChain
- **AI Model**: OpenAI GPT-4o-mini
- **Language**: Python 3.x

## 설치 방법

### 1. 저장소 클론 (또는 파일 다운로드)

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. 가상환경 생성 (권장)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. Streamlit 추가 설치

requirements.txt에 streamlit이 포함되어 있지 않으므로 별도로 설치해야 합니다:

```bash
pip install streamlit
```

## 사용 방법

### 1. 애플리케이션 실행

```bash
streamlit run app.py
```

### 2. 웹 브라우저에서 접속

기본적으로 `http://localhost:8501`에서 실행됩니다.

### 3. API 키 입력

- 사이드바에서 OpenAI API 키를 입력합니다
- API 키는 `sk-`로 시작합니다
- [OpenAI 플랫폼](https://platform.openai.com/)에서 API 키를 발급받을 수 있습니다

### 4. 시 생성

1. 메인 화면의 입력창에 시의 주제를 입력합니다
2. "시 작성 요청하기" 버튼을 클릭합니다
3. AI가 생성한 시를 확인합니다

## 주요 의존성 패키지

| 패키지 | 버전 | 용도 |
|--------|------|------|
| langchain | 1.0.5 | LLM 체인 구성 |
| langchain-openai | 1.0.2 | OpenAI 모델 연동 |
| openai | 2.7.2 | OpenAI API 클라이언트 |
| streamlit | - | 웹 UI 프레임워크 |
| pydantic | 2.12.4 | 데이터 검증 |

## 코드 구조

```
.
├── app.py              # 메인 애플리케이션 파일
├── requirements.txt    # 의존성 패키지 목록
└── README.md          # 프로젝트 문서 (이 파일)
```

## 주요 구성 요소

### LangChain 체인 구성

```python
prompt → llm → output_parser
```

1. **Prompt Template**: 시스템 메시지와 사용자 입력을 구성
2. **LLM**: GPT-4o-mini 모델로 시 생성
3. **Output Parser**: 문자열 형태로 결과 파싱

## 에러 처리

애플리케이션은 다음과 같은 에러를 처리합니다:

- API 키 미입력
- 주제 미입력
- API 키 유효성 오류
- 일반적인 실행 오류

## 환경 변수

API 키는 런타임에 환경 변수로 설정됩니다:

```python
os.environ['OPENAI_API_KEY'] = api_key
```

## 보안 고려사항

- API 키는 `type="password"`로 마스킹되어 입력됩니다
- API 키는 세션 기반으로만 저장되며 파일에 저장되지 않습니다
- 프로덕션 환경에서는 환경 변수나 비밀 관리 도구 사용을 권장합니다

## 라이선스

이 프로젝트의 라이선스 정보를 추가하세요.

## 기여

기여를 환영합니다! Pull Request를 보내주세요.

## 문의

문제가 발생하거나 질문이 있으시면 이슈를 등록해주세요.

---

**Note**: OpenAI API 사용에는 비용이 발생할 수 있습니다. [OpenAI 가격 정책](https://openai.com/pricing)을 확인하세요.
