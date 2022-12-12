from src.fighters import Fighter


class Arena:
    def __init__(self, number_of_spectators: int, gravity_enabled: bool):
        self.number_of_spectators = number_of_spectators
        self.gravity_enabled = gravity_enabled

    def fight(self, fighter1: Fighter, fighter2: Fighter) -> Fighter:
        print("Fight between {} and {}".format(fighter1.name, fighter2.name))

        import random

        # lets assign a weight of winning to each fighter
        fighter1_weight = 50
        fighter2_weight = 50

        # if the figher has a hat on, add 10% to their chance of winning
        if fighter1.hat:
            fighter1_weight += 10
        if fighter2.hat:
            fighter2_weight += 10

        # if the fighter has armor on, add 20% to their chance of winning
        if fighter1.armor:
            fighter1_weight += 20
        if fighter2.armor:
            fighter2_weight += 20

        # if the body_type is muscular, add 10% to their chance of winning
        if fighter1.body_type == "Muscular":
            fighter1_weight += 10
        if fighter2.body_type == "Muscular":
            fighter2_weight += 10

        # randomly choose between the two fighter weights
        winner = random.choices(
            [fighter1, fighter2], [fighter1_weight, fighter2_weight]
        )

        return winner[0]


if __name__ == "__main__":
    number_of_simulations = 100000
    simulation_outcomes = {}

    for i in range(number_of_simulations):
        arena = Arena(272, gravity_enabled=True)

        ryu = Fighter("Ryu", "Skinny", hat=None, armor=None)
        ken = Fighter("Ken", "Muscular", "Federoa", armor="Steel Plate Armor")

        winner = arena.fight(ken, ryu)

        print("The winner is {}".format(winner.name))

        if winner.name in simulation_outcomes:
            simulation_outcomes[winner.name] += 1
        else:
            simulation_outcomes[winner.name] = 1

    # print some statistics about the simulation
    for fighter_name, number_of_wins in simulation_outcomes.items():
        print("{} won {} times".format(fighter_name, number_of_wins))
        # print as a percentage
        print(
            "{} won {}% of the time".format(
                fighter_name, number_of_wins / number_of_simulations * 100
            )
        )
