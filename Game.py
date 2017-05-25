import sys, pygame
from GameObjects import *
from GameUtil import *
from math import *

### main game class - edit settings

class Game:
  # settings
  _WINDOW_CAPTION = "Game"
  _FPS = 30
  _FPS_DISPLAY = True
  _WIDTH = 320
  _HEIGHT = 320
  _BGCOL = (255, 255, 255)

  # initialization
  _GFX = pygame.display.set_mode((_WIDTH, _HEIGHT))
  pygame.display.set_caption(_WINDOW_CAPTION)
  _CLOCK = pygame.time.Clock()

  _CREATION_QUEUE = []
  _DELETION_QUEUE = []

  _ROOMS = [Room()]
  _ACTIVE_ROOM = _ROOMS[0]

  @staticmethod
  def gameLoop():
    while True:
      # window closed
      for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
      # create queued instances
      for instance in Game._CREATION_QUEUE:
        instance.create()
        Game._ACTIVE_ROOM.entities.append(instance)
      Game._CREATION_QUEUE.clear()
      # update active room
      Game._ACTIVE_ROOM.update()
      # delete queued instances
      for instance in Game._DELETION_QUEUE:
        instance.destroy()
        Game._ACTIVE_ROOM.entities.remove(instance)
      Game._DELETION_QUEUE.clear()
      # draw
      Game._GFX.fill(Game._BGCOL)
      Game._ACTIVE_ROOM.draw()
      pygame.display.update()
      # manage framerate
      Game._CLOCK.tick(Game._FPS);
      if Game._FPS_DISPLAY: print('FPS:', Game._CLOCK.get_fps())

  @staticmethod
  def instanceCreate(instance):
    Game._CREATION_QUEUE.append(instance)

  @staticmethod
  def instanceDestroy(instance):
    Game._DELETION_QUEUE.append(instance)

  @staticmethod
  def gotoRoom(roomNumber):
    Game._ACTIVE_ROOM.roomEnd()
    Game._ACTIVE_ROOM = Game._ROOMS[roomNumber]
    Game._ACTIVE_ROOM.roomStart()
  
  @staticmethod
  def entityExists(entity_class):
    for entity in Game._ACTIVE_ROOM.entities:
      if type(entity) == entity_class:
        return true
    return false

  @staticmethod
  def getEntities(entity_class):
    entities = []
    for entity in Game._ACTIVE_ROOM.entities:
      if type(entity) == entity_class:
        entities.append(entity)
    return entities

### new rooms - inherit from base class

'''
class NewRoom(Room):
  def __init__(self):
    super().__init__()
  def update(self):
    super().update()
  def draw(self):
    super().draw()
  def roomStart(self):
    super().roomStart()
  def roomEnd(self):
    super().roomEnd()
'''

class TestRoom(Room):
  def __init__(self):
    super().__init__()
  def update(self):
    super().update()
  def draw(self):
    super().draw()
  def roomStart(self):
    super().roomStart()
    Game.instanceCreate(TestEntity())
  def roomEnd(self):
    super().roomEnd()

### new entities - inherit from base class

'''
class NewEntity(Entity):
  def __init__(self, x=0, y=0):
    super().__init__(x, y)
  def create(self):
    super().create()
  def update(self):
    super().update()
  def destroy(self):
    super().destroy()
  def draw(self):
    super().draw()
'''

class TestEntity(Entity):
  def __init__(self, x=0, y=0):
    super().__init__(x, y)
  def create(self):
    super().create()
  def update(self):
    super().update()
  def destroy(self):
    super().destroy()
  def draw(self):
    super().draw()

### entry point - add rooms here
if __name__ == '__main__':
  Game._ROOMS.clear()
  # add rooms
  Game._ROOMS.append(TestRoom())
  # set starting room
  Game.gotoRoom(0)
  # start game
  Game.gameLoop()
