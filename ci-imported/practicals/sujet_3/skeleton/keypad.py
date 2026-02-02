import pygame
from skeleton.custom_types import UShort


class Keypad:

    @staticmethod
    def is_pressed(keycode: UShort):
        key_mapping = {
            0x1: pygame.K_1, 0x2: pygame.K_2, 0x3: pygame.K_3, 0xc: pygame.K_4,
            0x4: pygame.K_q, 0x5: pygame.K_w, 0x6: pygame.K_e, 0xd: pygame.K_r,
            0x7: pygame.K_a, 0x8: pygame.K_s, 0x9: pygame.K_d, 0xe: pygame.K_f,
            0xa: pygame.K_z, 0x0: pygame.K_x, 0xb: pygame.K_c, 0xf: pygame.K_v
        }

        pygame_key = key_mapping.get(int(keycode))
        if pygame_key is None:
            return False
        keys = pygame.key.get_pressed()
        return keys[pygame_key]
