// =================== PAGE LOADER ===================
window.addEventListener('load', () => {
    setTimeout(() => {
        document.getElementById('page-loader').classList.add('hidden');
    }, 1400);
});

// =================== HEADER SCROLL ===================
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
    document.getElementById('scroll-top').classList.toggle('visible', window.scrollY > 400);
}, { passive: true });

// =================== MOBILE MENU ===================
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.getElementById('mobile-menu');
hamburger.addEventListener('click', () => {
    const open = mobileMenu.classList.toggle('open');
    hamburger.classList.toggle('active', open);
    hamburger.setAttribute('aria-expanded', open);
});
// Close on mobile link click
document.querySelectorAll('.mobile-nav-link, .mobile-menu-cta .btn').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
    });
});

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
document.getElementById('scroll-top').addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// =================== TESTIMONIALS SLIDER ===================
const track = document.getElementById('testimonialsTrack');
const cards = track.querySelectorAll('.testimonial-card');
const dotsContainer = document.getElementById('tDots');
let currentIndex = 0;
let cardsPerView = 1;
let totalSlides = 0;

function getCardsPerView() {
    const w = window.innerWidth;
    if (w >= 1024) return 3;
    if (w >= 768) return 2;
    return 1;
}

function buildDots() {
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
}

function updateSlider() {
    cardsPerView = getCardsPerView();
    totalSlides = Math.ceil(cards.length / cardsPerView);
    currentIndex = Math.min(currentIndex, totalSlides - 1);
    buildDots();
    updatePosition();
}

function updatePosition() {
    const cardW = cards[0].getBoundingClientRect().width + 24;
    track.style.transform = `translateX(-${currentIndex * cardsPerView * cardW}px)`;
    dotsContainer.querySelectorAll('.tctrl-dot').forEach((d, i) => {
        d.classList.toggle('active', i === currentIndex);
        d.setAttribute('aria-selected', i === currentIndex ? 'true' : 'false');
    });
}

function goTo(idx) {
    currentIndex = Math.max(0, Math.min(idx, totalSlides - 1));
    updatePosition();
}

document.getElementById('tPrev').addEventListener('click', () => goTo(currentIndex - 1));
document.getElementById('tNext').addEventListener('click', () => goTo(currentIndex + 1));

// Auto-advance
let autoSlide = setInterval(() => goTo((currentIndex + 1) % totalSlides), 5000);
track.addEventListener('mouseenter', () => clearInterval(autoSlide));
track.addEventListener('mouseleave', () => {
    clearInterval(autoSlide);
    autoSlide = setInterval(() => goTo((currentIndex + 1) % totalSlides), 5000);
});

window.addEventListener('resize', updateSlider, { passive: true });
updateSlider();

// =================== SMOOTH SCROLL FOR NAV ===================
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) {
            e.preventDefault();
            const offset = target.getBoundingClientRect().top + window.scrollY - 80;
            window.scrollTo({ top: offset, behavior: 'smooth' });
        }
    });
});

// =================== MOUSE PARALLAX ===================
const heroSection = document.getElementById('hero');
const parallaxCards = document.querySelectorAll('.parallax-card');

if (heroSection) {
    heroSection.addEventListener('mousemove', (e) => {
        const { width, height, left, top } = heroSection.getBoundingClientRect();

        // Calculate mouse relative coordinates from the center of the hero section (-1 to 1)
        const mouseX = ((e.clientX - left) - width / 2) / (width / 2);
        const mouseY = ((e.clientY - top) - height / 2) / (height / 2);

        parallaxCards.forEach(card => {
            const speed = parseFloat(card.getAttribute('data-speed')) || 1.0;

            if (card.classList.contains('tv-frame')) {
                // TV Frame gets dynamic 3D rotation and soft translation
                const rotX = 8 - (mouseY * 8 * speed);
                const rotY = -14 + (mouseX * 12 * speed);
                const transX = mouseX * 12 * speed;
                const transY = mouseY * 12 * speed;

                card.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg) rotateZ(2deg) translate3d(${transX}px, ${transY}px, 0)`;
            } else if (card.classList.contains('hero-badge-float')) {
                // Floating glassmorphism cards get dynamic parallax slide
                const transX = mouseX * 24 * speed;
                const transY = mouseY * 24 * speed;

                // Retain their 3D translateZ parameter from CSS float states
                card.style.transform = `translate3d(${transX}px, ${transY}px, 40px)`;
            }
        });
    });

    // Reset smoothly when cursor leaves the hero section
    heroSection.addEventListener('mouseleave', () => {
        parallaxCards.forEach(card => {
            card.style.transition = 'transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)';

            if (card.classList.contains('tv-frame')) {
                card.style.transform = `rotateX(8deg) rotateY(-14deg) rotateZ(2deg) translate3d(0, 0, 0)`;
            } else if (card.classList.contains('hero-badge-float')) {
                card.style.transform = `translate3d(0, 0, 30px)`;
            }

            // Clean up transition property so movement remains responsive
            setTimeout(() => {
                card.style.transition = '';
            }, 800);
        });
    });
}
