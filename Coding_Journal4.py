class Goose:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length #float
        self.leg_length = leg_length #float
        self.num_eyes = num_eyes #int
        self.has_tail = has_tail #bool
        self.is_furry = is_furry #bool
    def describe(self):
        print("Goose\'s Physical Characteristics:")
        print(f"Arm length: {self.arm_length} (Geese have wings, not arms)")
        print(f"Leg length: {self.leg_length}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry: {'Yes' if self.is_furry else 'No'} (Geese have feathers)")
def main():
    my_goose = Goose(
        arm_length=0.0, 
        leg_length=10.0,
        num_eyes=2,
        has_tail=True,
        is_furry=False
    )
    my_goose.describe()
main()