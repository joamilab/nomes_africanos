#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:44:44 2020

Dados obtidos em https://www.slavevoyages.org, acervo digital com dados de viagens 
de pessoas africanas que foram capturadas e vendidas como escravas para países das 
Américas e Europa durante os séculos XVI - XIX. 

Tutorial de wordcloud com Python consultado: 
    https://sigmoidal.ai/como-criar-uma-wordcloud-em-python

@author: joamila
@date: 29/03/2020
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

#Carregar os dados de arquivo .csv
df_african_base = pd.read_csv('AfricanNamesDatabase.csv', sep=',')

#Substituir todos os nomes faltantes, representados por strings vazias,
 #pelo valor Nan
df_african_base['Name'].replace(" ", np.nan, inplace=True)

#Excluir linhas que contenham algum valor Nan
df_african_base.dropna(subset=['Name'], inplace=True)

#Usar apenas coluna com os nomes
names = df_african_base['Name']

#Colocar todos os nomes em uma mesma string
all_names = names.str.cat(sep=',')

#Imagem com mapa da África usada como máscara (dentro dos limites é branco e fora
 #preto)
africa_mask = np.array(Image.open("african-map.png"))

#Gerar nuvem de palavras
wordcloud = WordCloud(background_color="black", width=1000,
                      height=1000, max_words=250,
                      mask=africa_mask, 
                      max_font_size=200,
                      min_font_size=1).generate(all_names)

#Imprimir nuvem de palavras
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()

plt.imshow(wordcloud)
wordcloud.to_file("wordcloud_african_names.png")