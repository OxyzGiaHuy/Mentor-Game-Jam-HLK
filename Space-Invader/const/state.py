class BulletState:
    INVISIBLE = 'invisible'
    FLYING = 'flying'


class EggState:
    INVISIBLE = 'invisible'
    FLYING = 'flying'


class PlayerState:
    PLAYING = 'playing'
    DEAD = 'dead'
    EXPLODING = 'exploding'
    UNTARGETABLE = 'untargetable'


class RocketState:
    READY = 'ready'
    FLYING = 'flying'
    JUST_EXPLODE = 'just_explode'
    EXPLODING = 'exploding'
    EXPLODED = 'exploded'


class EnemyState:
    ALIVE = 'alive'
    DEAD = 'dead'
    EXPLODING = 'exploding'


class BossState:
    ALIVE = 'alive'
    DEAD = 'dead'
    EXPLODING = 'exploding'
    SLEEP = 'sleep'
