RIGHT = 'right'

LEFT = 'left'

UP = 'up'

DOWN = 'down'

LOSE_TEXT = 'YOU ARE FIRED'

BOSS_IMAGE_PATH = 'sprites/boss.png'

BATTLE_IMAGE_PATH = 'sprites/battle.png'

BATTLE_BG_IMAGE_PATH = 'sprites/battle_bg.jpg'
CONSOLAS = 'Consolas'
enemies_names = [['AttributeError', 'NameError', 'AttributeError'], ['KeyError', 'TypeError', 'AttributeError'],
                 ['KeyError', 'AttributeError', 'TypeError'], ['Can\'t run on battery']]
RIGHT_ANSWER = 'RIGHT ANSWER!'
scale_screen_resolution = (1918, 1074)

bg_images_paths = ['sprites/bg1.png', 'sprites/bg2.png',
                   'sprites/bg3.png', 'sprites/bg4.png']

hero_sprites_paths = ['sprites/idle_left.png', 'sprites/idle_right.png', 'sprites/run_left_1.png',
                      'sprites/run_left_2.png', 'sprites/run_left_3.png', 'sprites/run_left_4.png',
                      'sprites/run_left_5.png', 'sprites/run_right_1.png', 'sprites/run_right_2.png',
                      'sprites/run_right_3.png', 'sprites/run_right_4.png', 'sprites/run_right_5.png',
                      'sprites/idle_battle.png']

enemies_sprites = ['sprites/enemy0.png', 'sprites/enemy1.png', 'sprites/enemy2.png', 'sprites/enemy3.png',
                   'sprites/enemy4.png', 'sprites/enemy5.png']


def text_hint_1():
    """
    None -> str
    Returns the following string 'To beat your opponent,'
    """
    return 'To beat your opponent,'


def text_hint_2():
    """
    None -> str
    Returns the following string 'you should determine'
    """
    return 'you should determine'


def text_hint_3():
    """
    None -> str
    Returns the following string 'which sequence contains'
    """
    return 'which sequence contains'


def text_hint_4():
    """
    None -> str
    Returns the following string 'questioned number, if 2 sequences'
    """
    return ' questioned number, if 2 sequences'


def text_hint_5():
    """
    None -> str
    Returns the following string 'contain number'
    """
    return 'contain number'


def text_hint_6():
    """
    None -> str
    Returns the following string '- both answers are correct.'
    """
    return '- both answers are correct.'


def control_hint_1():
    """
    None -> str
    Returns the following string 'If you think that questioned number is: '
    """
    return 'If you think that questioned number is: '


def control_hint_2():
    """
    None -> str
    Returns the following string 'Ulam number - press 1.'
    """
    return 'Ulam number - press 1.'


def control_hint_3():
    """
    None -> str
    Returns the following string 'Ulam number - press 2.'
    """
    return 'Prime number - press 2.'


def control_hint_4():
    """
    None -> str
    Returns the following string 'Ulam number - press 3.'
    """
    return 'Happy number - press 3.'
