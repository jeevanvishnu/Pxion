// =================== PAGE LOADER ===================
window.addEventListener('load', () => {
    setTimeout(() => {
        document.getElementById('page-loader').classList.add('hidden');
        const bgVideo = document.getElementById('hero-bg-video');
        if (bgVideo) {
            bgVideo.play().catch(err => {
                console.log('Video autoplay play triggered smoothly:', err);
            });
        }
    }, 1400);
});

// =================== HEADER SCROLL ===================
const header = document.getElementById('header');
const scrollTopBtn = document.getElementById('scroll-top');
const logoImg = document.querySelector('.logo-img');
window.addEventListener('scroll', () => {
    const isScrolled = window.scrollY > 40;
    if (header) {
        header.classList.toggle('scrolled', isScrolled);
    }
    if (logoImg) {
        logoImg.src = isScrolled ? 'assets/Logo.png' : 'assets/Logow.png';
    }
    if (scrollTopBtn) {
        scrollTopBtn.classList.toggle('visible', window.scrollY > 400);
    }
}, { passive: true });

// =================== MOBILE MENU ===================
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.getElementById('mobile-menu');
if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
        const open = mobileMenu.classList.toggle('open');
        hamburger.classList.toggle('active', open);
        hamburger.setAttribute('aria-expanded', open);
    });
    // Close on mobile link click
    document.querySelectorAll('.mobile-nav-link, .mobile-menu-cta .btn').forEach(link => {
        // Exclude dropdown toggles from closing the whole menu
        if (link.classList.contains('mobile-dropdown-toggle')) return;

        link.addEventListener('click', () => {
            mobileMenu.classList.remove('open');
            hamburger.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        });
    });

    // Mobile Dropdown Toggle
    const mobileDropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');
    mobileDropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
            toggle.setAttribute('aria-expanded', !isExpanded);
            const submenu = toggle.nextElementSibling;
            if (submenu && submenu.classList.contains('mobile-submenu')) {
                submenu.classList.toggle('open');
            }
        });
    });
}

// =================== SCROLL REVEAL ===================
const revealEls = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            e.target.classList.add('visible');
            revealObserver.unobserve(e.target);
        }
    });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
revealEls.forEach(el => revealObserver.observe(el));

// =================== SCROLL TO TOP ===================
const scrollTopElement = document.getElementById('scroll-top');
if (scrollTopElement) {
    scrollTopElement.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// =================== TESTIMONIALS SLIDER ===================
const track = document.getElementById('testimonialsTrack');
if (track) {
    const cards = track.querySelectorAll('.testimonial-card');
    const dotsContainer = document.getElementById('tDots');
    let currentIndex = 0;
    let cardsPerView = 1;
    let totalSlides = 0;

    const getCardsPerView = () => {
        const w = window.innerWidth;
        if (w >= 1024) return 3;
        if (w >= 768) return 2;
        return 1;
    };

    const buildDots = () => {
        dotsContainer.innerHTML = '';
        for (let i = 0; i < totalSlides; i++) {
            const dot = document.createElement('button');
            dot.className = 'tctrl-dot' + (i === 0 ? ' active' : '');
            dot.setAttribute('role', 'tab');
            dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
            dot.setAttribute('aria-selected', i === 0 ? 'true' : 'false');
            dot.addEventListener('click', () => goTo(i));
            dotsContainer.appendChild(dot);
        }
    };

    const updateSlider = () => {
        cardsPerView = getCardsPerView();
        totalSlides = Math.ceil(cards.length / cardsPerView);
        currentIndex = Math.min(currentIndex, totalSlides - 1);
        buildDots();
        updatePosition();
    };

    const updatePosition = () => {
        const cardW = cards[0].getBoundingClientRect().width + 24;
        track.style.transform = `translateX(-${currentIndex * cardsPerView * cardW}px)`;
        dotsContainer.querySelectorAll('.tctrl-dot').forEach((d, i) => {
            d.classList.toggle('active', i === currentIndex);
            d.setAttribute('aria-selected', i === currentIndex ? 'true' : 'false');
        });
    };

    const goTo = (idx) => {
        currentIndex = Math.max(0, Math.min(idx, totalSlides - 1));
        updatePosition();
    };

    const tPrevBtn = document.getElementById('tPrev');
    const tNextBtn = document.getElementById('tNext');
    if (tPrevBtn) tPrevBtn.addEventListener('click', () => goTo(currentIndex - 1));
    if (tNextBtn) tNextBtn.addEventListener('click', () => goTo(currentIndex + 1));

    // Auto-advance
    let autoSlide = setInterval(() => goTo((currentIndex + 1) % totalSlides), 5000);
    track.addEventListener('mouseenter', () => clearInterval(autoSlide));
    track.addEventListener('mouseleave', () => {
        clearInterval(autoSlide);
        autoSlide = setInterval(() => goTo((currentIndex + 1) % totalSlides), 5000);
    });

    window.addEventListener('resize', updateSlider, { passive: true });
    updateSlider();
}

// =================== SMOOTH SCROLL FOR NAV ===================
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const href = a.getAttribute('href');
        if (href && href !== '#' && href.startsWith('#')) {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offset = target.getBoundingClientRect().top + window.scrollY - 80;
                window.scrollTo({ top: offset, behavior: 'smooth' });
            }
        }
    });
});

