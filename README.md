# 🎤 RANGERS: AI 기반 아티스트-팬덤 채팅 플랫폼

> 📍 **AI 욕설 감지 모델을 활용하여 아티스트와 팬이 건강하게 소통할 수 있는 채팅 서비스**

RANGERS는 **연예인 대상 악성 메시지 문제를 해결하기 위해 개발된 AI 기반 소통 플랫폼**입니다.  
딥러닝 기반 욕설 감지 모델을 통해 **실시간 채팅 필터링**을 지원하며, 아티스트와 팬덤이 **안전하고 긍정적인 커뮤니티 경험**을 할 수 있도록 합니다.  

> 슬로건: _“악성 메시지로부터 아티스트를 수호하는 레인저스”_

---

## 📑 프로젝트 자료

- 📂 [프로젝트 발표 자료 (PDF)](./RANGERS_PPT.pdf)  
- 🎬 [시연 영상 다운로드 (MP4)](./RANGERS시연영상.mp4)  

<p align="center">
  <a href="./RANGERS시연영상.mp4">
    <img src="./media/img/demo_thumbnail.png" alt="시연 영상 썸네일" width="600"/>
  </a>
</p>

---

---

## 📌 주요 기능

- 회원가입 / 로그인 / 로그아웃  
- 아티스트와 팬덤 간 **실시간 채팅** (WebSocket 기반)  
- AI 모델을 활용한 **욕설/비윤리 문장 자동 필터링**  
- **아티스트 피드 / 팬 피드** 기능 제공  
- **매너 온도 시스템** → 사용자별 신뢰도 관리  

---

## 📁 프로젝트 구조

```
RANGERS/
│  manage.py                  # Django 실행 파일
│  README.md
│  requirements.txt           # 기본 라이브러리 목록
│  requirements-linux.txt     # 리눅스 환경용 패키지 설정
│  runtime.txt                # 실행 환경 설정
│  .gitignore
│  .gitattributes
│  RANGERS시연영상.mp4        # 프로젝트 시연 영상
│  mobaxterm 실행순서.txt
│  장고 실행순서.txt
│  깃 사용법 정리.txt
│  prepros-6.config
│  udo ubuntu-drivers devices
│
├─chat/                       # 채팅 기능 (WebSocket)
│   ├─consumers.py
│   ├─routing.py
│   ├─filtering.py            # AI 욕설 감지 로직
│   └─templates/chat/
│
├─feed/                       # 아티스트/팬 피드 기능
├─common/                     # 공통 유틸
├─rangers/                    # Django 프로젝트 설정
├─rangers_model/              # HuggingFace 모델 로드 및 관리
├─templates/                  # 전체 템플릿 (HTML)
├─static/                     # 정적 파일 (CSS, JS)
└─media/img/                  # 이미지 및 업로드 파일
```

---

## ⚙️ 로컬 실행 방법

1. 가상환경 생성 및 패키지 설치
```bash
python -m venv venv
source venv/bin/activate   # (윈도우: venv\Scripts\activate)
pip install -r requirements.txt
```

2. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

3. 서버 실행
```bash
python manage.py runserver
```

---

## 🧠 AI 모델

- **데이터셋**  
  - **AI Hub 한국어 윤리검증 데이터** (약 45만 문장)  
    - 비윤리 여부, 유형(8가지), 강도까지 라벨링된 대화 데이터  
  - **Smilegate 한국어 욕설 데이터**  
  - **한국어 혐오 댓글 데이터셋**  
  - 추가로 변형된 욕설, 신조어, 구어체 포함 데이터를 확보하여 **실제 채팅 환경에 가까운 데이터**로 확장  

- **모델 후보군 (HuggingFace, 총 8종 비교 실험)**  
  - BERT, DistilBERT, KoBERT, KcBERT, BERT-kor, XLM-RoBERTa, mBERT, KoELECTRA-hatespeech  
  - 각 모델에 대해 **정확도, 추론 속도, 욕설 변형 대응력, 고유명사 오탐지율**을 비교  

- **모델 선정 과정**  
  - 단순 금칙어 탐지가 아니라 **문맥 기반 욕설 탐지**가 중요하므로 BERT 계열 모델에 집중  
  - 최종적으로 **`beomi/kcbert-base`** 모델이 **정확도와 변형 욕설 탐지 성능**에서 가장 우수하여 채택  

- **파인튜닝 방식**  
  - HuggingFace Transformers 기반 Fine-tuning  
  - **이진 분류(Binary Classification)**:  
    - **비윤리적(1)** vs **윤리적(0)** 메시지 판별  
  - 추가 레이어(`BERTForSequenceClassification`)를 쌓아 문장 단위 분류 수행  

- **최종 성능**  
  - Test Accuracy: **84%**  
  - 구어체/신조어/변형 욕설에 강건한 성능 확보  
  - 고유명사(인명, 지명 등)에 대한 불필요한 오탐지 최소화  
 

---

## 🛠 사용 기술

| 범주 | 기술 |
|------|------|
| Language | Python 3.x, JavaScript |
| Backend | Django, Django Channels |
| Frontend | HTML5, CSS, Bootstrap |
| Realtime | WebSocket, Redis |
| Database | PostgreSQL, SQLite (dev) |
| AI/NLP | PyTorch, HuggingFace Transformers, KcBERT |
| Infra | GitHub, Figma, Notion |

---

## 🚀 향후 발전 방향
- 모바일 앱 버전 확장  
- 다국어 욕설 감지 모델 적용  
- 대형 팬덤 플랫폼/SNS로의 확장  

---

## 🙋🏻‍♂️ 프로젝트 제작자: RANGERS 팀

- **프론트엔드**: 웹 화면 설계 및 구현  
- **백엔드**: DB 설계, 채팅 기능 개발, 서버 연결  
- **데이터 분석**: 데이터 수집·전처리, NLP 모델 학습 및 평가  

---

## 📫 Contact

- 📧 이메일: [chris123ag@naver.com]  
- 🔗 GitHub: [https://github.com/kwon-sungjae]  

> “AI를 활용해 사회적 문제를 해결하는 경험, 이것이 RANGERS의 출발점이었습니다.”
