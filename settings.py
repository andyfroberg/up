class Settings:
    # Game Setup
    SCREEN_RESOLUTION = (700, 500)  # (width, height)
    FPS = 60  # Frames per second
    PIXEL_SCALE = 64
    SPRITE_SCALE = 1

    # Game Difficulty
    # GAME_DIFFICULTY = GameDifficulty.NORMAL

    # Player Stats
    PLAYER_START_X = 2
    PLAYER_START_Y = 2
    PLAYER_START_ANGLE = 0
    PLAYER_SPEED = 0.05
    PLAYER_BOUNDING_RECT = 0.25

    # Dungeon Character Stats

    # Room Settings
    ROOM_MIN_WIDTH = 3
    ROOM_MIN_HEIGHT = 3
    ROOM_MAX_WIDTH = 14
    ROOM_MAX_HEIGHT = 8
    OPEN_FLOOR = 0
    BRICK_WALL = 1
    DOOR = 2
    ROCK = 3
    OGRE = 4