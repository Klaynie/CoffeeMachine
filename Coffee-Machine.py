class CoffeeMachine:

    def __init__(self, money, water, milk, beans, cups):
        self.state = "initial"
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups

    def switch_state(self, new_state):
        self.state = new_state

    def set_state_initial(self):
        self.switch_state("initial")

    def set_state_buy(self):
        self.switch_state("buy")

    def set_state_fill(self):
        self.switch_state("fill")

    def set_state_take(self):
        self.switch_state("take")

    def set_state_remaining(self):
        self.switch_state("remaining")

    def set_state_exit(self):
        self.switch_state("exit")

    def __str__(self):
        return "The coffee machine has\n" \
                f"{self.water} of water\n" \
                f"{self.milk} of milk\n" \
                f"{self.beans} of coffee beans\n" \
                f"{self.cups} of disposable cups\n" \
                f"${self.money} of money"

    def user_interaction(self):
        global keep_going
        if self.state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.action_buy()
        elif self.state == "fill":
            self.action_fill()
        elif self.state == "take":
            print(f"I gave you ${self.money}")
            self.money = 0
            self.set_state_initial()
        elif self.state == "remaining":
            print(self)
            self.set_state_initial()
        elif self.state == "exit":
            self.set_state_exit()

    def action_buy(self):
        buy_action = input()
        if buy_action == "back":
            self.set_state_initial()
        else:
            menu_number = int(buy_action)
            if self.check_capcity(menu_number):
                print(buy_messages[0])
                self.buy_item(menu_number)
                self.set_state_initial()

    def check_capcity(self, menu_number):
        capacity_delta = get_capacity_delta(menu_number)
        if self.water - capacity_delta[1] < 0:
                print(buy_messages[1])
                return False
        if self.milk - capacity_delta[2] < 0:
                print(buy_messages[2])
                return False
        if self.beans - capacity_delta[3] < 0:
                print(buy_messages[3])
                return False
        if self.cups - capacity_delta[4] < 0:
                print(buy_messages[4])
                return False
        return True

    def buy_item(self, menu_number):
        capacity_delta = get_capacity_delta(menu_number)
        self.money += capacity_delta[0]
        self.water -= capacity_delta[1]
        self.milk -= capacity_delta[2]
        self.beans -= capacity_delta[3]
        self.cups -= capacity_delta[4]

    def action_fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        self.set_state_initial()

buy_messages = ["I have enough resources, making you a coffee!", 
                "Sorry, not enough water!",
                "Sorry, not enough milk!",
                "Sorry, not enough coffee beans!",
                "Sorry, not enough disposable cups"]

menu = [['espresso',[4, 250, 0, 16, 1]], ['latte',[7, 350, 75, 20, 1]], ['cappucino',[6, 200, 100, 12, 1]]]
keep_going = True

def action_to_prompt(instance, action):
    global keep_going
    if action == "buy":
        instance.set_state_buy()
    elif action == "fill":
        instance.set_state_fill()
    elif action == "take":
        instance.set_state_take()
    elif action == "remaining":
        instance.set_state_remaining()
    elif action == "exit":
        instance.set_state_exit()
        keep_going = False
    coffee_machine.user_interaction()
    return None

def get_capacity_delta(menu_number):
    return menu[menu_number - 1][1]

def coffee_machine_loop():
    global keep_going
    while keep_going:
        action_to_prompt(coffee_machine, input("Write action (buy, fill, take, remaining, exit):"))

coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)
coffee_machine_loop()