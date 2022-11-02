"Draft for game_is_active loop"
# while game_is_active:
# #     print(f'Available Monsters:\nDemon1\nDemon2\nVampire1\n')
# #     print("Available commands:\nStatistics.current_stats(object)\nCreature.attack(target)\nDemon.fireball(target)\nDemon.roar(target)\nVampire.consumption(target)\nInventory.equipment(creature)\nInventory.add_item(creature)\nInventory.use_item(creature)\n")
#     next_action = input("What is Your next action?")
#     if next_action == "Statistics.current_stats(object)": 
#         statistics_input = input("Which object would You like to check?")
#         match statistics_input:
#             case "Demon1":
#                 Statistics.current_stats(Demon1)
#             case "Demon2":
#                 Statistics.current_stats(Demon2)
#             case "Vampire1":
#                 Statistics.current_stats(Vampire1)
#     else: pass

"Printing all methods assigned to object"
# method_list = [metod for metod in dir(Demon1) if not metod.startswith("__")]
# for row in method_list:
#     print(row)

"Adding player"
# adding_players()