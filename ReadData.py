# -*- coding: utf-8 -*-

import os
#import Params.Parameters as param  #not used


class ReadData:
    
    def __init__(self):
        0;
        
    
    def readFrameStatic(self,count, staticFilePath):
        
        directoryList = os.listdir(staticFilePath)
        val = 0;
        
        for fname in directoryList:
            if (val== count):
                return fname
            else:
                val+=1
  
   
  
 
