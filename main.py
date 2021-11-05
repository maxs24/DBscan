import pygame
import functions
import dbscan


if __name__ == '__main__':
    r = 4
    points = []
    colors = []
    minPts = 3
    eps = 30
    screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
    pygame.display.update()
    play = True
    while play:
        #pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    functions.near_point(event.pos[0], event.pos[1], points, colors, r)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    #functions.flags(points, colors, minPts, eps)
                    dbscan.dbscan(points, colors, minPts, eps)
            screen.fill('WHITE')
            for i in range(len(points)):
                pygame.draw.circle(screen, colors[i], points[i], r)
            #flags()
            pygame.display.update()