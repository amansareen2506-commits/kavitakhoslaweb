import os

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

# Let's define the replacements for the FAQ answers:

# Q2: Authenticity
q2_old = """                <div class=we-specialize-exclusively2>
                  We specialize exclusively in certified natural diamonds daily
                  hand picked, ensuring that each stone meets the highest
                  standards of quality and authenticity. Our collection includes
                  a range of sizes and cuts, allowing you to find the perfect
                  diamond to cherish.
                </div>"""

q2_new = """                <div class=we-specialize-exclusively2>
                  Every diamond & Solitare's we offer comes with a certified grading report from a reputable gemological laboratory namely <strong>GIA/IGI/DU/DGLA</strong>. This report details the unique characteristics of your diamond, giving you confidence in its authenticity and quality. Besides the labs EACH DIAMOND & SOLITARE’S ARE HANDPICKED / VALIDATED WITH 45 YEAR EXPERIENCE TEAM OF 10 PERSONALS.
                </div>"""

# Q3: Customized
# Since the class name we-specialize-exclusively2 is used in multiple blocks, we will target the full faq-item blocks to be unique!

faq_block_q3_old = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>
                    DO YOU OFFER CUSTOMIZED JEWELRY ?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  We specialize exclusively in certified natural diamonds daily
                  hand picked, ensuring that each stone meets the highest
                  standards of quality and authenticity. Our collection includes
                  a range of sizes and cuts, allowing you to find the perfect
                  diamond to cherish.
                </div>
              </div>"""

faq_block_q3_new = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>
                    DO YOU OFFER CUSTOMIZED JEWELRY ?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Yes, we invite you to explore the possibility of creating a customized jewelry or engagement ring that reflects your unique love story. Our skilled designers & artisans will guide you through the design process, ensuring a piece that is beautifully crafted and made for you and your loved ones. <strong>We are a Bespoke Jewelry Brand.</strong>
                </div>
              </div>"""

# Q4: Care Recommendations
faq_block_q4_old = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>
                    WHAT ARE YOUR CARE RECOMMENDATIONS FOR MY DIAMOND &amp; GOLD
                    JEWELRY?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  We specialize exclusively in certified natural diamonds daily
                  hand picked, ensuring that each stone meets the highest
                  standards of quality and authenticity. Our collection includes
                  a range of sizes and cuts, allowing you to find the perfect
                  diamond to cherish.
                </div>
              </div>"""

faq_block_q4_new = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>
                    WHAT ARE YOUR CARE RECOMMENDATIONS FOR MY DIAMOND &amp; GOLD
                    JEWELRY?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  To preserve the beauty of your diamond & gold jewelry, we recommend gentle cleaning with a soft cloth and storing it in a protective place when not in use. Avoid exposure to harsh chemicals that could tarnish its remarkable shine. The Jewelry bought from us has unlimited cleaning & maintenance facility for one year from the day of purchase.
                </div>
              </div>"""

# Q5: Pricing
faq_block_q5_old = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>HOW DOES YOUR PRICING WORK?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  We specialize exclusively in certified natural diamonds daily
                  hand picked, ensuring that each stone meets the highest
                  standards of quality and authenticity. Our collection includes
                  a range of sizes and cuts, allowing you to find the perfect
                  diamond to cherish.
                </div>
              </div>"""

faq_block_q5_new = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>HOW DOES YOUR PRICING WORK?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Our pricing reflects the high quality and craftsmanship of our natural diamonds / solitaire's and designer gold jewelry. Each piece is thoughtfully priced based on its unique attributes and the care involved in its creation. Feel free to reach out for further details. We assure you our range with its pricing and quality of diamonds used are NOT at all available.
                </div>
              </div>"""

# Q6: Return Policy
faq_block_q6_old = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>WHAT IS YOUR RETURN POLICY?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  We specialize exclusively in certified natural diamonds daily
                  hand picked, ensuring that each stone meets the highest
                  standards of quality and authenticity. Our collection includes
                  a range of sizes and cuts, allowing you to find the perfect
                  diamond to cherish.
                </div>
              </div>"""

faq_block_q6_new = """              <div class=faq-item2>
                <div class=what-types-of-diamonds-do-you-group>
                  <div class=what-types-of>WHAT IS YOUR RETURN POLICY?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2 style="line-height: 1.6;">
                  We believe in the quality and authenticity of our pieces. We provide <strong>90% cash back</strong> in Diamond. <strong>95% in exchange</strong> of diamond jewelry purchased from us. <strong>97% cash back</strong> in gold and <strong>100% Exchange</strong> in Gold Jewelry purchased from us,<br><br><strong>Special Return / Exchange Policy If you Buy D colour Flawless(FL) clarity Jewelery from us, its cash back and exchange value is 100% of the Purchase Bill amount which also includes making charges and taxes.</strong><br><br>If you have questions or concerns after your purchase, please contact our customer service team, and we will assist you personally.
                </div>
              </div>"""

# Apply the updates sequentially
content = content.replace(q2_old, q2_new)
content = content.replace(faq_block_q3_old, faq_block_q3_new)
content = content.replace(faq_block_q4_old, faq_block_q4_new)
content = content.replace(faq_block_q5_old, faq_block_q5_new)
content = content.replace(faq_block_q6_old, faq_block_q6_new)

open(html_path, 'w', encoding='utf-8').write(content)
print("Updated index.html FAQ answers successfully!")
