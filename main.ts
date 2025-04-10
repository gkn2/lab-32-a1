let greeting = "Hello!"
function change_greeting() {
    
    greeting = "Welcome to the game!"
}

let mySprite = sprites.create(assets.image`mc`, SpriteKind.Player)
change_greeting()
mySprite.say(greeting)
