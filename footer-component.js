/**
 * Kavita Khosla — Global Footer Component
 * Injects a unified luxury footer into every page.
 * To edit the footer, change this file only.
 */
(function () {
  /* ── 1. CSS ─────────────────────────────────────────────── */
  const style = document.createElement('style');
  style.id = 'kk-footer-styles';
  style.textContent = `
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@300;400;500&display=swap');

    /* ── Reset on footer elements ── */
    #kk-global-footer * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    /* ── Footer shell ── */
    #kk-global-footer {
      width: 100%;
      background: radial-gradient(ellipse at 60% 0%, #0d3028 0%, #06231d 55%, #041a15 100%);
      font-family: 'Inter', sans-serif;
      position: relative;
      overflow: visible !important;
    }

    /* ── Inner container ── */
    #kk-global-footer .kk-footer-inner {
      max-width: 1440px;
      margin: 0 auto;
      padding: 80px 40px 0;
    }

    /* ── Four-column grid ── */
    #kk-global-footer .kk-footer-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 48px 40px;
      padding-bottom: 64px;
    }

    /* ── Column heading ── */
    #kk-global-footer .kk-col-heading {
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #F8F6F2;
      margin-bottom: 18px;
    }

    /* ── Gold ornament divider under heading ── */
    #kk-global-footer .kk-col-divider {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 22px;
    }
    #kk-global-footer .kk-col-divider-line {
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, transparent, #C8A15A 40%, #C8A15A 60%, transparent);
      opacity: 0.5;
    }
    #kk-global-footer .kk-col-divider-diamond {
      width: 5px;
      height: 5px;
      background: #C8A15A;
      transform: rotate(45deg);
      flex-shrink: 0;
    }

    /* ── Nav links ── */
    #kk-global-footer .kk-footer-links {
      display: flex;
      flex-direction: column;
      gap: 12px;
      list-style: none;
    }
    #kk-global-footer .kk-footer-links a {
      font-family: 'Inter', sans-serif;
      font-size: 12.5px;
      font-weight: 300;
      letter-spacing: 0.06em;
      color: #E8E6DF;
      text-decoration: none;
      transition: color 0.3s ease;
      display: inline-block;
    }
    #kk-global-footer .kk-footer-links a:hover {
      color: #C8A15A;
    }

    /* ── Gold divider above bottom bar ── */
    #kk-global-footer .kk-footer-divider {
      width: 100%;
      height: 1px;
      background: linear-gradient(90deg, transparent 0%, #C8A15A 20%, #C8A15A 80%, transparent 100%);
      opacity: 0.6;
    }

    /* ── Bottom bar ── */
    #kk-global-footer .kk-footer-bottom {
      width: 100%;
      padding: 24px 0 48px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }
    #kk-global-footer .kk-footer-copyright {
      font-size: 11.5px;
      font-weight: 300;
      letter-spacing: 0.08em;
      color: rgba(232, 230, 223, 0.55);
      white-space: nowrap;
    }
    #kk-global-footer .kk-footer-socials {
      display: flex;
      align-items: center;
      gap: 24px;
      flex-shrink: 0;
    }
    #kk-global-footer .kk-footer-socials a {
      display: flex;
      align-items: center;
      gap: 7px;
      font-size: 12px;
      font-weight: 300;
      letter-spacing: 0.06em;
      color: #E8E6DF;
      text-decoration: none;
      transition: color 0.3s ease;
      white-space: nowrap;
    }
    #kk-global-footer .kk-footer-socials a:hover {
      color: #C8A15A;
    }
    #kk-global-footer .kk-footer-socials svg {
      width: 16px;
      height: 16px;
      min-width: 16px;
      fill: #C8A15A;
      flex-shrink: 0;
      transition: fill 0.3s ease;
    }
    #kk-global-footer .kk-footer-socials a:hover svg {
      fill: #C8A15A;
    }

    /* ── RESPONSIVE: Tablet ── */
    @media (max-width: 960px) {
      #kk-global-footer .kk-footer-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 40px 32px;
      }
    }

    /* ── RESPONSIVE: Mobile ── */
    @media (max-width: 600px) {
      #kk-global-footer .kk-footer-inner {
        padding: 56px 24px 0;
      }
      #kk-global-footer .kk-footer-grid {
        grid-template-columns: 1fr;
        gap: 36px;
        text-align: center;
        padding-bottom: 48px;
      }
      #kk-global-footer .kk-col-divider {
        justify-content: center;
      }
      #kk-global-footer .kk-footer-links {
        flex-direction: row !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 10px 20px !important;
        align-items: center !important;
      }
      #kk-global-footer .kk-footer-bottom {
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 16px;
        padding: 20px 0 40px;
      }
      #kk-global-footer .kk-footer-socials {
        justify-content: center;
      }
    }
  `;
  document.head.appendChild(style);

  /* ── 2. HTML ─────────────────────────────────────────────── */
  const footerHTML = `
    <footer id="kk-global-footer">
      <div class="kk-footer-inner">

        <div class="kk-footer-grid">

          <!-- Col 1: ABOUT -->
          <div class="kk-footer-col">
            <div class="kk-col-heading">About</div>
            <div class="kk-col-divider">
              <div class="kk-col-divider-line"></div>
              <div class="kk-col-divider-diamond"></div>
              <div class="kk-col-divider-line"></div>
            </div>
            <ul class="kk-footer-links">
              <li><a href="/about-us/about-us.html">About Us</a></li>
              <li><a href="/about-us/about-us.html">Our Team</a></li>
              <li><a href="/about-us/about-us.html">Our Legacy</a></li>
            </ul>
          </div>

          <!-- Col 2: COLLECTIONS -->
          <div class="kk-footer-col">
            <div class="kk-col-heading">Collections</div>
            <div class="kk-col-divider">
              <div class="kk-col-divider-line"></div>
              <div class="kk-col-divider-diamond"></div>
              <div class="kk-col-divider-line"></div>
            </div>
            <ul class="kk-footer-links">
              <li><a href="/malana-collection/malana-collection.html">Rings</a></li>
              <li><a href="/thia-collection/thia-collection.html">Earrings</a></li>
              <li><a href="/pierre-collection/pendants.html">Pendants</a></li>
              <li><a href="/pierre-collection/necklaces.html">Necklaces</a></li>
              <li><a href="/pierre-collection/solitaire-pendants.html">Solitaire Pendant Sets</a></li>
              <li><a href="/onzee-collection/onzee-collection.html">Bracelets &amp; Bangles</a></li>
              <li><a href="/natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html">Natural Diamond &amp; Solitaires</a></li>
              <li><a href="/lab-grown-diamonds/lab-grown-diamonds.html">Lab Grown Diamonds</a></li>
            </ul>
          </div>

          <!-- Col 3: MMTC -->
          <div class="kk-footer-col">
            <div class="kk-col-heading">MMTC</div>
            <div class="kk-col-divider">
              <div class="kk-col-divider-line"></div>
              <div class="kk-col-divider-diamond"></div>
              <div class="kk-col-divider-line"></div>
            </div>
            <ul class="kk-footer-links">
              <li><a href="/mmtc/gold-coins.html">Gold Coins</a></li>
              <li><a href="/mmtc/silver-coins.html">Silver Coins</a></li>
              <li><a href="/mmtc/silver-bars.html">Silver Bars</a></li>
            </ul>
          </div>

          <!-- Col 4: SUPPORT -->
          <div class="kk-footer-col">
            <div class="kk-col-heading">Support</div>
            <div class="kk-col-divider">
              <div class="kk-col-divider-line"></div>
              <div class="kk-col-divider-diamond"></div>
              <div class="kk-col-divider-line"></div>
            </div>
            <ul class="kk-footer-links">
              <li><a href="/index.html#faq">FAQ</a></li>
              <li><a href="/contact-us/contact-us.html">Book Appointment</a></li>
              <li><a href="/contact-us/contact-us.html">Contact Us</a></li>
            </ul>
          </div>

        </div><!-- /grid -->

        <!-- Gold divider -->
        <div class="kk-footer-divider"></div>

        <!-- Bottom bar -->
        <div class="kk-footer-bottom">
          <span class="kk-footer-copyright">&copy; 2026 | GST NO. 06AJAPK5493J1Z0</span>
          <div class="kk-footer-socials">
            <a href="https://www.instagram.com/kavitakhosla.studio" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              Instagram
            </a>
            <a href="https://www.facebook.com/kavitakhosla.studio" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              Facebook
            </a>
          </div>
        </div>

      </div><!-- /inner -->
    </footer>
  `;

  /* ── 3. Inject & Replace ─────────────────────────────────── */
  const OLD_FOOTER_SELECTORS = [
    '.frame-parent18',
    '.frame-parent19',
    '.kavita-khosla-2026-gst-no-parent',
    '.kavita-khosla-2026-gst-no-group',
    '.kavita-khosla-2026-gst-no-container',
    '.kavita-khosla-2026-gst-no-parent3',
    '.social-media-handle-nav-parent',
  ];

  function hideOldFooter() {
    OLD_FOOTER_SELECTORS.forEach(function(sel) {
      document.querySelectorAll(sel).forEach(function(el) {
        el.style.cssText = 'display:none!important;visibility:hidden!important;height:0!important;overflow:hidden!important;';
      });
    });
  }

  function injectFooter() {
    if (document.getElementById('kk-global-footer')) return;
    hideOldFooter();
    const wrapper = document.createElement('div');
    wrapper.innerHTML = footerHTML;
    const footerEl = wrapper.firstElementChild;
    document.body.appendChild(footerEl);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectFooter);
  } else {
    injectFooter();
  }
})();
