css_code = """
/* ======================== BENTO GALLERY ======================== */
.bento-gallery {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 12px;
    margin-top: 40px;
}

.bento-item {
    position: relative;
    overflow: hidden;
    height: 320px;
    background: #000;
}

.bento-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.bento-item:hover img {
    transform: scale(1.05);
}

.bento-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0) 40%);
    pointer-events: none;
}

.bento-title {
    position: absolute;
    bottom: 20px;
    left: 24px;
    color: #fff;
    font-size: 18px;
    font-weight: 500;
    margin: 0;
    z-index: 2;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    font-family: 'Inter', sans-serif;
}

/* Staggered Grid Column Spans */
.bento-item:nth-child(1) { grid-column: span 3; }
.bento-item:nth-child(2) { grid-column: span 5; }
.bento-item:nth-child(3) { grid-column: span 4; }
.bento-item:nth-child(4) { grid-column: span 5; }
.bento-item:nth-child(5) { grid-column: span 4; }
.bento-item:nth-child(6) { grid-column: span 3; }

/* Responsive adjustments */
@media (max-width: 992px) {
    .bento-item:nth-child(1) { grid-column: span 5; }
    .bento-item:nth-child(2) { grid-column: span 7; }
    .bento-item:nth-child(3) { grid-column: span 12; height: 250px; }
    .bento-item:nth-child(4) { grid-column: span 12; height: 250px; }
    .bento-item:nth-child(5) { grid-column: span 7; }
    .bento-item:nth-child(6) { grid-column: span 5; }
}

@media (max-width: 768px) {
    .bento-item:nth-child(1),
    .bento-item:nth-child(2),
    .bento-item:nth-child(3),
    .bento-item:nth-child(4),
    .bento-item:nth-child(5),
    .bento-item:nth-child(6) { 
        grid-column: span 6; 
        height: 220px; 
    }
}

@media (max-width: 576px) {
    .bento-item:nth-child(1),
    .bento-item:nth-child(2),
    .bento-item:nth-child(3),
    .bento-item:nth-child(4),
    .bento-item:nth-child(5),
    .bento-item:nth-child(6) { 
        grid-column: span 12; 
        height: 250px; 
    }
}
"""

with open('c:/Users/jeeva/OneDrive/Documents/Bebright/style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)
print("CSS appended to style.css")
