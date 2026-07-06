import os

html_path = 'natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html'
content = open(html_path, encoding='utf-8').read()

# 1. Update HTML: remove placeholder card, keep only the main card
old_html_block = """        <section class="frame-section new-centered-row">
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

new_html_block = """        <section class="frame-section new-centered-row">
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

content = content.replace(old_html_block, new_html_block)

# 2. Inject CSS rules right before </style><body> to center the card on desktop
CENTERING_CSS = """
  /* Center the last single card on the page on desktop */
  .new-centered-row {
    justify-content: center !important;
  }
  .new-centered-row .rectangle-parent {
    max-width: calc(50% - 12px) !important;
    flex: 0 0 calc(50% - 12px) !important;
  }
  @media screen and (max-width: 768px) {
    .new-centered-row .rectangle-parent {
      max-width: 100% !important;
      flex: 1 1 100% !important;
    }
  }
"""

style_end = content.find('</style><body>')
if style_end != -1:
    content = content[:style_end] + CENTERING_CSS + content[style_end:]
    print("Injected Centering CSS.")
else:
    print("Could not find style end tag!")

open(html_path, 'w', encoding='utf-8').write(content)
print("Updated natural-solitaire-and-diamonds.html to center the pendant set card.")
