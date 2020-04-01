# Import
from statistics import mode
from time import sleep 
from random import randint
from random import choice
import kivy
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
# Main child class from parent Widget class
global file_win
global file_loss
global string
file_win=open('win.txt','a+')
file_loss=open('loss.txt','a+')
string=''
file_win.seek(0)
file_loss.seek(0)
global string_win
global string_loss
global string_loss2
global string_win2
string_win2=file_win.readlines()
string_loss2=file_loss.readlines()
string_win=string_win2
string_loss=string_loss2
print ('Win:',string_win)
print('Loss:',string_loss)


def ai_fun(new_av,loc,string):
	global string_loss
	def list_making(l):
		pass
	length=len(string_loss)
	le=len(string)
	le=le-1
	new_list=[]
	list_for_word=[]
	for i in range(length):
		if string_win[i][le]==loc:
			new_list.append(string_win[i])
			try :
				list_for_word.append(string_win[i][le+1])
			except :
				pass
	print ('list for word :',list_for_word)	
	try:
		candidate=mode(list_for_word)
		print('a')
	except :
		if len(list_for_word)!=0:
			for j in list_for_word:
				if j in string :
					candidate=j
					print('b')					
					break
				else :
					candidate='NOT FOUND'
					print('c')
		else :
			candidate='NOT FOUND'
			print('d')
	string_loss=new_list
	print ('candidate :',candidate)
	return(candidate)
