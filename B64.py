#!/usr/bin/env python3
#Author: Basuh94

import base64

def interfaceInptut():
    print( 'Welcome, Base64 encoder[E] / decoder[D] / close[C]' )
    interface = input( 'Input: ' )
    if( interface == 'E' or interface == 'e' or interface == 'D' or interface == 'd' or interface == 'c' or interface == 'C' ):
        if( interface == 'E' or interface == 'e' ):
            dataEncod = input( 'Enter the value you need to code in BASE64: ' )
            encodeB64(dataEncod)
        elif(interface == 'D' or interface == 'd'):
            dataDecode= input( 'Enter the value you need to decode BASE64: ' )
            decodeB64(dataDecode) 
        else:
            print( 'Goodbye!' )
            exit()        
    else:
        print( 'Error, the entered parameter is not correct!' )
        interfaceInptut()

def decodeB64(data):
    try:
        dataDescode = base64.b64decode(data.encode( 'utf-8' ) )
        print( 'Reply: ' + str( dataDescode, 'utf-8' ) )
    except:
        print( 'The values ​​are incorrect!' )
        return( interfaceInptut() )

def encodeB64(data):
    try:
        dataEncode = base64.b64encode(data.encode( 'utf-8' ) )
        print( 'Reply: ' + str( dataEncode, 'utf-8' ) )
    except:
        print( 'The values ​​are incorrect!' )
        return( interfaceInptut() )

interfaceInptut()


