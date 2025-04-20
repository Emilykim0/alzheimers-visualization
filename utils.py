## 함수 기능 : DataFrame의 컬럼별 고유값과 개수와 고유값 출력
## 함수 이름 : printUniqueValue()
## 매개 변수 : df_columns
## 반 환 값 : 없음
def printUniqueValue(df):
    for col in df.columns:
        print(f"\n[{col} 컬럼의 고유값] ========")
        print('갯수 : ',df[col].nunique())
        print(df[col].unique())



# color code
color4=['#fff0f3','#ffccd5','#ffb3c1','#ff8fa3','#ff758f','#ff4d6d']
color1=["#f0ebd8","#748cab","#3e5c76",'#1d2d44','#0d1321']
color2=['#233d4d','#fe7f2d','#fcca46','#a1c181','#619b8a']
color3=["#d9ed92",'#b5e48c','#99d98c','#76c893','#52b69a','#34a0a4','#168aad','#1a759f','#1e6091','#184e77']
color5=['#f72585','#b5179e','#7209b7','#560bad','#480ca8','#3a0ca3','#3f37c9','#4361ee','#4895ef','#4cc9f0']
