print(
    r"""
___________.__             ___________                         __    __                  __________      .__               
\__    ___/|  |__   ____   \_   _____/__________  ____   _____/  |__/  |_  ____   ____   \______   \__ __|__| ____   ______
  |    |   |  |  \_/ __ \   |    __)/  _ \_  __ \/ ___\ /  _ \   __\   __\/ __ \ /    \   |       _/  |  \  |/    \ /  ___/
  |    |   |   Y  \  ___/   |     \(  <_> )  | \/ /_/  >  <_> )  |  |  | \  ___/|   |  \  |    |   \  |  /  |   |  \\___ \ 
  |____|   |___|  /\___  >  \___  / \____/|__|  \___  / \____/|__|  |__|  \___  >___|  /  |____|_  /____/|__|___|  /____  >
                \/     \/       \/             /_____/                        \/     \/          \/              \/     \/
      """
)
print(
    r"""
In a land swallowed by time and overgrown by legend, you stand at the edge of something long lost — a forgotten ruin whispered about by only the oldest of travelers. Those who enter seldom return, and those who do are never the same. The choices you make will shape your fate: will you uncover ancient knowledge, awaken a sleeping curse, or vanish into myth like so many before you?

Choose wisely. Every path echoes in the stone halls of the forgotten.

(For all decisions made in the game, respond with the number of the option you wish to select. You will likely have the option of chossing 1, 2 or 3 with every chapter.)

Press [Enter] to begin your journey...
      """
)

# This input tag will simply pause the game and wait for any input from the user to then begin the game
input("")

print("Chapter 1: The Encounter")

chapter_1 = int(
    input(
        "You meet a hooded figure warning of danger ahead. \nHe says, 'Prove your worth, and I may aid you'\nSelect your response:\n\n1. 'I will face any challenge. Test me!'\n2. 'Step aside, old man. I'll find my own way.'\n3. 'Who are you, and why should I trust you?'\n\n"
    )
)

if chapter_1 == 1:
    print(
        r"""
As you wish, answer the following riddle correctly and you will earn a map to the ruins!

I stand when others turn away,        
Face the storm and never sway.
You won’t find me in the loudest cheer,
But in quiet hearts that conquer fear.
What am I?
          """
    )
    decision = input()
    decision.lower()

    if decision == "bravery":
        print(
            "Congratulations, you have answered correctly. Here, you have earned the map that will guide you in your journey!"
        )

        print("You put the map away while you walk away from the figure. He simply turns around and vanishes.\n")
        print("You continue your path.\n\n")
    else: 
        print("You have answered incorrectly. The hooded figure disappears instantly.\n")
        print("You continue your path.\n\n")

elif chapter_1 == 2: 
    print("You have angered the figure greatly and he has vanished. You may proceed blindly.")

elif chapter_1 == 3:
    print("My name is Eron, guardian of this forest.\nI was once cursed by the very ruin you seek.\nBeware for your own greed and desires can very well become your demise.\n\n")

