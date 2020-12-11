import math
def top_three(scores):
    #scores = scores
    top_scores = []
    scores.sort()
    top_scores.append(scores.pop())
    top_scores.append(scores.pop())
    top_scores.append(scores.pop())
    return top_scores

tracker=0
def move_forward():
    global tracker
    tracker +=1
    print('moving forward by one step')

def turn_right():
    global tracker
    tracker -=1
    print('turning right')

def square_root(x):
    return math.sqrt(x)
def move():
    move_forward()
    turn_right()
    turn_right()
    turn_right()
    turn_right()
    turn_right()
    turn_right()
    move_forward()
    turn_right()
    move_forward()
    return tracker

print(move())

nums = [43,12,6,78,14]
chars = ['a','t,','k']

concat = nums + chars
print(concat)
print(square_root(64))
nums.sort()
print(top_three(nums))