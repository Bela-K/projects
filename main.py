import random
class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def roll_advantage(self):
        roll1 = self.roll()
        roll2 = self.roll()
        return max(roll1, roll2)
    
    def roll_disadvantage(self):
        roll1 = self.roll()
        roll2 = self.roll()
        return min(roll1, roll2)
    
def main():
    userprompt = str(input("How do you want to roll (eg. 1d6 or 1d20kh1 or 4d6kh3): "))
    if 'd' in userprompt:
        parts = userprompt.split('d')
        number_of_dice = int(parts[0])
        if 'kh' in parts[1]:
            sides_part, keep_part = parts[1].split('kh')
            sides = int(sides_part)
            keep = int(keep_part)
            rolls = [Dice(sides).roll() for _ in range(number_of_dice)]
            rolls.sort(reverse=True)
            result = sum(rolls[:keep])
            print(f"Rolls: {rolls}, Keeping: {rolls[:keep]}, Result: {result}")
        elif 'kl' in parts[1]:
            sides_part, keep_part = parts[1].split('kl')
            sides = int(sides_part)
            keep = int(keep_part)
            rolls = [Dice(sides).roll() for _ in range(number_of_dice)]
            rolls.sort()
            result = sum(rolls[:keep])
            print(f"Rolls: {rolls}, Keeping: {rolls[:keep]}, Result: {result}")
        else:
            sides = int(parts[1])
            rolls = [Dice(sides).roll() for _ in range(number_of_dice)]
            result = sum(rolls)
            print(f"Rolls: {rolls}, Result: {result}")

if __name__ == "__main__":
    main()