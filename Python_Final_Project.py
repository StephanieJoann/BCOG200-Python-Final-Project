import tkinter as tk 
from tkinter import ttk
import os
import time
import random
import sys
#imports required modules 


class RumiMind: # defines class RumiMind

	def __init__(self): # defines attributes of class RumiMind
		# creates the application window
		# size of the screen 
		self.window = tk.Tk()
		self.window.geometry("800x600")
		self.canvas = tk.Canvas()
		self.canvas.pack()
		# creates screen index		
		self.current_screen_indx = 0
		self.screen_type_list = ['instructions', 'instructions', 'instructions', 'image_condition']
		# this imports text files of instructions to the instruction file list
		self.instruction_counter = 0
		self.instruction_file_list = ['instructions/instructions1.txt', 'instructions/instructions2.txt', 'instructions/instructions3.txt']
		self.instructions_text_list = []
		self.instructions = None
		# imports images...
		self.image_dict = {}
		self.image_counter = 0
		self.image_list = ['images/baby_7.png', 'images/baby_8.png']

		self.image_stimulus = None

		self.trial_number = 1
		self.probe1_responses = []
		self.probe2_responses = []

		self.load_images()
		self.load_instructions()
		self.next_screen()

	
	def load_instructions(self): # this opens the instruction text file list and appends it
		for filename in self.instruction_file_list:
			f = open(filename)
			new_instructions = ""
			for line in f:
				new_instructions += line
			self.instructions_text_list.append(new_instructions)
			f.close()
		
	def load_images(self): # this loads our images
		for filename in self.image_list:
			new_image = tk.PhotoImage(filename) # created a tkinter image object
			self.image_dict[filename] = new_image 

	def show_instructions(self): # this shows and destroys instructions as needed
			if self.instructions is not None:
				self.instructions.destroy()
				self.next_button.destroy()
			
			self.instructions = tk.Label(self.canvas, text=self.instructions_text_list[self.instruction_counter])
			self.instruction_counter += 1
			self.instructions.pack()

			self.next_button = tk.Button(self.canvas, text="Next", command=self.next_screen)
			self.next_button.pack()
			# self.next_button.place(x=558, y =279)
			# self.instructions.place(x=600, y=100, anchor='center')

	def image_condition(self): # this goes through the three instructions one by one and destroys the previous one
		self.next_button.destroy()
		if self.instructions is not None:
			self.instructions.destroy()
		if self.image_stimulus is not None:
			self.image_stimulus.destroy()
		
		for self.trial_number in range(3): # creates fixation cross and sets timing for that stimulus. Then it will destroy and produces probe 1
			print(self.trial_number)

			# print("Showing Stimulus")
			self.image_stimulus = tk.Label(self.canvas, text='+', font=("Helvetica", 32))
			self.image_stimulus.pack()
			# print('GET OUT')
			self.window.update()

			# print('I AM A MONSTER')
			self.probe_time = random.uniform(PROBE_MIN_TIME, PROBE_MAX_TIME)
			time.sleep(self.probe_time)

			print("Showing Probe 1")
			self.probe1_done = False
			self.image_stimulus.destroy()
			self.probe1_stimulus = tk.Label(self.canvas, text="Was your focus on task or off task")
			self.probe1_stimulus.pack()
			self.on_task_button = tk.Button(self.canvas, text="On task", command=self.on_task)
			self.off_task_button = tk.Button(self.canvas, text="Off task", command=self.off_task)
			self.on_task_button.pack()
			self.off_task_button.pack()
			self.window.update()
			# print("but where did the lighter fluid come from")

			while not self.probe1_done: # while probe1_done is true, update window 
				# print('hey brother')
				self.window.update()

			# print(self.on_task)

			# destroys image stimulus and buttons 
			self.image_stimulus.destroy()
			self.probe1_stimulus.destroy()
			self.on_task_button.destroy()
			self.off_task_button.destroy()
			self.window.update()

			time.sleep(.5)
			self.probe2_done = False
			
			if self.on_task == False:
				print("Showing Probe 2")
				self.probe2_stimulus = tk.Label(self.canvas, text="Was your focus positive, negative, or neutral?") # creates question
				self.probe2_stimulus.pack()
				self.positive_button = tk.Button(self.canvas, text="Positive", command=self.positive_focus) # creates positive button
				self.negative_button = tk.Button(self.canvas, text="Negative", command=self.negative_focus) # creates negative button
				self.neutral_button = tk.Button(self.canvas, text="Neutral", command=self.neutral_focus) # creates neutral button
				self.positive_button.pack() # aligns buttons
				self.negative_button.pack() # aligns buttons
				self.neutral_button.pack() # aligns buttons
				self.window.update()

				while not self.probe2_done: # updates window when probe2_done is not True
					self.window.update()

				print("pressed one of the 3 buttons")

				self.probe2_stimulus.destroy()
				self.positive_button.destroy()
				self.negative_button.destroy()
				self.neutral_button.destroy()
				self.window.update()

		# self.output_data()
		sys.exit()

	#### Trying to save the output data here 
	# def output_data(self):
		# f = open('probe1_data.txt', "w+")
		# f = open("probe1_data.txt", "a")
		# probe1_data.txt.append(probe1_responses)
		# f.close()

		# f = open('probe2_data.txt', "w+")
		# f.write(probe2_data.txt.self.probe1_responses)
		# 	# f.write('probe2_data.txt')
		# f.close()
		
		

	def on_task(self): # encodes user responses to probe1_responses for the on task button if condition is met
		response_tuple = (self.trial_number, self.probe_time, 1)
		self.probe1_responses.append(response_tuple)
		self.on_task = True
		self.probe1_done = True
		# print("there is always money in the banana stand")
		# print(self.on_task, self.probe1_done)

	def off_task(self): # encodes user responses to probe1_responses for the off task button if condistion is met
		response_tuple = (self.trial_number, self.probe_time, 0)
		self.probe1_responses.append(response_tuple)
		self.on_task = False
		self.probe1_done = True
		# print(self.on_task, self.probe1_done)

	def positive_focus(self): # encodes user responses to probe2_responses for the positive focus button if condition is met
		response_tuple = (self.trial_number, self.probe_time, 0)
		self.probe2_responses.append(response_tuple)
		self.pressed_positive_button = True
		self.pressed_negative_button = False
		self.pressed_neutral_button = False
		self.probe2_done = True

	def negative_focus(self): # encodes user responses to probe2_responses for the negative focus button if condition is met
		response_tuple = (self.trial_number, self.probe_time, 1)
		self.probe2_responses.append(response_tuple)
		self.pressed_positive_button = False
		self.pressed_negative_button = True
		self.pressed_neutral_button = False
		self.probe2_done = True
	
	def neutral_focus(self): # encodes user responses to probe2_responses for the neutral focus button if condition is met
		response_tuple = (self.trial_number, self.probe_time, 2)
		self.probe2_responses.append(response_tuple)
		self.pressed_positive_button = True
		self.pressed_negative_button = False
		self.pressed_neutral_button = True
		self.probe2_done = True

	def next_screen(self): # iterates through the current screen, instructions, and condition
		current_screen = self.screen_type_list[self.current_screen_indx]

		if current_screen == 'instructions':
			self.show_instructions()

		elif current_screen == 'image_condition':
			self.image_condition()

		self.current_screen_indx += 1


EXPERIMENT_TIME = 5
PROBE_MIN_TIME = 0.5
PROBE_MAX_TIME = 3
#logistics for timing


if __name__ == "__main__":
	my_experiment = RumiMind()
	my_experiment.window.mainloop()
# this is the main loop that calls our previously made functions

	
