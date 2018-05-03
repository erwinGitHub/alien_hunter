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
        self.ship_speed_factor = 3.5
        self.initial_ammo = 40
        self.ammo = self.initial_ammo
        self.ship_images = ["images/xwing.png",
                                "images/exp1.png", 
                                "images/exp2.png", 
                                "images/exp3.png", 
                                "images/exp4.png", 
                                "images/exp5.png", 
                                "images/exp6.png", 
                                "images/exp7.png", 
                                "images/exp8.png", 
                                "images/exp9.png", 
                                "images/exp10.png"] 
       
        
        #Bullet settings
        self.bullet_speed_factor = 5.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 200, 200
        
        #Alien ship settings
        self.alien_speed_factor = 4
        self.alien_drop_factor = 100
        self.alien_images = ["images/alien.png",
                                "images/exp1.png", 
                                "images/exp2.png", 
                                "images/exp3.png", 
                                "images/exp4.png", 
                                "images/exp5.png", 
                                "images/exp6.png", 
                                "images/exp7.png", 
                                "images/exp8.png", 
                                "images/exp9.png", 
                                "images/exp10.png"] 
                
