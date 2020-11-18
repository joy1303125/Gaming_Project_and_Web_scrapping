import random
import simplegui
Computer_score=0
Human_score=0
computer_choice=""#
human_choice=""#ei 2 ta choice die kno function declare kre nai 7-13 no line er code e hcce edr declare kra function
def choice_to_number(choice):
    rps_dict={'rock':0,'paper':1,'scissors':2}
    return rps_dict[choice]
def number_to_choice(number):
    rps_dict={0:'rock',1:'paper',2:'scissors'}
    return rps_dict[number]
def random_computer_choice():
    return random.choice(['rock','paper','scissors'])
def choice_result(human_choice,computer_choice):
    global Computer_score
    global Human_score
    human_number=choice_to_number(human_choice)
    computer_number=choice_to_number(computer_choice)

    if (human_number-computer_number)%3 == 1 :
        print("computer wins!!")
        Computer_score += 1
    elif (human_number == computer_number):
        print('tie.')
    else:
        Human_score += 1
def test_choice_to_number():
    assert choice_to_number('rock')==0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2
def test_number_to_choice():
    assert number_to_choice(0)=='rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'
def test_all():
    test_choice_to_number()
    test_number_to_choice()
test_all()
def rock():#1st e 40-57.then 21-27 condition check ,then hcce 7-12 te hcce 21-27 call kra condition gula onusra element supply kra
    global human_choice,computer_choice
    global Human_score,Computer_score
    human_choice='rock'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)
def paper():
    global human_choice,computer_choice
    global Human_score,Computer_score
    human_choice='paper'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)
def scissors():
    global human_choice,computer_choice
    global Human_score,Computer_score
    human_choice='scissors'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)
def draw(canvas):
    try:
        canvas.draw_text('You:'+  human_choice, [10,40], 48,"Green")
        canvas.draw_text('comp:' + computer_choice, [10, 80], 48, "Red")
        canvas.draw_text("Human_score:"+ str(Human_score),[10,150],30,"Green")
        canvas.draw_text("Computer_score : "+ str(Computer_score),[10,190],30,"Red")
    except Type_error:
        pass
def play_rps():
    frame=simplegui.create_frame("home", 300, 200)
    frame.add_button("rock",rock)
    frame.add_button("paper",paper)
    frame.add_button("scissors",scissors)
    frame.set_draw_handler(draw)
    frame.start()

play_rps()
