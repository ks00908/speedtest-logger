######################################################################
#                      PYTHON SPEED LOGGER                           #
#                  by  ks0908/Krzysztof Szypuła                      #
######################################################################


####################   IMPORTS AND INITS  ################
import speedtest
import logging
import time
import os
from datetime import datetime
print("Setting up connection to speedtest.com servers to begin testing connection speed.\nPlease wait, no interaction with program in needed.\nTests will automatically happen each 10 minutes\nTest measurement will be confirmed by console print\n\n")

#################################################


####################  CODE  #####################

logging.basicConfig(filename="speedlog.txt",
                level=logging.DEBUG,
                format='%(levelname)s: %(asctime)s %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S')


try:
     while True:
      speedtester = speedtest.Speedtest()
      speedtester.get_best_server()
      upload = speedtester.upload()
      download = speedtester.download()
      uploadMbps = str(round(upload/1000000, 2))
      downloadMbps = str(round(download/1000000, 2))
      logging.info("\nConnection Speed: \n DOWNLOAD: "+ downloadMbps +"\n UPLOAD: "+uploadMbps+"\n\n ALL SPEEDS IN Mbps \n\n==========================================\n")
      print("speed measured        "+str(datetime.now()))
      time.sleep(600)
except speedtest.ConfigRetrievalError:
      print("connection timeout         "+str(datetime.now()))
      logging.warning("\nexception: connection timeout")
      pass
except Exception as e:
      print("\nan error occured and halted execution of program\nafter you press any button as requested via command prompt application will close")
      logging.error("An exception occured and stopped execution of aplication. \nTRACEBACK:\n\n"+str(e))
      quit()