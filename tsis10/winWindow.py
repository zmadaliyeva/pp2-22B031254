
import psycopg2
import pygame

import var

conn = psycopg2.connect(dbname='score_data', user='postgres', password='196235', host='127.0.0.1')
conn.autocommit = True
cur = conn.cursor()
# cur.execute(
#     """create table SCORE_DATA (
#         username VARCHAR(50),
#         score VARCHAR(50)
#     );"""
# )
def get_font(size):
    return pygame.font.SysFont("bahnschrift", size)
i = 1
j = 1

class WinWindow:
    def __init__(self, screen):
        pygame.init()
        self.SCREEN = screen
        pygame.display.set_caption("Game over")

        self.WIN_TEXT = get_font(60).render("Game over", True, "White")
        self.USER_TEXT = get_font(30).render("Username", True, "White")

        self.SCORE_TEXT = get_font(30).render("Score", True, "White")
        self.WIN_RECT = self.WIN_TEXT.get_rect(center=(300, 100))

        self.MOUSE_POS = pygame.mouse.get_pos()
        self.t = True
    def sql(self):
        self.USER_NAME = get_font(30).render(f"{var.user}", True, "White")
        self.USER_SCORE = get_font(30).render(f"{var.Length_of_snake-1}", True, "White")
        cur.execute("""INSERT INTO SCORE_DATA (username, score) VALUES (%s, %s)""", (var.user, var.Length_of_snake-1))

        user_query = """SELECT * FROM SCORE_DATA ORDER BY score DESC"""
        cur.execute(user_query)
        global rows_name
        rows_name = cur.fetchall()

    # Отрисовка экрана выигрыша
    def draw_win_window(self):
        if self.t:
            self.sql()
            self.t = False
        else:
            self.SCREEN.fill((0,0,0))
            for k in range(len(rows_name)):
                if(k<=7):
                    self.SCREEN.blit(get_font(30).render(rows_name[k][0], True, "White"), [100, 160 + 40*(k+1)])
                    self.SCREEN.blit(get_font(30).render(rows_name[k][1], True, "White"), [400, 160 + 40 *(k+1)])

            self.SCREEN.blit(self.WIN_TEXT, self.WIN_RECT)
            self.SCREEN.blit(self.USER_TEXT, [100, 160])
            self.SCREEN.blit(self.SCORE_TEXT, [400, 160])



        pygame.display.update()