import schedule
from bs4 import BeautifulSoup
import pymysql
def job():
    import os

    def fun():
        os.system("python3  /opt/softwares/Py_Monitoring/outhtml.py")
        os.system("python3  /opt/softwares/Py_Monitoring/show.py")
        #os.system("Rscript  /tandelindata/ETL_code/R_text_mysql.R")

    fun()

schedule.every(2).seconds.do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
