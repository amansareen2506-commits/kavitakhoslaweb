import os

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

# Define blocks matching by the unique questions

# Q3
q3_old_block = """                  <div class=what-types-of>
                    DO YOU OFFER CUSTOMIZED JEWELRY ?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Every diamond & Solitare's we offer comes with a certified grading report from a reputable gemological laboratory namely <strong>GIA/IGI/DU/DGLA</strong>. This report details the unique characteristics of your diamond, giving you confidence in its authenticity and quality. Besides the labs EACH DIAMOND & SOLITARE’S ARE HANDPICKED / VALIDATED WITH 45 YEAR EXPERIENCE TEAM OF 10 PERSONALS.
                </div>"""

q3_new_block = """                  <div class=what-types-of>
                    DO YOU OFFER CUSTOMIZED JEWELRY ?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Yes, we invite you to explore the possibility of creating a customized jewelry or engagement ring that reflects your unique love story. Our skilled designers & artisans will guide you through the design process, ensuring a piece that is beautifully crafted and made for you and your loved ones. <strong>We are a Bespoke Jewelry Brand.</strong>
                </div>"""

# Q4
q4_old_block = """                  <div class=what-types-of>
                    WHAT ARE YOUR CARE RECOMMENDATIONS FOR MY DIAMOND &amp; GOLD
                    JEWELRY?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Every diamond & Solitare's we offer comes with a certified grading report from a reputable gemological laboratory namely <strong>GIA/IGI/DU/DGLA</strong>. This report details the unique characteristics of your diamond, giving you confidence in its authenticity and quality. Besides the labs EACH DIAMOND & SOLITARE’S ARE HANDPICKED / VALIDATED WITH 45 YEAR EXPERIENCE TEAM OF 10 PERSONALS.
                </div>"""

q4_new_block = """                  <div class=what-types-of>
                    WHAT ARE YOUR CARE RECOMMENDATIONS FOR MY DIAMOND &amp; GOLD
                    JEWELRY?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  To preserve the beauty of your diamond & gold jewelry, we recommend gentle cleaning with a soft cloth and storing it in a protective place when not in use. Avoid exposure to harsh chemicals that could tarnish its remarkable shine. The Jewelry bought from us has unlimited cleaning & maintenance facility for one year from the day of purchase.
                </div>"""

# Q5
q5_old_block = """                  <div class=what-types-of>HOW DOES YOUR PRICING WORK?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Every diamond & Solitare's we offer comes with a certified grading report from a reputable gemological laboratory namely <strong>GIA/IGI/DU/DGLA</strong>. This report details the unique characteristics of your diamond, giving you confidence in its authenticity and quality. Besides the labs EACH DIAMOND & SOLITARE’S ARE HANDPICKED / VALIDATED WITH 45 YEAR EXPERIENCE TEAM OF 10 PERSONALS.
                </div>"""

q5_new_block = """                  <div class=what-types-of>HOW DOES YOUR PRICING WORK?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Our pricing reflects the high quality and craftsmanship of our natural diamonds / solitaire's and designer gold jewelry. Each piece is thoughtfully priced based on its unique attributes and the care involved in its creation. Feel free to reach out for further details. We assure you our range with its pricing and quality of diamonds used are NOT at all available.
                </div>"""

# Q6
q6_old_block = """                  <div class=what-types-of>WHAT IS YOUR RETURN POLICY?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Every diamond & Solitare's we offer comes with a certified grading report from a reputable gemological laboratory namely <strong>GIA/IGI/DU/DGLA</strong>. This report details the unique characteristics of your diamond, giving you confidence in its authenticity and quality. Besides the labs EACH DIAMOND & SOLITARE’S ARE HANDPICKED / VALIDATED WITH 45 YEAR EXPERIENCE TEAM OF 10 PERSONALS.
                </div>"""

q6_new_block = """                  <div class=what-types-of>WHAT IS YOUR RETURN POLICY?</div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2 style="line-height: 1.6;">
                  We believe in the quality and authenticity of our pieces. We provide <strong>90% cash back</strong> in Diamond. <strong>95% in exchange</strong> of diamond jewelry purchased from us. <strong>97% cash back</strong> in gold and <strong>100% Exchange</strong> in Gold Jewelry purchased from us,<br><br><strong>Special Return / Exchange Policy If you Buy D colour Flawless(FL) clarity Jewelery from us, its cash back and exchange value is 100% of the Purchase Bill amount which also includes making charges and taxes.</strong><br><br>If you have questions or concerns after your purchase, please contact our customer service team, and we will assist you personally.
                </div>"""

# Q7
q7_old_block = """                  <div class=what-types-of>
                    CAN I TRACK MY ORDER ONCE I PLACE IT?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Every diamond & Solitare's we offer comes with a certified grading report from a reputable gemological laboratory namely <strong>GIA/IGI/DU/DGLA</strong>. This report details the unique characteristics of your diamond, giving you confidence in its authenticity and quality. Besides the labs EACH DIAMOND & SOLITARE’S ARE HANDPICKED / VALIDATED WITH 45 YEAR EXPERIENCE TEAM OF 10 PERSONALS.
                </div>"""

q7_new_block = """                  <div class=what-types-of>
                    CAN I TRACK MY ORDER ONCE I PLACE IT?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  We specialize exclusively in certified natural diamonds daily
                  hand picked, ensuring that each stone meets the highest
                  standards of quality and authenticity. Our collection includes
                  a range of sizes and cuts, allowing you to find the perfect
                  diamond to cherish.
                </div>"""

# Q8
q8_old_block = """                  <div class=what-types-of>
                    HOW DO I CARE FOR MY CERTIFIED DIAMOND?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  Every diamond & Solitare's we offer comes with a certified grading report from a reputable gemological laboratory namely <strong>GIA/IGI/DU/DGLA</strong>. This report details the unique characteristics of your diamond, giving you confidence in its authenticity and quality. Besides the labs EACH DIAMOND & SOLITARE’S ARE HANDPICKED / VALIDATED WITH 45 YEAR EXPERIENCE TEAM OF 10 PERSONALS.
                </div>"""

q8_new_block = """                  <div class=what-types-of>
                    HOW DO I CARE FOR MY CERTIFIED DIAMOND?
                  </div>
                  <img class=frame-icon alt src=/Frame1.ca451626.svg?v=2030>
                </div>
                <div class=we-specialize-exclusively2>
                  We specialize exclusively in certified natural diamonds daily
                  hand picked, ensuring that each stone meets the highest
                  standards of quality and authenticity. Our collection includes
                  a range of sizes and cuts, allowing you to find the perfect
                  diamond to cherish.
                </div>"""

content = content.replace(q3_old_block, q3_new_block)
content = content.replace(q4_old_block, q4_new_block)
content = content.replace(q5_old_block, q5_new_block)
content = content.replace(q6_old_block, q6_new_block)
content = content.replace(q7_old_block, q7_new_block)
content = content.replace(q8_old_block, q8_new_block)

open(html_path, 'w', encoding='utf-8').write(content)
print("Corrected and updated FAQ answers in index.html.")
