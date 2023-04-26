# Dead window
        while True:
            render_end = game_over.render('GAME OVER', 20, pygame.Color('red'))
            last_balance = final_balance.render(f'Your balance was - {coins}', 20, pygame.Color('orange'))
            surface.blit(render_end, (WIDTH // 2 - 200, WIDTH // 3))
            surface.blit(last_balance, (WIDTH // 2 - 220, WIDTH // 2 - 50))
            pygame.display.flip()
            
            # For closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    exit()