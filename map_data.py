import pygame

level_5_bg = pygame.image.load('data/images/level_5.png')
level_4_bg = pygame.image.load('data/images/level_4.png')
level_1_bg = pygame.image.load('data/images/level_1.png')
level_2_bg = pygame.image.load('data/images/level_2.png')
level_3_bg = pygame.image.load('data/images/level_3.png')

mazes = [
    {'blocks':[(0, 440, 320, 160)
    ,(480, 440, 320, 160)
    ,(320, 560, 160, 40)
    ,(0, 0, 40, 440)
    ,(40, 0, 760, 40)
    ,(760, 40, 40, 560)
    ,(80, 360, 280, 40)
    ,(440, 360, 280, 40)
    ,(80, 80, 40, 60)
    ,(80, 280, 40, 80)
    ,(680, 80, 40, 60)
    ,(600, 280, 120, 80)
    ,(120, 80, 200, 40)
    ,(480, 80, 200, 40)
    ,(280, 120, 40, 40)
    ,(480, 120, 40, 40)
    ,(360, 200, 80, 40)
    ,(440, 280, 40, 40)
    ,(320, 120, 160, 40)
    ,(320, 280, 40, 40)
    ,(120, 280, 80, 80)
    ,(240, 120, 40, 40)
    ,(80, 80, 200, 80)
    ,(80, 200, 200, 40)
    ,(240, 280, 120, 40)
    ,(240,200,80,80)
    ,(40,200,40,40)
    ,(440, 120, 280, 40)
    ,(480, 200, 240, 40)
    ,(480, 240, 80, 80)
    ,(720, 200, 40, 40)
    ,(360,360,80,40)
             ],
         'start': (390,500),
         'finish': (370,50),
         'image': level_1_bg
         },
    {'blocks':[(0, 0, 420, 40)
    ,(80, 80, 280, 120)
    ,(0,40,40,400)
    ,(0, 400, 150, 110)
    ,(0, 560, 560, 40)
    ,(200, 510, 60, 50)
    ,(560, 560, 240, 40)
    ,(420, 0, 100, 270)
    ,(520, 0, 280, 50)
    ,(360, 330, 90, 170)
    ,(150, 400, 220,40)
    ,(320,200,40,200)
    ,(760,40,40,520)
    ,(450, 450, 250, 50)
    ,(660,100,40,350)
    ,(500, 180, 40, 40)
    ,(590, 180, 70, 40)
    ,(500, 220, 40, 120)
    ,(540,300,65,40)
    ,(0,510,40,50)
             ],
         'start': (50,530),
         'finish': (260,340),
         'image': level_2_bg
     
     },
    {'blocks':[(0, 0, 800, 40)
    ,(0, 40, 40, 560)
    ,(760, 40, 40, 560)
    ,(40, 560, 760, 40)
    ,(120, 115, 80, 325)
    ,(160, 440, 40, 120)
    ,(200, 115, 480, 45)
    ,(680, 115, 30, 400)
    ,(260, 475, 425, 40)
    ,(260, 205, 320, 40)
    ,(260, 215, 45, 280)
    ,(580, 205, 55, 200)
    ,(634, 405, -288, 30)
    ,(345, 405, 40, -124)
    ,(385, 280, 120, 35)
    ,(505, 280, 37, 89)],
         'start': (65,525),
         'finish': (415,350),
         'image': level_3_bg
     },
    {'blocks':[(0, 0, 40, 600)
    ,(40, 0, 600, 40)
    ,(120, 0, 40, 120)
    ,(80, 80, 40, 40)
    ,(0, 240, 120, 40)
    ,(80, 160, 80, 40)
    ,(80, 320, 120, 40)
    ,(160, 280, 40, 40)
    ,(80, 400, 120, 40)
    ,(160, 440, 120, 40)
    ,(240, 480, 40, 40)
    ,(160, 480, 40, 120)
    ,(0, 560, 800, 40)
    ,(760, 80, 40, 480)
    ,(720, 80, 40, 40)
    ,(320, 440, 80, 80)
    ,(240, 320, 40, 80)
    ,(200, 200, 40, 80)
    ,(240, 240, 120, 40)
    ,(320, 280, 40, 120)
    ,(360, 360, 80, 40)
    ,(320, 40, 40, 160)
    ,(280, 120, 40, 80)
    ,(240, 80, 40, 80)
    ,(200, 120, 40, 40)
    ,(440, 480, 40, 80)
    ,(480, 520, 120, 40)
    ,(400, 240, 40, 80)
    ,(400, 80, 40, 120)
    ,(440, 80, 40, 40)
    ,(520, 80, 40, 80)
    ,(560, 120, 40, 40)
    ,(480, 160, 40, 80)
    ,(520, 200, 80, 40)
    ,(480, 280, 80, 40)
    ,(480, 320, 40, 40)
    ,(480, 360, 200, 40)
    ,(440, 400, 80, 40)
    ,(520, 440, 40, 40)
    ,(640, 400, 40, 40)
    ,(600, 440, 120, 40)
    ,(640, 480, 40, 40)
    ,(720, 520, 40, 40)
    ,(600, 40, 40, 80)
    ,(640, 80, 40, 120)
    ,(680, 160, 40, 160)
    ,(640, 240, 40, 80)
    ,(600, 280, 40, 40)
    ,(720, 360, 40, 40)],
         'start': (50,500),
         'finish': (730,15),
         'image': level_4_bg
         },
    { 'blocks':[(0, 0, 800, 40),
    (0, 40, 40, 600),
    (40,560,760,40),
    (140,100,40,460),
    (40,410,50,30),
    (90,300,50,30),
    (40,40,50,200),
    (240,40,40,480),
    (340,420,40,140),
    (280,320,400,40),
    (450,360,40,150),
    (550,420,40,140),
    (640,360,40,150),
    (760,0,40,560),
    (325, 225, 500, 40),
    (280, 140, 380, 40),
    (520, 40, 40, 100)
        ],
         'start': (50,520),
         'finish': (570,80),
         'image': level_5_bg
     }
         
         ]