#!/usr/bin/python
import re
#re_data=re.compile(r'^\d{4}-\d{2}-\d{2}$')	
class meeting(object):
	attend_list=[]
		
	def __init__(self):
		self.user={}
		self.root={}
		self.meeting=[]
		self.comments=[]
			
	def registration(self,name,password,quanxian='user'):
		if quanxian=='root':
			if name in self.root:
				print 'root ID has been used,try another one..'
				return False
			elif len(name)>8 or len(name)<5:
				print 'root ID must beetwen 5-8'
				return False
			self.root[name]=password
			return True	
		else:
			if name in self.user:
				print 'user ID has been used,try another one..'
				return False
			elif len(name)>8 or len(name)<5:
				print 'user ID must beetwen 5-8'
				return False
			self.user[name]=password
			return True
	def login(self,uid,password,quanxian='user'):
		if quanxian=='root':
			for x,y in self.root.iteritems():
				if x==uid and y==password:
					print 'ROOT %s Login...'% uid
					return True
		else:
			for x,y in self.user.iteritems():
				if x==uid and y==password:
					print 'User %s Login...'% uid
					return True
	
	def release_meeting(self,uid,password,data,types):
		if self.login(uid,password):
			message=data,uid,types
			return self.meeting.append(message)

	def attend_meeting(self,uid,password,data,promoter,types):
		message=data,promoter,types
		if self.login(uid,password):
			for i in self.meeting:
				if message==i:
					return meeting.attend_list.append((uid,i))

	def meeting_release(self,uid,password):
		print '%s release conference list: '%uid
		if self.login(uid,password):
			for i in self.meeting:
				if uid in i:
					print i

	def meeting_attend(self,uid,password):
		print '%s attend conference list: '%uid
		if self.login(uid,password):
			for i in meeting.attend_list:
				if uid in i:
					print i[-1]		
		
	def query_participants(self,uid,password,data,promoter,types):
		message=data,promoter,types
		numbers=0
		if self.login(uid,password):
			for i in meeting.attend_list:	
				if message in i:
					numbers=numbers+1
					print i[0]	
		print 'A total of %s people attended the meeting' % numbers	
	
	def add_comments(self,uid,password,data,promoter,types,comments):
		message=data,promoter,types
		mark=[message,uid,comments]
		if self.login(uid,password):	
			for i in self.meeting:
				if message==i:
					return self.comments.append(mark) 
	
	def query_comments(self,uid,password,data,promoter,types):
		message=data,promoter,types
		for i in self.comments:
			if message in i:
				cid=i[1]
				com=i[-1]
				print cid+' :'+com			
	
	def query_user(self):
		return self.user
	def query_root(self):
		return self.root

a=meeting()
#a.registration('wangchao','123','root')
a.registration('wangchao','123')
a.registration('lijianxi','234')
a.registration('sunzchao','123')
a.registration('housiwen','123')
#print a.query_root()
a.release_meeting('wangchao','123','2016-01-01','workshop')
a.release_meeting('wangchao','123','2016-11-01','debate')
a.release_meeting('lijianxi','234','2015-12-12','forum')
a.release_meeting('lijianxi','234','2015-08-23','lecture')
#a.query_meeting('wangchao')
#a.query_meeting('lijianxi')
a.attend_meeting('wangchao','123','2016-01-01','wangchao','workshop')
a.attend_meeting('sunzchao','123','2016-01-01','wangchao','workshop')
a.attend_meeting('lijianxi','234','2016-01-01','wangchao','workshop')
a.attend_meeting('housiwen','123','2016-01-01','wangchao','workshop')
#a.meeting_release('wangchao','123')
#a.meeting_attend('wangchao','123')
#a.meeting_attend('lijianxi','234')
#print meeting.attend_list
#print a.meeting
#a.query_participants('wangchao','123','2016-01-01','wangchao','workshop')
a.add_comments('wangchao','123','2016-01-01','wangchao','workshop','This is a great meeting!')
a.add_comments('lijianxi','234','2016-01-01','wangchao','workshop','Nice meeting!')
a.add_comments('sunzchao','123','2016-01-01','wangchao','workshop','Lunnch is delicious..')
a.add_comments('housiwen','123','2016-01-01','wangchao','workshop','Boring..')
a.query_comments('wangchao','123','2016-01-01','wangchao','workshop')
