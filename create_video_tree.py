#!/usr/local/bin/python2
# -*- coding: utf-8 -*-

import sys,os
from string import Template

webTitle='Empty'							# Назва серіалу ( буде показано в header title web-сторінки )
basePrefix='tst'							# Основний префікс ( в назві файлів, каталогів і т.п.)
numEpisodes=1								# Кількість епізодів
videoCat='a'								# Категорія ( 'a'-аніме, 'm'-музика, 'tv'-фільми )

webHeader=webTitle							# Назва серіалу в заголовку web-сторіни ( буде додано номер єпізоду та його назва )
baseDir='/usr/local/www/insecuredata/'+videoCat+'/'+basePrefix+'/'	# Каталог, в якому розміщєно дерево html
baseVideoDir='/usr/local/www/xyz/'+videoCat+'/'+basePrefix+'/'		# Каталог, де розміщєні відеофайли
baseIco=basePrefix+'.jpg'					# Дефолтна іконка в головномі індексі
videoWidth='854'							# Ширина вікна плеєра
videoHeight='480'							# Висота вікна плеєра
videoDir=basePrefix							# Підкаталог в каталозі відеофайлів, де знаходяться відеофайли серіалу
videoPrefix=basePrefix						# Префікс в назві відеофайлів серіалу
videoPoster=''								# URL зображення для постеру

episodeTitle=[ ]							# Назви єпізодів, якщо потрібно.

numColumns=2								# Кількість стовпчиків в таблиці головного індексу

addon=[										# Доповнення, описуються назва та ім'я файла (без розширення)
	['opening','sw1-op'],
	['ending','sw1-end']
]

addon=[]

#--------------------------------------------------------------------------------

t1 = Template('''<!DOCTYPE html>
<html>
<head>
  <title>$tmplTitle</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <link href="http://m3.z7z.me/video-js/video-js.css" rel="stylesheet">
  <script src="http://m3.z7z.me/video-js/video.js"></script>
  <script>
    videojs.options.flash.swf = "http://m3.z7z.me/video-js/video-js.swf"
  </script>
</head>
<body>
<div align="center">
  <h2>$tmplHead</h2><br>
</div>
<div align="center">
  <video id="$tmplId" class="video-js vjs-default-skin vjs-big-play-centered" autoplay controls preload="auto"
    width="$tmplWidth" height="$tmplHeight" $tmplPoster data-setup='{}'>
    <source src="http://m3.z7z.me:800/c14d5f/$tmplCateg/$tmplDir/$tmplVideoFile" type='video/mp4' />
  </video>
</div>
</body>
</html>
''')

t2 = Template('''<!DOCTYPE html>
<html>
<head>
  <title>$tmplTitle</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>

<body>

<table border=0 width=80% align="center">

  <tr>
    <td align="center" colspan=$tmplColumns><h3><font color="gray">$tmplHeader</font></h3></td>
  </tr>
$mainTable
  <tr>
    <td align="center" colspan=$tmplColumns><h3><font color="gray">***</font></h3></td>
  </tr>

</table>
</body>
</html>
''')

t3 = Template('''   <td align="center">
      <a href="$FleftNum/index.html"><img src="$tmplIco"></a><br><strong>$tmplEpiName</strong><br>&nbsp;
   </td>
''')

t4 = Template('''  <tr>
    <td align="center" colspan=$tmplColumns><h3><font color="gray">***</font></h3></td>
  </tr>
''')

def usage():
	print 'Usage: ',sys.argv[0],' configfile all|tree|index'
	exit(1)

def getEpiName(i):
	if i > numEpisodes:
		rc='<br>'+addon[i-numEpisodes-1][0]
	else:
		rc='<br>episode '+str(i)
		ep=i-1
		if ep < len(episodeTitle):
			if episodeTitle[ep]:
				rc+='<br>'+episodeTitle[ep]
	return rc

def getVideoFileName(i,fi):
	if i > numEpisodes:
		rc=addon[i-numEpisodes-1][1]
	else:
		rc=videoPrefix+fi
	return rc

def creVidTree():
	if not os.path.exists(baseDir):
		os.mkdir(baseDir)
	if not os.path.exists(baseVideoDir):
		os.mkdir(baseVideoDir)
	for i in range(1,numEpisodes+1+len(addon)):
		FleftNum="%02u" % (i)
		epiDir=baseDir+FleftNum+'/'
		if not os.path.exists(epiDir):
			os.mkdir(epiDir)
		fn=epiDir+'index.html'
		if os.path.exists(fn):
			os.rename(fn,fn+'.prev')
		curvideoPoster=''
		if videoPoster:
			curvideoPoster='poster="'+videoPoster+'"'
		out=open(fn,'w')
		out.write(t1.substitute(
					tmplTitle=webTitle,
					tmplHead=webHeader+getEpiName(i),
					tmplId=basePrefix+'-'+FleftNum,
					tmplWidth=videoWidth,
					tmplHeight=videoHeight,
					tmplCateg=videoCat,
					tmplDir=videoDir,
					tmplPoster=curvideoPoster,
					tmplVideoFile=getVideoFileName(i,FleftNum)+'.mp4'))
		out.close()

def creBaseIndex():
	k=0
	s=''
	numRow=numEpisodes//numColumns
	if (numEpisodes % numColumns) != 0 :
		numRow+=1
	for i in range(numRow):
		s+='  <tr>\n'
		for j in range(numColumns):
			k+=1
			if k > numEpisodes :
				s+='   <td></td>\n'
			else:
				s+=t3.substitute(tmplEpiName=getEpiName(k), FleftNum="%02u" % (k), tmplIco=baseIco)
		s+='  </tr>\n'
	if len(addon):
		k=0
		l=len(addon)
		s+=t4.substitute(tmplColumns=numColumns)
		numRow=l//numColumns
		if (l % numColumns) != 0 :
			numRow+=1
		for i in range(numRow):
			s+='  <tr>\n'
			for j in range(numColumns):
				if k < l:
					s+=t3.substitute(tmplEpiName=addon[k][0], FleftNum="%02u" % (k+numEpisodes+1), tmplIco=baseIco)
				else:
					s+='   <td></td>\n'
				k+=1
			s+='  </tr>\n'
	fn=baseDir+'index.html'
	if os.path.exists(fn):
		os.rename(fn,fn+'.prev')
	out=open(fn,'w')
	out.write(t2.substitute(
				tmplTitle=webTitle,
				tmplHeader=webHeader,
				tmplColumns=numColumns,
				mainTable=s))
	out.close()

#  main   --------------------------------------------------

if len(sys.argv) != 3:
	usage()

if os.path.exists(sys.argv[1]):
	execfile(sys.argv[1])
else:
	print 'Config file not found'
	exit(1)

if sys.argv[2] == 'tree':
	creVidTree()
elif sys.argv[2] == 'index':
	creBaseIndex()
elif sys.argv[2] == 'all':
	creVidTree()
	creBaseIndex()
else:
	usage()
