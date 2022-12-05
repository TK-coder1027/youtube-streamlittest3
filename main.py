import streamlit as st
import time

st.title('Streamlit 入門')

#st.write('DataFrame')
#st.write('DisplayImage')

#st.write('Interactive Widgets')
st.write('プログレスバーの表示')
'Start!!'

#latest_iteration = st.empty()
bar = st.progress(0)
latest_iteration = st.empty()

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!!!'


left_column, right_column, other_column = st.columns(3)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
    other_column.write('ここだよ')

# left_column1, right_column1, other_column1 = st.columns(3)
# button1 = left_column1.button('右カラムに文字を表示')
# if button1:
#     right_column1.write('ここは右カラム')
#     other_column1.write('ここだよ')

expander1 = st.expander('問いあわせ内容1')
expander1.write('問いあわせの回答1')
expander2 = st.expander('問いあわせ内容2')
expander2.write('問いあわせの回答2')
expander3 = st.expander('問いあわせ内容3')
expander3.write('問いあわせの回答3')



# text = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味は', text, 'です。' 

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

# st.sidebar.write('Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味は', text, 'です。' 

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

# option =st.selectbox(
#     'あなたが好きな数字を教えて下さい',
#     list(range(1, 11))
# )

#st.write('あなたは選んだ', option)

# if st.checkbox('Show Image'):
#     img = Image.open('sample1.jpg')
#     st.image(img, caption='kamei', use_column_width=True)

# df = pd.DataFrame({
#     '１列目': [1, 2, 3, 4],
#     '２列目': [10, 20, 30, 40]

# })

# df1 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

#st.line_chart(df1)

# st.map(df1)

#print(df)

# st.write(df1)
#st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

#st.dataframe(df.style.highlight_max(axis=0))

#staticなテーブルをつくるときにtableを使う
#st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```


"""
