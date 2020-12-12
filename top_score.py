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


def sing(num_bottles):
    #TODO: Add your code to achieve the desired output and pass the challenge. 
    #NOTE: The f String method of String Interpolation does not work. 
    list=[]
    for i in range(num_bottles,0,-1):
        list.append('{i} bottles of beer on the wall {i} bottles of beer.'.format(i=i))
        list.append('Take one down and pass it around {i} bottles on the wall.'.format(i=i-1))
        list.append('')
    print(list)


sing(99)


def square_root(x):
    return math.sqrt(x)


nums = [43,12,6,78,14]
chars = ['a','t,','k']

concat = nums + chars
print(concat)
print(square_root(64))
nums.sort()
print(top_three(nums))