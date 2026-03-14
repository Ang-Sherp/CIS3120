def dragon_lair_room(player_info_arg):
    """Dragon Lair Room: a blazing chamber where a dragon guards an ancient relic."""

    print("\nFlames flicker across the walls as you enter the Dragon Lair Room.")

    # --- Update player state ---
    player_info_arg["location"] = "Dragon Lair Room"

    burn_damage = 15
    player_info_arg["health"] -= burn_damage

    player_info_arg["choices"].append("Dragon Lair Room")

    # --- Display current state ---
    show_player_info(player_info_arg)

    # --- Room narrative ---
    print("The heat is overwhelming, and the ground is covered in blackened stone.")
    print("At the center of the chamber, a dragon watches over a glowing relic.")
    print("You can try to calm the dragon, steal the relic, or retreat.")

    action = input("Do you calm the dragon, steal the relic, or retreat? > ").lower()

    if "calm" in action:
        print("You speak softly and lower your head.")
        print("The dragon studies you, then allows you to take a single relic.")

        relic = "Dragon Relic"
        if relic not in player_info_arg["inventory"]:
            player_info_arg["inventory"].append(relic)
            print(f"You obtained the {relic}!")

        return player_info_arg

    elif "steal" in action:
        print("You rush toward the glowing relic.")
        print("The dragon roars and spreads its wings!")
        you_died("The dragon strikes before you can escape")

    elif "retreat" in action:
        print("You decide the risk is too great and step back out of the lair.")
        return "flee"

    else:
        print("Your uncertainty angers the dragon.")
        print("You stumble backward and escape the room.")
        return "flee"
