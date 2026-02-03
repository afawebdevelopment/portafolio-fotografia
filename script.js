// Menú Hamburguesa
const menuToggle = document.getElementById('menuToggle');
const menu = document.getElementById('menu');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        menuToggle.classList.toggle('active');
        menu.classList.toggle('active');
    });
}

// Cerrar menú al hacer clic en un link
const menuLinks = document.querySelectorAll('.menu a');
menuLinks.forEach(link => {
    link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        menu.classList.remove('active');
    });
});

// ==================== FULLSCREEN GALLERY ====================

const galleryCards = document.querySelectorAll('.gallery-card');
const fullscreenModal = document.getElementById('fullscreenModal');
const fullscreenImg = document.getElementById('fullscreenImg');
const closeBtn = document.getElementById('closeFullscreen');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const currentPhotoSpan = document.getElementById('currentPhoto');
const totalPhotosSpan = document.getElementById('totalPhotos');

let currentPhotoIndex = 0;
const photos = [];

// Obtener todas las fotos
galleryCards.forEach((card, index) => {
    const img = card.querySelector('img');
    photos.push({
        src: img.src,
        alt: img.alt
    });
    
    // Evento click en cada card
    card.addEventListener('click', () => {
        currentPhotoIndex = index;
        openFullscreen();
    });
});

// Actualizar el total de fotos
totalPhotosSpan.textContent = photos.length;

// Abrir fullscreen
function openFullscreen() {
    const photo = photos[currentPhotoIndex];
    fullscreenImg.src = photo.src;
    fullscreenImg.alt = photo.alt;
    currentPhotoSpan.textContent = currentPhotoIndex + 1;
    fullscreenModal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Cerrar fullscreen
function closeFullscreen() {
    fullscreenModal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Navegar a la siguiente foto
function nextPhoto() {
    currentPhotoIndex = (currentPhotoIndex + 1) % photos.length;
    openFullscreen();
}

// Navegar a la foto anterior
function prevPhoto() {
    currentPhotoIndex = (currentPhotoIndex - 1 + photos.length) % photos.length;
    openFullscreen();
}

// Event listeners para los botones
closeBtn.addEventListener('click', closeFullscreen);
nextBtn.addEventListener('click', nextPhoto);
prevBtn.addEventListener('click', prevPhoto);

// Cerrar modal al hacer clic fuera de la imagen
fullscreenModal.addEventListener('click', (e) => {
    if (e.target === fullscreenModal) {
        closeFullscreen();
    }
});

// Teclas de navegación
document.addEventListener('keydown', (e) => {
    if (!fullscreenModal.classList.contains('active')) return;
    
    if (e.key === 'Escape') {
        closeFullscreen();
    } else if (e.key === 'ArrowRight') {
        nextPhoto();
    } else if (e.key === 'ArrowLeft') {
        prevPhoto();
    }
});

// ==================== SMOOTH SCROLL ====================

// Suavizar el desplazamiento al hacer clic en los links
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Cambiar navbar al hacer scroll
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.2)';
    } else {
        header.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.1)';
    }
});

console.log('Script de portafolio de Ana Cristina cargado correctamente');
