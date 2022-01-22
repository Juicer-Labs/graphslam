import pygame

class GraphPlotter():

    def __init__(self, width=1000, height=1000, background=(60, 60, 60), centerAtMiddle=True):
        pygame.init()
        self.width, self.height = width, height
        self.background = background
        self.screen = pygame.display.set_mode((width, height))
        self.ratio = 4
        self.update()

        self.center = (0,self.height)
        if centerAtMiddle:
            self.center = (self.width / 2, self.height / 2)


    def plotXY(self, X, Y, color=(255, 0, 0), radius=3):
        # self.screen.fill(self.background)

        for i in range(len(X) - 1):
            # Draw circle with (0, 0) at center of screen
            pygame.draw.circle(self.screen, color,
               (self.center[0] + int(X[i]), self.center[1] - int(Y[i])),
            radius)

        self.update()

    def draw_line(self, p1, p2, color = (20, 255, 255)):
        pygame.draw.line(self.screen, color, p1, p2)
        self.update()

    # TODO: make this decorator
    def update(self):
        pygame.display.flip()

    def __del__(self):
        pygame.quit()


    def draw_data_graph(self, vertices, edge_ids, edges, edge_covariance):
        self.screen.fill(self.background)

        self.plotXY(vertices[:, 0], vertices[:, 1])

        self.update()
