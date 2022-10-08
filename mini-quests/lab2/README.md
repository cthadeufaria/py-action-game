# "Dragon's Bane" (mini-quest II)

### Running the game
 - Clone this repository, and make sure you have [Python 3](https://www.python.org/) installed
 - Execute `python3 main.py` on a terminal

The script only depends on standard Python libraries.

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0-standalone.html)

### Context

> The plot thickens...
>
> "You just tapped your way through a damp corridor, following a draft until a sturdy shut door. The poorly lit doorway reveals a charred knob where a dim light protrudes through an obfuscated keyhole. You try to pry the door open, to no avail. There must be a way to unlock this door. You press onward along the faintly lit walkway, trying not to lose your bearings until heavy breathing halts you...Something or someone is alive in here...with you...the moment you take a turn, the sight before you has you gasping for air, as a surge of primal fear paralyses you...its...its a dragon. 
>
> Although snuggled and asleep, nothing would prepare you for such an encounter, as his scales sparkly reflect the dimness of the ambient light, revealing his imposing body, almost blocking the entire passage. But the crackly snap of hopelessness hits you when you spot another shiny object, hanging from his neck: a key. Surely, to the door. Undoubtedly, such an indomitable creature would not surrender his key on a mere request. Maybe you can snatch the key without waking the foul beast...
>
> But you need something to cut the necklace that holds the key...you carefully trace back your steps, and begin burrowing and scavenging throughout the passageways, trying to find something that might have been left behind by some other lost adventurer. Suddenly, you notice another dim sparkling light from a pile of rubble...as you move closer, you feel a foul stench of rotten and putrid flesh...amidst the rubble, there is a corpse of a humanoid creature you cannot recognise. The smell is so bad, you barely dare to touch the remains, but the shiny light draws you to push the corpse aside...its...its....a sword!
>
> Praise the Gods! What a holy gift! Not even in your most wild expectations would you expect to find such a valuable item. The sword is sturdy, long and seems robust. Oddly enough it does not seem rusty at all...as if it had always been there for you to find it. Luckily, it appears to be quite sharp...cutting that key off the dragon should be sweet...Hopeful, you hustle back to where the dragon was, careful enough not to reveal your presence, and take a careful look over the corner at the sleeping....wait...where is he??!... Oh no!! IT'S AWAKE!!!...
>
> Note: You are supposed to reuse the results from mini-quest I and evolve them.

---

***Task #1. "Refactoring" to Objects.***

For your programming solution to grow in a sustainable manner, you must now prepare the code for the accommodation of the next features. Therefore, you are going to "refactor" your code, by separating concerns and responsibilities into classes. Therefore, perform the following tasks:

 * Separate user interaction from game logic. Create two separate packages(Java)/namespaces(C++), one containing the class(es) for user input, for example: dkeep.cli (command-line interface), and another containing the classes for the game logic, for example: dkeep.logic. This separation will allow, in the future, to have multiple ways of using/running the game logic code: through the command-line interface, through automatic unit tests, or through a graphical user interface.


 * User interaction package/namespace internals. The user interaction package/namespace should have, at least, one class with the main method entry point and possible auxiliary methods for handling input. It is recommended to place the "game loop/cycle" in this package/namespace. The game "loop" consists of: continuously asking the user to enter a command; running the game logic accordingly (to that command) and updating the game state; printing the game screen; until the game is over (hero dies or wins). 


 * Game logic package/namespace internals. This package/namespace should have, at least, the following classes (with attributes private or protected, and non-static):

   * A class to represent the state of the game, storing the current map and the game elements (hero, dragon, sword, etc.). It should provide an API (constructors and public methods), to be used by the user interaction package/namespace to, at least: instantiate a new game, issue a hero's movement action, check the game state (game over?), get the map in order to print it (e.g., using toString might be a possibility or a similar C++ counterpart);

   * A class to represent the current map. 

   * Several classes to represent the game elements that might be present within the game level (hero, dragon, ...) and their status. These should have a super-class with the common properties (coordinates, etc.), exploiting inheritance and polymorphism accordingly (having the specific behaviour of each game element in its respective class). 
   
***Task #2. Advanced Game Logic***

a) Change the basic game logic, so that instead of a key, there is a sword ('S'). The hero needs to slay the dragon in order to get the key to open the exit door. When the hero picks the sword, his/her representation changes from 'H' to 'A' (meaning "Armed"). If the hero reaches any of the dragon's adjacent positions while armed, the dragon dies, otherwise, (unarmed) the hero dies. Therefore the hero needs to pick the sword first, then kill the dragon, and only then he/she is allowed to go through the exit. 

b) The dragon is now awake and moves one position in a random direction, every time the hero moves. It must be a valid movement direction (e.g. the dragon must progress through the corridor, and not hit the wall and stay there). As such, when the user enters a moving command for the hero, both hero and dragon move (hero first, dragon next). You should check the game logic (win/lose situation) at every game element move. For example: (1) User enters a command, (2) hero moves, (3) game logic checks win/lose status (if hero just moved next to the dragon; is armed or not; is the hero going through the exit; has the dragon been slain, etc...), (4) if the game is still not over then move dragon, (5) check game logic again, (6) if the game still not over, go back to (1). The dragon cannot pick the sword if he steps over it, but his representation changes to 'F' (while he is in the same position as the sword). Leaving that position, and everything reverts back to normal ('D' for the dragon and 'S' for the sword). The dragon can never go through the exit.

c) There are now multiple dragons, all scattered across the map. All dragons move in the same fashion, and the hero must slay all in order to leave through the exit. You must ask the user how many dragons will there be, before starting the game. Rule: You must use a proper java collection or c++ standard library structure to solve this issue.

d) Create a new moving strategy for the dragon where he can move diagonally through ("cuts") corners. Hint: generate the next two valid dragon movements and check if they are "corners". (only four possibilities). If so, move directly to the second position. 

Good luck!
