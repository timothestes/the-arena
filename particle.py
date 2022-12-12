import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Ski on Ice")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

ski_pos = [300, 300]
ski_vel = [random.randint(-5, 5), random.randint(-5, 5)]
ski_rad = 20

ice_particles = []
for i in range(100):
    ice_particles.append([random.randint(0, 600), random.randint(0, 600)])

ice_rad = 5

clock = pygame.time.Clock()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update ski position
    ski_pos[0] += ski_vel[0]
    ski_pos[1] += ski_vel[1]

    # Check for screen boundaries and reverse ski velocity if needed
    if ski_pos[0] + ski_rad >= 600 or ski_pos[0] - ski_rad <= 0:
        ski_vel[0] *= -1
    if ski_pos[1] + ski_rad >= 600 or ski_pos[1] - ski_rad <= 0:
        ski_vel[1] *= -1

    # Update ice particle positions
    for i in range(len(ice_particles)):
        ice_particles[i][0] += random.randint(-3, 3)
        ice_particles[i][1] += random.randint(-3, 3)

    # Check for ski-ice particle collisions
    for particle in ice_particles:
        if (
            (ski_pos[0] - particle[0]) ** 2 + (ski_pos[1] - particle[1]) ** 2
        ) ** 0.5 <= ski_rad + ice_rad:
            # Reverse ski velocity
            ski_vel[0] *= -1
            ski_vel[1] *= -1
            break

    # Clear screen
    screen.fill(BLACK)

    # Draw ski and ice particles
    pygame.draw.circle(screen, BLUE, ski_pos, ski_rad)
    for particle in ice_particles:
        pygame.draw.circle(screen, WHITE, particle, ice_rad)

    # Update screen
    pygame.display.flip()

    # Control game speed
    clock.tick(60)
