while True:
    start_screen()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
        if rect_easy.collidepoint(mouseX, mouseY) or rect_medium.collidepoint(mouseX, mouseY) or rect_hard.collidepoint(mouseX, mouseY):

    pygame.display.update()