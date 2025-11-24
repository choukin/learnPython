from gun import Gun


class Soldier:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def change_gun(self, new_gun):
        self.gun = new_gun

    def add_gun_bullets(self, bullets_num):
        if self.gun is None:
            print('No gun on me')
            return

        self.gun.add_bullets(bullets_num)

    def fire(self):
        if self.gun is None:
            print('No gun on me')
            return
        if (self.gun.shoot()):
            print('fire in the hole.')
        else:
            print('Fire failed')


if __name__ == '__main__':
    xusanduo = Soldier('xusanduo')
    xusanduo.change_gun(Gun("AK47", 5))
    xusanduo.fire()
    xusanduo.fire()
    xusanduo.fire()
    xusanduo.fire()
    xusanduo.fire()
    xusanduo.fire()
    xusanduo.add_gun_bullets(3)
    xusanduo.fire()
