## 설치 방법 (수동)

### 1. 시스템 의존성 설치

#### macOS
```bash
brew install poppler
```

#### Ubuntu/Debian
```bash
sudo apt-get install poppler-utils
```

#### Windows
1. [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)에서 다운로드
2. PATH에 bin 폴더 추가

### 2. 가상환경 설정 (추천)

```bash
# 가상환경 생성 및 패키지 설치
./setup.sh
```

setup.sh 스크립트는:
- poppler 설치 여부 확인
- Python 가상환경 생성
- 필요한 패키지 자동 설치

### 3. 직접 설치 (선택사항)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 사용 방법

### 방법 1: pdf2qb 명령어 사용 (추천)

```bash
# 가상환경 활성화
source venv/bin/activate

# pdf2qb 명령어로 실행
pdf2qb <PDF_폴더_경로>

# 예시
pdf2qb sample
pdf2qb sample --columns 3
```

### 방법 2: 쉘 스크립트 사용

```bash
# 가상환경에서 실행
./run.sh <PDF_폴더_경로>

# 예시
./run.sh sample
./run.sh sample --columns 3
```

### 방법 3: Python 직접 실행

```bash
# 가상환경 활성화
source venv/bin/activate

# Python 스크립트 실행
python3 pdf2qb.py <PDF_폴더_경로>
```

### 옵션

- `--columns`, `-c`: 페이지당 열 개수 (기본값: 2)

### 예시

```bash
# sample 폴더의 모든 PDF 파일 처리 (기본 2열)
pdf2qb sample

# 3열로 분할
pdf2qb sample --columns 3

# 또는 쉘 스크립트 사용
./run.sh sample --columns 3
```

## 출력 형식

각 PDF 파일에 대해 파일명과 동일한 폴더가 생성되며, 다음과 같은 형식으로 이미지가 저장됩니다:

```
page_1_C01B0001.png  # 페이지 1, 열 1, 박스 1
page_1_C01B0002.png  # 페이지 1, 열 1, 박스 2
page_1_C02B0001.png  # 페이지 1, 열 2, 박스 1
...
```

## 작동 원리

1. PDF 파일을 페이지 단위 이미지로 변환
2. 각 페이지를 지정된 수의 열로 분할
3. 각 열을 40픽셀 단위로 스캔하여 흰색 구간 감지
4. 연속된 비흰색 구간을 하나의 문제(박스)로 간주
5. 각 문제를 개별 PNG 파일로 저장

## 파일 구조

```
pdf_to_question_bank/
├── pdf2qb.py                     # 메인 Python 스크립트
├── setup.py                      # 패키지 설치 스크립트
├── requirements.txt              # Python 패키지 의존성
├── setup.sh                      # 가상환경 설정 스크립트
├── run.sh                        # 실행 스크립트
├── quickstart.sh                 # 빠른 시작 스크립트
├── venv/                         # Python 가상환경 (자동 생성)
├── sample/                       # 샘플 PDF 파일
│   ├── *.pdf                     # PDF 파일들
│   └── [PDF_파일명]/             # 생성된 문제 이미지들
│       └── page_*_C*B*.png
└── README.md
```

## 테스트

샘플 PDF 파일로 테스트:

```bash
./quickstart.sh sample/

# 또는
./quickstart.sh {your_folder_path} --columns 3
```

성공적으로 실행되면 지정한 폴더 내에 각 PDF 파일명과 동일한 폴더가 생성되고, 그 안에 개별 문제 이미지들이 저장됩니다.

