import pygame

# Independent visual demo only. Targets and distances are simulated.
# F8: toggle ESP-style demo elements.
# F9: toggle Stream Mode (clean scene, no demo boxes/lines/labels).
# ESC: quit.
pygame.init()
W, H = 900, 560
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("ESP Demo - simulated targets only")
clock = pygame.time.Clock()

GREEN = (45, 255, 65)
WHITE = (245, 245, 245)
BROWN = (111, 77, 49)
font = pygame.font.SysFont("Arial", 17)
small = pygame.font.SysFont("Arial", 14)

show_esp = True
stream_mode = False

targets = [
    {"x": 285, "y": 255, "w": 48, "h": 115, "name": "BOT", "dist": 13.33, "hp": 0.82},
    {"x": 540, "y": 250, "w": 48, "h": 115, "name": "BOT", "dist": 15.46, "hp": 0.96},
]

def draw_person(cx, top, scale=1.0):
    head_r = int(10 * scale)
    pygame.draw.circle(screen, (205, 190, 160), (cx, top + int(13*scale)), head_r)
    pygame.draw.line(screen, WHITE, (cx, top + int(24*scale)),
                     (cx, top + int(62*scale)), max(2, int(4*scale)))
    pygame.draw.line(screen, WHITE, (cx, top + int(34*scale)),
                     (cx - int(16*scale), top + int(51*scale)), max(2, int(3*scale)))
    pygame.draw.line(screen, WHITE, (cx, top + int(34*scale)),
                     (cx + int(16*scale), top + int(49*scale)), max(2, int(3*scale)))
    pygame.draw.line(screen, WHITE, (cx, top + int(62*scale)),
                     (cx - int(13*scale), top + int(99*scale)), max(2, int(4*scale)))
    pygame.draw.line(screen, WHITE, (cx, top + int(62*scale)),
                     (cx + int(13*scale), top + int(99*scale)), max(2, int(4*scale)))

def label(text, x, y, color=WHITE, f=font):
    screen.blit(f.render(text, True, color), (x, y))

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F8:
                show_esp = not show_esp
            elif event.key == pygame.K_F9:
                stream_mode = not stream_mode

    # Background scene
    screen.fill((49, 53, 55))
    pygame.draw.rect(screen, BROWN, (0, 0, 650, 440))
    for x in range(35, 650, 95):
        pygame.draw.line(screen, (128, 91, 59), (x, 0), (x, 440), 2)
    pygame.draw.rect(screen, (37, 39, 41), (650, 0, 250, 440))
    pygame.draw.rect(screen, (22, 25, 27), (720, 0, 100, 440))
    pygame.draw.rect(screen, (72, 73, 71), (0, 440, W, 120))

    # Simulated characters remain part of the demo scene.
    for t in targets:
        draw_person(t["x"] + t["w"] // 2, t["y"] + 5, 0.95)

    # The clean Stream Mode suppresses all ESP-style visual elements.
    if show_esp and not stream_mode:
        aim = (W // 2, H - 45)
        pygame.draw.circle(screen, (230, 230, 230), aim, 4, 1)
        for t in targets:
            center = (t["x"], t["y"] + t["h"] // 2)
            pygame.draw.line(screen, GREEN, aim, center, 2)

        for t in targets:
            x, y, w, h = t["x"], t["y"], t["w"], t["h"]
            pygame.draw.rect(screen, GREEN, (x, y, w, h), 2)
            pygame.draw.rect(screen, (50, 50, 50), (x - 13, y, 7, h))
            pygame.draw.rect(screen, GREEN,
                             (x - 13, y + int(h * (1-t["hp"])), 7, int(h*t["hp"])))
            label(t["name"], x + 2, y - 24, WHITE, small)
            label(f'{t["dist"]:.2f}m', x - 2, y + h + 5, WHITE, small)

    # Demo controls are shown in the window itself.
    mode_text = "STREAM MODE: ON" if stream_mode else "STREAM MODE: OFF"
    label(mode_text, 15, 15, WHITE, small)
    label("F8: toggle demo ESP | F9: clean scene | ESC: quit", 15, 35, WHITE, small)
    pygame.display.flip()

pygame.quit()
