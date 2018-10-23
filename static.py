RIGHT = 'right'

LEFT = 'left'

UP = 'up'

DOWN = 'down'

LOSE_TEXT = 'YOU ARE FIRED'

CONSOLAS = 'Consolas'

RIGHT_ANSWER = 'RIGHT ANSWER!'
scale_screen_resolution = (1918, 1074)

bg_images_paths = ['sprites/bg1.png', 'sprites/bg2.png', 'sprites/bg3.png', 'sprites/bg4.png']

hero_sprites_paths = ['sprites/idle_left.png', 'sprites/idle_right.png', 'sprites/run_left_1.png',
                      'sprites/run_left_2.png', 'sprites/run_left_3.png', 'sprites/run_left_4.png',
                      'sprites/run_left_5.png', 'sprites/run_right_1.png', 'sprites/run_right_2.png',
                      'sprites/run_right_3.png', 'sprites/run_right_4.png', 'sprites/run_right_5.png',
                      'sprites/idle_battle.png']

enemies_sprites = ['sprites/enemy0.png', 'sprites/enemy1.png', 'sprites/enemy2.png', 'sprites/enemy3.png',
                   'sprites/enemy4.png', 'sprites/enemy5.png']


def text_hint_1():
    return 'To beat your opponent,'


def text_hint_2():
    return 'you should determine'


def text_hint_3():
    return 'which sequence contains'


def text_hint_4():
    return ' questioned number, if 2 sequences'


def text_hint_5():
    return 'contain number'


def text_hint_6():
    return '- both answers are correct.'


def control_hint_1():
    return 'If you think that questioned number is: '


def control_hint_2():
    return 'Ulam number - press 1.'


def control_hint_3():
    return 'Prime number - press 2.'


def control_hint_4():
    return 'Happy number - press 3.'