class MyGrid(Widget):
	bttn_1=ObjectProperty(None)
	bttn_2=ObjectProperty(None)
	bttn_3=ObjectProperty(None)
	bttn_4=ObjectProperty(None)
	bttn_5=ObjectProperty(None)
	bttn_6=ObjectProperty(None)
	bttn_7=ObjectProperty(None)
	bttn_8=ObjectProperty(None)
	bttn_9=ObjectProperty(None)
	label_main=ObjectProperty(None)
	yes_bttn=ObjectProperty(None)
	no_bttn=ObjectProperty(None)	
	row_1=ObjectProperty(None)
	
	def chk1(self):
		self.label_main.text='pro1'
	def chk2(self):
		self.label_main.text='pro2'
	
	def new(self):
		global string
		global string_win
		global string_win2
		global string_loss
		global string_loss2
		string_loss=string_loss2
		string_win=string_win2
		string=''
		self.label_main.text='Player 1'
		self.bttn_1.text=''
		self.bttn_2.text=''
		self.bttn_3.text=''
		self.bttn_4.text=''
		self.bttn_5.text=''
		self.bttn_6.text=''
		self.bttn_7.text=''
		self.bttn_8.text=''
		self.bttn_9.text=''
		self.bttn_1.color=1,1,1,1
		self.bttn_2.color=1,1,1,1
		self.bttn_3.color=1,1,1,1
		self.bttn_4.color=1,1,1,1
		self.bttn_5.color=1,1,1,1
		self.bttn_6.color=1,1,1,1
		self.bttn_7.color=1,1,1,1
		self.bttn_8.color=1,1,1,1
		self.bttn_9.color=1,1,1,1
	
	def fun_game(self,loc):
		
		def win_declare(s_c):
			if (s_c=='+'):
				self.label_main.text='Player 1 : Wins'
				global file_win
				global string
				file_win.write(string)
				file_win.write('\n')
				string=''
				
			elif (s_c=='o'):
				self.label_main.text='Player 2 : Wins'
				global file_loss
				file_loss.write(string)
				file_loss.write('\n')
				string=''

			elif (s_c=='n'):
				self.label_main.text='Draw'
				file_loss.write(string)
				file_loss.write('\n')
				string=''
		
		def check(s_c):
			if (self.bttn_1.text == self.bttn_2.text == self.bttn_3.text != ''):
				win_declare(s_c)
				self.bttn_1.color =0,1,0,1
				self.bttn_2.color =0,1,0,1
				self.bttn_3.color =0,1,0,1
			elif (self.bttn_4.text == self.bttn_5.text == self.bttn_6.text != ''):
				win_declare(s_c)
				self.bttn_4.color =0,1,0,1
				self.bttn_5.color =0,1,0,1
				self.bttn_6.color =0,1,0,1
			elif (self.bttn_7.text == self.bttn_8.text == self.bttn_9.text != '') :
				win_declare(s_c)
				self.bttn_7.color =0,1,0,1
				self.bttn_8.color =0,1,0,1
				self.bttn_9.color =0,1,0,1
			elif (self.bttn_1.text == self.bttn_4.text == self.bttn_7.text != '') :
				win_declare(s_c)
				self.bttn_1.color =0,1,0,1
				self.bttn_4.color =0,1,0,1
				self.bttn_7.color =0,1,0,1
			elif (self.bttn_2.text == self.bttn_5.text == self.bttn_8.text != '') :
				win_declare(s_c)
				self.bttn_2.color =0,1,0,1
				self.bttn_5.color =0,1,0,1
				self.bttn_8.color =0,1,0,1			
			elif (self.bttn_3.text == self.bttn_6.text == self.bttn_9.text != '') :
				win_declare(s_c)
				self.bttn_3.color =0,1,0,1
				self.bttn_6.color =0,1,0,1
				self.bttn_9.color =0,1,0,1
			elif (self.bttn_1.text == self.bttn_5.text == self.bttn_9.text != '') :
				win_declare(s_c)
				self.bttn_1.color =0,1,0,1
				self.bttn_5.color =0,1,0,1
				self.bttn_9.color =0,1,0,1
			elif (self.bttn_3.text == self.bttn_5.text == self.bttn_7.text != '') :
				win_declare(s_c)
				self.bttn_3.color =0,1,0,1
				self.bttn_5.color =0,1,0,1
				self.bttn_7.color =0,1,0,1
		

		def chng_again():
			global string
			string=string[:-1]
			#print('after poping string: ',string)
			if (self.label_main.text=='Player 1'):
				self.label_main.text='Player 2'
			elif (self.label_main.text=='Player 2'):
				self.label_main.text='Player 1'
		
		def star_circle(loc,s_c):
			global string
			string=string+loc
			#print('after adding string: ',string)
			if loc=='1':
				if (self.bttn_1.text==''):
					self.bttn_1.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='2':
				if (self.bttn_2.text==''):
					self.bttn_2.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='3':
				if (self.bttn_3.text==''):
					self.bttn_3.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='4':
				if (self.bttn_4.text==''):
					self.bttn_4.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='5':
				if (self.bttn_5.text==''):
					self.bttn_5.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='6':
				if (self.bttn_6.text==''):
					self.bttn_6.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='7':
				if (self.bttn_7.text==''):
					self.bttn_7.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='8':
				if (self.bttn_8.text==''):
					self.bttn_8.text=s_c
					check(s_c)
				else :
					chng_again()
			elif loc=='9':
				if (self.bttn_9.text==''):
					self.bttn_9.text=s_c
					check(s_c)
				else :
					chng_again()		
		
		def chng(loc,s_c):
			global string
			if (s_c=='+'):
				self.label_main.text='Player 2'
				star_circle(loc,s_c)
			elif (s_c=='o'):
				self.label_main.text='Player 1'
				star_circle(loc,s_c)
		global string
		#main command
		if (self.label_main.text=='Player 1'):
			s_c='+'
			chng(loc,s_c)
			
		elif (self.label_main.text=='Player 2'):
			# can add sleep command here (time sleep already imported)
			s_c='o'
			chng(loc,s_c)
		def auto_player():
			if self.label_main.text=='Player 2':
				available=['1','2','3','4','5','6','7','8','9'] # it should be created at new  and at starting only 
				new_av=[]
				if self.bttn_1.text!='':
					available[0]=''
				if self.bttn_2.text!='':
					available[1]=''
				if self.bttn_3.text!='':
					available[2]=''
				if self.bttn_4.text!='':
					available[3]=''
				if self.bttn_5.text!='':
					available[4]=''
				if self.bttn_6.text!='':
					available[5]=''
				if self.bttn_7.text!='':
					available[6]=''
				if self.bttn_8.text!='':
					available[7]=''
				if self.bttn_9.text!='':
					available[8]=''
				for i in range(9):
					if available[i]!='':
						new_av.append(available[i])
				print ('list for player 2 :',new_av)
				print ('player 1 location :',loc)
				print ('string :',string)
				if len(new_av)!=0:
					ran_loc_str=choice(new_av) # replace this line with ai code
					candidate=ai_fun(new_av,loc,string)
					if candidate=='NOT FOUND':
						self.fun_game(ran_loc_str)
					else :
						self.fun_game(candidate)
				else :
					win_declare('n')
			elif self.label_main.text=='Player 1':
				available=['1','2','3','4','5','6','7','8','9'] # it should be created at new  and at starting only 
				new_av=[]
				if self.bttn_1.text!='':
					available[0]=''
				if self.bttn_2.text!='':
					available[1]=''
				if self.bttn_3.text!='':
					available[2]=''
				if self.bttn_4.text!='':
					available[3]=''
				if self.bttn_5.text!='':
					available[4]=''
				if self.bttn_6.text!='':
					available[5]=''
				if self.bttn_7.text!='':
					available[6]=''
				if self.bttn_8.text!='':
					available[7]=''
				if self.bttn_9.text!='':
					available[8]=''
				for i in range(9):
					if available[i]!='':
						new_av.append(available[i])
				print ('list for player 1 :',new_av)
				if len(new_av)!=0:
					ran_loc_str=choice(new_av)
					self.fun_game(ran_loc_str)
				else :
					win_declare('n')
		

		auto_player()
		
		
		
	def exit(self,code):
		global file_win
		global file_loss
		file_win.close()
		file_loss.close()
		quit()
		
		
	'''	
		if (code=='ee'):
			crnt_cnd=self.label_main.text
			self.yes_bttn.text='Yes'
			self.no_bttn.text='No'
			self.label_main.text='Are you sure want to exit ?'
		elif (code=='ey'):
			quit()
		elif (code=='en'):
			self.yes_bttn.text=''
			self.no_bttn.text=''
			self.label_main.text=crnt_cnd
			print (crnt_cnd)
			print ('This !')
	'''
# Myapp class imported from Parent class App
class MyApp(App):
	def build(self):
		return MyGrid()
		
# Condition which is mostly alwas true
if __name__=='__main__':
	MyApp().run() 
