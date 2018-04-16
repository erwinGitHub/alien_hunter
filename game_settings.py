class Settings():
    """\class which is used to store all game settings"""
    
    def __init__(self):
        """Settings initiaton"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_title = "aliens"

        #Background settings
        self.background_image = "images/space.jpg"
        
        #Ship settings
        self.ship_image = "images/xwing.png"
        self.ship_speed_factor = 2
        
        #Bullet settings
        self.bullet_speed_factor = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 200, 200
        
        #Alien ship settings
        self.alien_image = "images/alien.png"
        
