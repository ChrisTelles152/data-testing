import universe
import gym
import random

#reinforcement learning step
def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
	#for every 15 iterations, sum the total observations and take the average
	#if lower than 0, change direction
	#if we go 15+ iterations and get a reward each step, we're doing somethin right
	#that's when we turn

	if(j >= 15):
		turn = True
	else:
		turn = False

		#reset vars
		total_sum = 0
		

def main():
	env = gym.make('flashgames.CoasterRacer-v0')
	observation_n = env.reset()
	
	# initialize environment
	# number of iterations
	n = 0
	j = 0

	# sum of observations
	total_sum = 0
	prev_total_sum = 0
	turn = False

	# define keyboard actions
	left = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowLeft', True),('KeyEvent', 'ArrowRight', False)]
	right = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowLeft', False),('KeyEvent', 'ArrowRight', True)]
	forward = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowLeft', False),('KeyEvent', 'ArrowRight', False)]

	# main logic
	while True:
		#increment counter for number of iterations
		n+=1

		#if at least one iteration is made, check if turn is needed
		if (n>1):
			#if at least one iteration, check if a turn
			if(observations_n[0] != None):
				#store the reward in the previous score
				prev_score = reward_n[0]

				if(turn):
					#pick a random event
					#where to turn?
					event = random.choice(left,right)
				
					#perform action
					action_n = [event for ob in observation_n]

		elif(~turn):
			#if no turn is needed, go straight
			action_n = [forward for ob in observation_n]

		#if there is an observation, game has started, check if turn is needed
		if(observation_n[0] != None):
			turn, j, total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])

		#save new variables for each iteration
		observation_n, reward_n, info = env.step(action_n)
		env.render()

if name == '__main__':
	main()			
