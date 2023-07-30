from typing import List, Union, Tuple

class Collider:
    def __init__(self, position, height, width):
        self.position = position
        self.height = height
        self.width = width
        


class ColliderManager:

    colliders: List[Union[Collider, Tuple[Collider]]] = []

    @staticmethod
    def collides(collider1: Collider, collider2: Collider) -> bool:
        if collider1 != collider2:
            if type(collider1) == tuple and type(collider1) != type(collider2):
                for collider in collider1:
                    left0 = collider.position.x
                    top0 = collider.position.y
                    left1 = collider2.position.x
                    top1 = collider2.position.y
                    right0 = collider.position.x + collider.width
                    bottom0 = collider.position.y + collider.height
                    right1 = collider2.position.x + collider2.width
                    bottom1 = collider2.position.y + collider2.height
                    if ((right1 >= left0) and (right0 >= left1)
                        and (bottom1 >= top0) and (bottom0 >= top1)):
                        return True

    @staticmethod
    def isCollision():
        for collider1 in ColliderManager.colliders:
            for collider2 in ColliderManager.colliders:
                if ColliderManager.collides(collider1, collider2):
                    return True
        return False
                    