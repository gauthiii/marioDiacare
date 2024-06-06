class JumpTrait:
    def __init__(self, entity,dashboard):
        self.verticalSpeed = -12
        self.jumpHeight = 120
        self.entity = entity
        self.dashboard = dashboard
        self.initalHeight = 384
        self.deaccelerationHeight = self.jumpHeight - ((self.verticalSpeed*self.verticalSpeed)/(2*self.entity.gravity))

    def jump(self, jumping):
        if jumping:
            if self.entity.onGround:
                self.entity.sound.play_sfx(self.entity.sound.jump)
                self.entity.vel.y = self.verticalSpeed
                self.entity.inAir = True
                self.initalHeight = self.entity.rect.y
                self.entity.inJump = True
                self.entity.obeyGravity = False  # always reach maximum height
                if self.dashboard.points >= 5:
                    self.dashboard.points -=5
                if self.dashboard.points1 <=2000:
                    self.dashboard.points1 += 100

        if self.entity.inJump:
            if (self.initalHeight-self.entity.rect.y) >= self.deaccelerationHeight or self.entity.vel.y == 0:
                self.entity.inJump = False
                self.entity.obeyGravity = True

    def reset(self):
        self.entity.inAir = False
