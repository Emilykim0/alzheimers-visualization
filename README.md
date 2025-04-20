# 🧠 알츠하이머병 시각화 프로젝트 (Pandas & Matplotlib)

고령화 사회에 접어들며 **알츠하이머병(AD)**에 대한 조기 진단의 중요성이 커지고 있습니다.  
본 프로젝트는 **혈압, 콜레스테롤, 유전자, 뇌 구조 지표** 등 다양한 변수와 AD 진단 사이의 관계를 **시각화 기반으로 분석**한 결과를 담고 있습니다.

> **📅 진행 기간:** 2025.01.24 ~ 2025.01.31  
> **📊 사용 도구:** pandas, matplotlib.pyplot, seaborn

---

## 📂 폴더 구조

alzheimers_visual_project/ │ ├── Alzheimer_김영혜.ipynb # 메인 분석 노트북 ├── utils.py # 컬러팔레트 및 유틸 함수 ├── AD.txt # 데이터 설명 텍스트 ├── README.md # 프로젝트 설명 파일 │ └── DATA_AD/ ├── alzheimer.csv ├── alzheimers_disease_data.csv └── nep499.csv

---

## 💡 주요 분석 내용

- ✅ 혈압 및 콜레스테롤 지표에 따른 AD 진단 여부 및 MMSE 비교  
- ✅ eTIV, nWBV, ASF 등 뇌 구조 지표와 인지 기능(MMSE) 및 치매 진행도(CDR) 관계  
- ✅ APOE 유전자 보유 여부 및 조합에 따른 AD 발병률 분석  
- ✅ 상관관계 히트맵 및 그룹별 비교 시각화 (bar, box, scatter, pie 등)

---

## ▶️ 실행 방법

```bash
pip install pandas matplotlib seaborn
```
이후 Alzheimer_김영혜.ipynb 파일을 실행하면 전체 분석 과정을 볼 수 있어요.

## 🔗 관련 링크
🧾 [프로젝트 상세 노션 페이지](https://yeonghyekim.notion.site/Alzheimer-s-Disease-18fe2859370c804ab1dbc4bdde782bc7?pvs=4)

👩‍💻 프로젝트 회고
이 프로젝트는 단기간 내 복잡한 분석을 기획하고 수행하는 훈련을 목표로 했습니다.
특히 상관관계 분석만으로 인과관계를 판단할 수 없는 한계,
그리고 제한된 데이터 안에서 인사이트를 도출하려는 노력이 주요 학습 포인트였습니다.