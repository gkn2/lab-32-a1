greeting = "Hello!"  


def change_greeting():
    global greeting  
    greeting = "Welcome to the game!"  



mySprite = sprites.create(assets.image("""mc"""), SpriteKind.player)



change_greeting()  

mySprite.say(greeting)  


