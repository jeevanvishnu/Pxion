css_code = """
/* ======================== PARALLELOGRAM GALLERY ======================== */
.parallelogram-gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
    margin-bottom: 20px;
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}

.pg-item {
    width: calc(25% - 15px);
    height: 180px;
    position: relative;
    cursor: pointer;
    overflow: hidden;
    transition: transform 0.3s ease, filter 0.3s ease;
    border-radius: 4px; /* Slight rounding for elegance, though clip-path overwrites it mostly */
}

.pg-item:hover {
    transform: scale(1.05);
    z-index: 10;
}

/* Alternating rows logic (4 items per row) */
/* Leaning right default */
.pg-item {
    clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%);
}

/* Leaning left for next row */
.pg-item:nth-child(8n+5),
.pg-item:nth-child(8n+6),
.pg-item:nth-child(8n+7),
.pg-item:nth-child(8n+8) {
    clip-path: polygon(0% 0, 90% 0, 100% 100%, 10% 100%);
}

.pg-content {
    width: 100%;
    height: 100%;
    position: relative;
}

.pg-content img, .pg-content video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.pg-item:hover .pg-content img,
.pg-item:hover .pg-content video {
    transform: scale(1.1);
}

.pg-overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.2);
    transition: background 0.3s ease;
}

.pg-item:hover .pg-overlay {
    background: rgba(0, 0, 0, 0);
}

/* Play Icon adjustments for PG items */
.pg-item .gallery-play-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
    z-index: 2;
    transition: all 0.3s ease;
}

.pg-item .gallery-play-icon svg {
    width: 20px;
    height: 20px;
    fill: #040b4f;
    margin-left: 3px;
}

.pg-item:hover .gallery-play-icon {
    background: #FF5722;
}

.pg-item:hover .gallery-play-icon svg {
    fill: #fff;
}

/* Responsive adjustments */
@media (max-width: 992px) {
    .pg-item {
        width: calc(33.333% - 15px);
        height: 140px;
    }
    .pg-item {
        clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%);
    }
    .pg-item:nth-child(6n+4),
    .pg-item:nth-child(6n+5),
    .pg-item:nth-child(6n+6) {
        clip-path: polygon(0% 0, 90% 0, 100% 100%, 10% 100%);
    }
}

@media (max-width: 768px) {
    .pg-item {
        width: calc(50% - 15px);
        height: 120px;
    }
    .pg-item {
        clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%);
    }
    .pg-item:nth-child(4n+3),
    .pg-item:nth-child(4n+4) {
        clip-path: polygon(0% 0, 90% 0, 100% 100%, 10% 100%);
    }
}

@media (max-width: 480px) {
    .pg-item {
        width: calc(100% - 15px);
        height: 180px;
        clip-path: polygon(5% 0, 100% 0, 95% 100%, 0% 100%) !important;
    }
}
"""

with open('c:/Users/jeeva/OneDrive/Documents/Bebright/style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)
print("CSS appended to style.css")