// =================== MOUSE PARALLAX (BACKGROUND ORBS) ===================
const heroSection = document.getElementById('hero');
const ambientOrbs = document.querySelectorAll('.orb');

if (heroSection && ambientOrbs.length > 0) {
    heroSection.addEventListener('mousemove', (e) => {
        const { width, height, left, top } = heroSection.getBoundingClientRect();

        // Calculate mouse relative coordinates from the center of the hero section (-1 to 1)
        const mouseX = ((e.clientX - left) - width / 2) / (width / 2);
        const mouseY = ((e.clientY - top) - height / 2) / (height / 2);

        ambientOrbs.forEach((orb, index) => {
            // Give different speeds to different orbs for high-end parallax depth
            const speed = (index + 1) * 15;
            const transX = mouseX * speed;
            const transY = mouseY * speed;

            orb.style.transform = `translate3d(${transX}px, ${transY}px, 0)`;
        });
    });

    // Reset smoothly when cursor leaves the hero section
    heroSection.addEventListener('mouseleave', () => {
        ambientOrbs.forEach(orb => {
            orb.style.transition = 'transform 1.0s cubic-bezier(0.16, 1, 0.3, 1)';
            orb.style.transform = `translate3d(0, 0, 0)`;

            setTimeout(() => {
                orb.style.transition = '';
            }, 1000);
        });
    });
}

// =================== VIEWPORT-AWARE PLAYBACK ===================
const heroVideo = document.getElementById('hero-bg-video');
if (heroVideo) {
    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                heroVideo.play().catch(err => {
                    console.log('Video autoplay interrupted or deferred:', err);
                });
            } else {
                heroVideo.pause();
            }
        });
    }, { threshold: 0.05 });
    videoObserver.observe(heroVideo);
}

// =================== FAQ ACCORDION INTERACTION ===================
document.querySelectorAll('.faq-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
        const item = trigger.closest('.faq-item');
        const content = item.querySelector('.faq-content');
        const isOpen = item.classList.contains('active');

        // Close all other open items
        document.querySelectorAll('.faq-item.active').forEach(openItem => {
            if (openItem !== item) {
                openItem.classList.remove('active');
                openItem.querySelector('.faq-trigger').setAttribute('aria-expanded', 'false');
                openItem.querySelector('.faq-content').style.maxHeight = null;
                openItem.querySelector('.faq-content').setAttribute('aria-hidden', 'true');
            }
        });

        // Toggle the clicked item
        if (isOpen) {
            item.classList.remove('active');
            trigger.setAttribute('aria-expanded', 'false');
            content.style.maxHeight = null;
            content.setAttribute('aria-hidden', 'true');
        } else {
            item.classList.add('active');
            trigger.setAttribute('aria-expanded', 'true');
            content.style.maxHeight = content.scrollHeight + 'px';
            content.setAttribute('aria-hidden', 'false');
        }
    });
});

// =================== CONTACT FORM SUBMISSION ===================
const contactForm = document.getElementById('contact-form-submit');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const nameVal = document.getElementById('contact-name').value;
        const emailVal = document.getElementById('contact-email').value;
        const catSelect = document.getElementById('contact-category');
        const catVal = catSelect.options[catSelect.selectedIndex].text;

        // Create custom notification block
        const container = contactForm.parentNode;

        // Check if there is an existing notification and remove it
        const oldNotify = container.querySelector('.form-notification');
        if (oldNotify) {
            oldNotify.remove();
        }

        const notification = document.createElement('div');
        notification.className = 'form-notification';
        notification.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="flex-shrink:0">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                <polyline points="22 4 12 14.01 9 11.01" />
            </svg>
            <span>Thank you, <strong>${nameVal}</strong>! Your request for <strong>${catVal}</strong> has been received. Our certified engineers will contact you at <strong>${emailVal}</strong> within 2 hours.</span>
        `;

        // Insert notification above the form title or inside container top
        container.insertBefore(notification, container.firstChild);

        // Clear all fields smoothly
        contactForm.reset();

        // Smooth scroll to notification top
        notification.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
}

// =================== CATALOG INTERACTIVE FILTERING ===================
const filterTabs = document.querySelectorAll('.filter-tab');
const catalogCards = document.querySelectorAll('.catalog-card');

if (filterTabs.length > 0 && catalogCards.length > 0) {
    filterTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            filterTabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            tab.classList.add('active');

            const filterVal = tab.getAttribute('data-filter');

            catalogCards.forEach(card => {
                const cardCatsStr = card.getAttribute('data-category') || '';
                const cardCats = cardCatsStr.split(' ');

                if (filterVal === 'all' || cardCats.includes(filterVal)) {
                    // Show matching card
                    card.classList.remove('hidden');
                    card.classList.add('visible');
                } else {
                    // Hide non-matching card
                    card.classList.add('hidden');
                    card.classList.remove('visible');
                }
            });
        });
    });
}


// Animated Counters
document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll('.counter');
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const targetValue = parseInt(target.getAttribute('data-target'));
                let current = 0;
                const duration = 1500; // 1.5 seconds total
                const increment = targetValue / (duration / 16); // assuming 60fps (16ms per frame)
                
                const updateCounter = () => {
                    current += increment;
                    if (current < targetValue) {
                        target.innerText = Math.ceil(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        target.innerText = targetValue;
                    }
                };
                
                updateCounter();
                observer.unobserve(target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });
});
