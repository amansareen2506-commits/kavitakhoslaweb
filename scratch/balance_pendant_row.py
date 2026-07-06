import os

html_path = 'natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html'
content = open(html_path, encoding='utf-8').read()

old_block = """        <section class="frame-section new-centered-row">
          <section class=rectangle-parent>
            <img class=frame-item loading=lazy alt src=/pendant-set.png?v=2036>

            <div class=frame-div>
              <div class=carat-solitaire-pendant-parent>
                <h2 class=carat-solitaire-pendant>Pendent Set</h2>
                <div class=k-yellow-gold>CRAFTED TO SHINE</div>
              </div>
            </div>
          </section>
        </section>"""

new_block = """        <section class="frame-section new-centered-row">
          <section class=rectangle-parent>
            <img class=frame-item loading=lazy alt src=/pendant-set.png?v=2036>

            <div class=frame-div>
              <div class=carat-solitaire-pendant-parent>
                <h2 class=carat-solitaire-pendant>Pendent Set</h2>
                <div class=k-yellow-gold>CRAFTED TO SHINE</div>
              </div>
            </div>
          </section>
          <!-- Invisible placeholder card to balance the flex row and make the main card exactly 50% width -->
          <section class=rectangle-parent style="visibility: hidden; height: 0; min-height: 0; padding: 0; margin: 0; flex: 1;"></section>
        </section>"""

if old_block in content:
    content = content.replace(old_block, new_block)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Successfully balanced the last flex row to keep the pendant set card at 50% width.")
else:
    print("Could not find the exact old block in natural-solitaire-and-diamonds.html!")
