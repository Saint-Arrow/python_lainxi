import os, time
import pyautogui

upgrade_85_time=25
upgrade_time=230

FW_1_DIR='C:/Users/Acer/Desktop/'
FW_1_NAME='VX71UVS_G51.V_V9.0.01_20230209_pri.img'

FW_2_DIR='C:/Users/Acer/Desktop/'
FW_2_NAME='VX71UVS_G51.MO_V9.0.01_20230209_pri.img'
kill_upgrade=0

if kill_upgrade==0:
	os.system(r'start /d"F:\WORK\VHD_CWJ_File\tool\upgrade v2.8" upgrade.exe')

if "__main__" == __name__:
	t=0
	while 1==1:
		if kill_upgrade==1:
			os.system(r'start /d"D:\upgrade v2.8" upgrade.exe')
		#选择升级模式
		time.sleep(1)
		pyautogui.click(648, 250,button='left')
		#选择升级文件
		time.sleep(1)
		pyautogui.moveTo(820, 320, duration=1)
		pyautogui.click()
		pyautogui.doubleClick()
		time.sleep(1)
		if t%2 == 0:
		#if 1==1:
			pyautogui.typewrite(FW_1_DIR)
			pyautogui.click(1295,319,button='left') #点击打开
			time.sleep(2)
			
			pyautogui.moveTo(1029,891, duration=1)
			time.sleep(1)
			pyautogui.typewrite(FW_1_NAME)
			
			pyautogui.click(1357,923,button='left')
			time.sleep(2)
		else:
			pyautogui.typewrite(FW_2_DIR)
			pyautogui.click(1295,319,button='left') #点击打开
			time.sleep(2)
			
			pyautogui.moveTo(1029,891, duration=1)
			time.sleep(2)
			pyautogui.typewrite(FW_2_NAME)
			
			pyautogui.click(1357,923,button='left')
			time.sleep(1)
		time.sleep(1)
		#点击升级
		time.sleep(1)
		pyautogui.click(1280, 350,button='left')
		t=t+1
		print ("click:"+str(t))
		count=0
		while count <= upgrade_time:
			print ("click:"+str(t)+"-"+str(count))
			count=count+1
			time.sleep(1)
			#if count==upgrade_85_time:#预计85%就开始杀掉程序，防止提示升级成功，提前退出软件会使得upgrade段错误 
		
		pyautogui.click(965, 540,button='left')
		time.sleep(1)
		if kill_upgrade==1:
			#退出升级软件
			time.sleep(1)
			pyautogui.click(1330, 206,button='left')
			#选择是
			time.sleep(1)
			pyautogui.click(896, 532,button='left')
			time.sleep(1)
	


