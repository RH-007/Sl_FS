
## Creacion de primer StreamLit app

import streamlit as st

st.write("Hola Mundo que mas puedo hacer? 🤔")

## st.button permite mostrar un botón.

## Que estamos construyendo?
## Una simple aplicación que imprime condicionalmente diferentes mensajes dependiendo si el botón fue presionado o no.

## Comportamiento de la aplicación:

## Por defecto, la aplicación imprime Goodbye
## Una vez que se hace click sobre el botón, la aplicación imprime Why hello there

st.header('st.button')

if st.button('Di Hola!!'):
    st.write('Gaaa')
else:
    st.write('Goodbye')
    
"""
**PARTE 2** 

st.write permite imprimir texto y datos en la Streamlit app.

Además de poder mostrar texto, también se puede mostrar lo siguiente mediante el comando st.write():

- Muestra cadenas; funciona como st.markdown()
- Muestra un dict de Python
- Muestra pandas DataFrame se puede mostrar como una tabla
- Gráficos/Esquemas/Representaciones de matplotlib, plotly, altair, graphviz, bokeh
- Y mas (ver st.write en la documentación de Streamlit)    
"""

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

## Ejemplo 1
st.write("aqui puedes agregar un mensaje!") 

## Ejemplo 2
st.write(12345)

## Ejemplo 3
df = pd.DataFrame({
    "col1" : [1,2,3,4],
    "col2" : [10,20,30,40]
})

st.write(df)

## Ejemplo 4
st.write("Abajo hay un datframe:", df, "Encima hay un dataframe")

## Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])


c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)