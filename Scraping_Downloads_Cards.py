#!/usr/bin/env python3
#Author: Basuh94

from bs4 import BeautifulSoup
import requests
import urllib3
import string
import os   

url = 'https://mtgpics.com/'

def DownloadImage( url, name, nameFolder ):  
    try:
        directory = './' + nameFolder + '/'
        CreateFolfer( directory )
        url_image = url
        auxUrl=url_image.replace('reg', 'big') 
        name_local_image = name 
        print(auxUrl)
        image = requests.get( auxUrl ).content
        with open( directory + name_local_image, 'wb' ) as handler:
	        handler.write( image )
    except:
        #f = open( directory + 'Error-Log.txt' )
        #f.write('Error Download: '  '->' + name + '\n' )
        #f.close()
        print( 'Image download failed: ' + auxUrl )

def CreateFolfer( directory ):
    try:
        os.stat( directory )
    except:
        os.mkdir( directory )

def MountUrl( url, directory, condition, card ):
    page = requests.get( url + directory ) 
    soup = BeautifulSoup( page.content, 'html.parser' )
    if( card == False ):
        need = soup.find_all( 'a', href = True )
        for a in need:
            completUrl = url + a[ 'href' ]
            if( condition in completUrl ):
                print( completUrl )
            MountUrl(url, a[ 'href' ], '', True)
    else:
        cards = soup.find_all( 'img', style = 'display:block;' )
        titles = soup.find_all( 'img', style ='max-width:500px;max-height:150px;' )
        for t in titles:
            title = t[ 'alt' ]
            print( title )
            for c in cards:
                image = c[ 'src' ].strip( '../' )
                name = c[ 'alt' ].rstrip( title ) + '.full.jpg'
                auxName = name.replace( '-', '' )
                clearName = auxName.replace( '/', '' )
                showUrl = url + image
                nameFolder = image.replace( 'pics/reg/', '' )[0:3]
                print( 'Download: ' + showUrl + ' -> ' + auxName.strip() )
                DownloadImage( showUrl, clearName, nameFolder.upper() )

MountUrl( url, 'sets', 'set?set=', False )

 
