[English](README.md) | 한국어

# PDF to Question Bank Converter

PDF 파일에서 개별 문제 이미지를 추출하는 도구입니다. PDF 페이지를 열(column)로 분할하고, 각 열에서 공백을 기준으로 개별 문제를 분리하여 이미지 파일로 저장합니다.
anki와 같은 플래시카드에서 문제 은행을 쉽게 생성하고자 만들었습니다.

## 빠른 시작

### 방법 1: pdf2qb 명령어 사용 (추천)

```bash
# 설정 (최초 1회)
./scripts/setup.sh

# 가상환경 활성화 후 사용
source venv/bin/activate
pdf2qb sample
pdf2qb sample --columns 3
```

### 방법 2: 쉘 스크립트 사용

```bash
# 한 번에 설정 및 실행
./scripts/quickstart.sh sample

# 3열로 분할
./scripts/quickstart.sh sample --columns 3
```

첫 실행 시 자동으로 가상환경을 생성하고 필요한 패키지를 설치합니다.
그외의 사용 방법은 [setup](docs/setup.md)를 참고해주세요.

## 미리보기 및 사용 예시




<table>
<tr>
<td>

지정한 경로에 pdf 파일을 넣고 스크립트 실행

<img alt="preview_1" src="https://github.com/user-attachments/assets/ba8eb71b-9554-48fa-a9b4-dc8d7d52c6e1" />
</td>
<td>

결과물: 개별 문제 이미지가 추출되어 저장됨

<img alt="preview_2" src="https://github.com/user-attachments/assets/19c08be1-8ddb-4a3b-850e-a96e1e53f999" />
</td>
</tr>
<tr>
<td>
사용예시: <br/>
추출된 이미지 파일을 anki에 임포트하여 문제 은행 생성
    <img alt="preview_3" src="https://github.com/user-attachments/assets/8728a109-4f00-4aac-9211-61db7b857355" />
</td>
<td>
    <img alt="preview_4" src="https://github.com/user-attachments/assets/20ba421c-0acb-4447-9c4c-6d309d960348" />
</td>
</tr>
</table>



<br/><br/><br/>


# 개선 필요 기능

- 문제나 답안이 아닌 제목이나 페이지 번호 등의 불필요한 이미지도 함께 추출되는 문제
- 흰색 배경이 아닌 문제 이미지도 처리 가능하도록 개선 필요
- 문제.pdf와 답안.pdf를 기반으로 문제 번호별로 매칭된 CSV(`번호,문제경로,답안경로`) 파일을 출력하는 기능 추가
- anki 덱 파일(.apkg)로 바로 변환하는 기능 추가

<br/><br/><br/>

---

**라이선스**

[MIT](LICENSE)
