class Fighter:
    def __init__(self, name: str, body_type: str, hat, armor) -> None:
        self.name = name
        self.body_type = body_type
        self.hat = hat
        self.armor = armor


if __name__ == "__main__":
    fighter1 = Fighter("Ryu", "Muscular", "Red", armor="None")
    fighter2 = Fighter("Ken", "Muscular", "Blue", armor="None")

    print(fighter1.name)
    print(fighter1.body_type)

    print(fighter2.name)
    print(fighter2.body_type)
