# utilCode
폴더 정리 등

### classifyTag.py
input: list_attr_cloth_trim.txt (deepFashion 라이브러리에서 제공)<br>
output: fabric_labels.txt와 texture_labels.txt 파일 생성

### classifyCatg.py, classifyCatg_.py
texture_labels.txt와 fabric_labels.txt에 따라 deepFashion에서 제공하는 이미지 데이터를 속성(category, texture, fabric)에 따라 분류할 때 사용
