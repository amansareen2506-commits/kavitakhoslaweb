import os

html_path = 'about-us/about-us.html'
content = open(html_path, encoding='utf-8').read()

# Locate the two section blocks
deepika_block = """                <section class=rectangle-parent20>
                  <img class=frame-child62 loading=lazy alt src=/Rectangle-123@2x.8e2e891c.png?v=2030>

                  <div class=deepika-rai-parent>
                    <div class=deepika-rai>Deepika Rai</div>
                    <div class=founder-ceo-chief-design-off-parent>
                      <div class=founder-ceo>
                        Founder &amp; CEO Chief Design<br>Officer Creative
                        Director
                      </div>
                      <i class=years-of-experience>With over 35 years of<br>experience in design</i>
                    </div>
                  </div>
                </section>"""

kavita_block = """                <section class=rectangle-parent20>
                  <img class=frame-child62 loading=lazy alt src=/Rectangle-126@2x.dacea64f.png?v=2030>

                  <div class=deepika-rai-parent>
                    <div class=deepika-rai>Kavita Khosla</div>
                    <div class=founder-ceo-chief-design-off-parent>
                      <div class=founder-ceo>Founder &amp; Managing Director</div>
                      <i class=years-of-experience>35 years of Experience</i>
                    </div>
                  </div>
                </section>"""

# Swap their positions in the content
if deepika_block in content and kavita_block in content:
    # Use temporary placeholders to avoid overlap issues
    content = content.replace(deepika_block, "[[TEMP_DEEPIKA]]")
    content = content.replace(kavita_block, "[[TEMP_KAVITA]]")
    content = content.replace("[[TEMP_DEEPIKA]]", kavita_block)
    content = content.replace("[[TEMP_KAVITA]]", deepika_block)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Successfully swapped Deepika Rai and Kavita Khosla profile cards in about-us.html.")
else:
    print("Could not find the exact HTML blocks for Deepika Rai and Kavita Khosla!")
