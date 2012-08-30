# -*- coding: utf-8 -*-

"""
Module implementing Y-str.
"""

from PyQt4.QtGui import QMainWindow,QTableWidgetItem, QFileDialog
from PyQt4.QtCore import pyqtSignature

from Ui_mainframe import Ui_MainWindow

class Y_str(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        strs='id,ref,Population,location,SNP,HG'
        wstrs=''
        a=[]
        self.labels=['id','ref','Population','location','SNP','HG']
        if self.checkBox.isChecked():
            strs+=',str1'
            wstrs+=' and str1>0'
            a.append(self.spinBox.value())
            self.labels.append('DYS388')
        if self.checkBox_2.isChecked():
            strs+=',str2'
            wstrs+=' and str2>0'
            a.append(self.spinBox_2.value())
            self.labels.append('DYS19/394')
        if self.checkBox_3.isChecked():
            strs+=',str3'
            wstrs+=' and str3>0'
            a.append(self.spinBox_3.value())
            self.labels.append('DYS389I')
        if self.checkBox_4.isChecked():
            strs+=',str4'
            wstrs+=' and str4>0'
            a.append(self.spinBox_5.value())
            self.labels.append('DYS389II')
        if self.checkBox_5.isChecked():
            strs+=',str5'
            wstrs+=' and str5>0'
            a.append(self.spinBox_4.value())
            self.labels.append('DYS390')
        if self.checkBox_6.isChecked():
            strs+=',str6'
            wstrs+=' and str6>0'
            a.append(self.spinBox_6.value())
            self.labels.append('DYS391')
        if self.checkBox_7.isChecked():
            strs+=',str7'
            wstrs+=' and str7>0'
            a.append(self.spinBox_7.value())
            self.labels.append('DYS392')
        if self.checkBox_8.isChecked():
            strs+=',str8'
            wstrs+=' and str8>0'
            a.append(self.spinBox_8.value())
            self.labels.append('DYS393')
        if self.checkBox_9.isChecked():
            strs+=',str9'
            wstrs+=' and str9>0'
            a.append(self.spinBox_9.value())
            self.labels.append('DYS425')
        if self.checkBox_10.isChecked():
            strs+=',str10'
            wstrs+=' and str10>0'
            a.append(self.spinBox_10.value())
            self.labels.append('DYS426')
        if self.checkBox_11.isChecked():
            strs+=',str11'
            wstrs+=' and str11>0'
            a.append(self.spinBox_19.value())
            self.labels.append('DYS434')
        if self.checkBox_12.isChecked():
            strs+=',str12'
            wstrs+=' and str12>0'
            a.append(self.spinBox_15.value())
            self.labels.append('DYS435')
        if self.checkBox_13.isChecked():
            strs+=',str13'
            wstrs+=' and str13>0'
            a.append(self.spinBox_20.value())
            self.labels.append('DYS436')
        if self.checkBox_14.isChecked():
            strs+=',str14'
            wstrs+=' and str14>0'
            a.append(self.spinBox_12.value())
            self.labels.append('DYS437')
        if self.checkBox_15.isChecked():
            strs+=',str15'
            wstrs+=' and str15>0'
            a.append(self.spinBox_16.value())
            self.labels.append('DYS438')
        if self.checkBox_16.isChecked():
            strs+=',str16'
            wstrs+=' and str16>0'
            a.append(self.spinBox_18.value())
            self.labels.append('DYS439')
        if self.checkBox_17.isChecked():
            strs+=',str17'
            wstrs+=' and str17>0'
            a.append(self.spinBox_14.value())
            self.labels.append('DYS385a')
        if self.checkBox_18.isChecked():
            strs+=',str18'
            wstrs+=' and str18>0'
            a.append(self.spinBox_17.value())
            self.labels.append('DYS385b')
        if self.checkBox_19.isChecked():
            strs+=',str19'
            wstrs+=' and str19>0'
            a.append(self.spinBox_13.value())
            self.labels.append('DYSA7.2')
        if self.checkBox_20.isChecked():
            strs+=',str20'
            wstrs+=' and str20>0'
            a.append(self.spinBox_11.value())
            self.labels.append('Y GATE H4')
        if self.checkBox_21.isChecked():
            strs+=',str21'
            wstrs+=' and str21>0'
            a.append(self.spinBox_23.value())
            self.labels.append('DYS448')
        if self.checkBox_22.isChecked():
            strs+=',str22'
            wstrs+=' and str22>0'
            a.append(self.spinBox_22.value())
            self.labels.append('DYS456')
        if self.checkBox_23.isChecked():
            strs+=',str23'
            wstrs+=' and str23>0'
            a.append(self.spinBox_26.value())
            self.labels.append('DYS458')
        if self.checkBox_24.isChecked():
            strs+=',str24'
            wstrs+=' and str24>0'
            a.append(self.spinBox_25.value())
            self.labels.append('DYS635')
        if self.checkBox_25.isChecked():
            strs+=',str37'
            wstrs+=' and str37>0'
            a.append(self.spinBox_24.value())
            self.labels.append('YCAIIa')
        if self.checkBox_26.isChecked():
            strs+=',str38'
            wstrs+=' and str38>0'
            a.append(self.spinBox_21.value())
            self.labels.append('YCAIIb')

        self.result=[]
        if len(strs)>len('id,ref,Population,location,SNP,HG,'):
            import sys,os,sqlite3
#            DB_HOME_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))+'/str.db'
            conn=sqlite3.connect('str.db')
            cu=conn.cursor()
            sql = 'select '+strs+' from'+' str'+' where id>0'+wstrs
            cu.execute(sql)
            for row in cu:
                sum=0
                for i in range(len(a)):
                    sum+=abs(row[6+i]-a[i])
                if sum<6:
                    newnow=list(row)
                    newnow.append(sum)
                    self.result.append(newnow)
            self.result.sort(key=lambda x:x[-1])
#            for x in self.result:
#                print x
            self.labels.append('steps')
            self.tableWidget.setRowCount(len(self.result))  
            self.tableWidget.setColumnCount(len(a)+7)
            self.tableWidget.setHorizontalHeaderLabels(self.labels)
 
            for i in range(self.tableWidget.rowCount()):  
                for j in range(self.tableWidget.columnCount()):  
                    newItem = QTableWidgetItem(str(self.result[i][j])) 
                    self.tableWidget.setItem(i,j,newItem)

            self.pushButton_2.setEnabled(True)

    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        filename=QFileDialog.getSaveFileName(self,self.tr("csv File"),"y-str.csv",self.tr("CSV Files(*.csv)"))
#        print filename
        
        s=[]
        for lable in self.labels:
            s.append(lable) 
            s.append(',')
        s[-1]='\n'
        for i in range(self.tableWidget.rowCount()):  
            for j in range(self.tableWidget.columnCount()):  
                s.append(str(self.result[i][j]).replace(',' , ' ') )
                s.append(',')
            s[-1]='\n'

        try:                                
            fd=open(filename,'w')
            try:                           
                fd.write(''.join(s)) 
            finally:                        
                fd.close()            
        except IOError:                     
            pass            

if __name__ == "__main__":  
    import PyQt4, PyQt4.QtGui, sys
    app = PyQt4.QtGui.QApplication(sys.argv)    
    myapp = Y_str()    
    myapp.show()  
  
sys.exit(app.exec_())  
