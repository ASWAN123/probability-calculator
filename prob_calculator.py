import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self , **kwargs):
		self.contents = list()
		for  key , value  in kwargs.items():
			for n  in range(value):
				self.contents.append(key)
		# print(self.contents)
		
	def draw(self , number):
		try:
			balls=random.sample(self.contents,number)
			for  ele  in balls:
				self.contents.remove(ele)
			return balls
		except:
			return self.contents

def experiment( hat , expected_balls, num_balls_drawn, num_experiments):

	M = 0
	for n in range(num_experiments):
		# format  the  list  again 
		balls_todraw = []
		for  key , value  in expected_balls.items():
			for n  in range(value):
				balls_todraw.append(key)
		# draw from hat class with  method deepcopy
		balls_copy = copy.deepcopy(hat)
		balls_list =balls_copy.draw(num_balls_drawn)
		cool = True 
		for  each  in  balls_todraw:
			if  each  in  balls_list:
				balls_list.remove(each)
			else:
				cool = False 
				break 
		if cool:
			M+=1
	return  M/num_experiments




