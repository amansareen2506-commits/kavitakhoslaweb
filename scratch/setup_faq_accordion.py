import os

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

ACCORDION_CSS = """
  /* FAQ Accordion Styling */
  .we-specialize-exclusively, .we-specialize-exclusively2 {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.3s ease, padding 0.3s ease;
    opacity: 0;
    margin-top: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }
  .faq-item.active .we-specialize-exclusively,
  .faq-item2.active .we-specialize-exclusively2 {
    max-height: 500px !important;
    opacity: 1 !important;
    margin-top: 12px !important;
    padding-bottom: 12px !important;
  }
  /* Smooth rotation of the arrow icons */
  .frame-icon {
    transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
  }
  .faq-item.active .frame-icon,
  .faq-item2.active .frame-icon {
    transform: rotate(180deg) !important;
  }
  .what-types-of-diamonds-do-you-parent,
  .what-types-of-diamonds-do-you-group {
    cursor: pointer !important;
    user-select: none !important;
  }
"""

ACCORDION_JS = """
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const faqItems = document.querySelectorAll('.faq-item, .faq-item2');
    faqItems.forEach(item => {
      const header = item.querySelector('.what-types-of-diamonds-do-you-parent, .what-types-of-diamonds-do-you-group');
      if (header) {
        header.addEventListener('click', function() {
          const isActive = item.classList.contains('active');
          
          // Close all FAQ items
          faqItems.forEach(otherItem => {
            otherItem.classList.remove('active');
          });
          
          // If the clicked one wasn't active, open it
          if (!isActive) {
            item.classList.add('active');
          }
        });
      }
    });
  });
</script>
"""

# Inject CSS
style_end = content.find('</style>')
if style_end != -1:
    content = content[:style_end] + ACCORDION_CSS + content[style_end:]
    print("Injected Accordion CSS.")
else:
    print("Could not find </style> tag!")

# Inject JS before </body>
body_end = content.find('</body>')
if body_end != -1:
    content = content[:body_end] + ACCORDION_JS + content[body_end:]
    print("Injected Accordion JS.")
else:
    # If no </body> is found, append at the end
    content = content + ACCORDION_JS
    print("Appended Accordion JS at the end of the file.")

open(html_path, 'w', encoding='utf-8').write(content)
print("index.html updated successfully with FAQ dropdown functionality!")
