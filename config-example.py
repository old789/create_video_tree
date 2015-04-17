#!/usr/local/bin/python2
# -*- coding: utf-8 -*-

webTitle='Example anime'					# Назва серіалу
basePrefix='ea'							# Основний префікс ( в назві файлів, каталогів і т.п.)
numEpisodes=12								# Кількість епізодів
videoCat='a'								# Категорія ( 'a'-аніме, 'm'-музика, 'tv'-фільми )

webHeader='+++ '+webTitle+' +++'					# Назва серіалу в заголовку web-сторіни ( буде додано номер єпізоду та його назва )
baseDir='/usr/local/www/insecuredata/'+videoCat+'/'+basePrefix+'/'	# Каталог, в якому розміщєно дерево html
baseVideoDir='/usr/local/www/xyz/'+videoCat+'/'+basePrefix+'/'		# Каталог, де розміщєні відеофайли
baseIco=basePrefix+'.jpg'					# Дефолтна іконка в головномі індексі
videoWidth='854'							# Ширина вікна плеєра
videoHeight='480'							# Висота вікна плеєра
videoDir=basePrefix							# Підкаталог в каталозі відеофайлів, де знаходяться відеофайли серіалу
videoPrefix=basePrefix						# Префікс в назві відеофайлів серіалу
videoPoster='/a/ea/1.jpg'								# URL зображення для постеру

#episodeTitle=[ '' for i in range(numEpisodes) ]
episodeTitle=[ 'тест1', 'єтест2', 'еуіе3', 'єеуіе4'  ]

numColumns=3								# Кількість стовпчиків в таблиці головного індексу

baseDir=basePrefix+'/'						#### DEBUG ####
baseVideoDir=basePrefix+'-video/'						#### DEBUG ####
videoPrefix='ea'

addon=[										# Доповнення, описуються назва та ім'я файла (без розширення)
	['opening','ea-op'],
	['ending','ea-end']
]

#--------------------------------------------------------------------------------
