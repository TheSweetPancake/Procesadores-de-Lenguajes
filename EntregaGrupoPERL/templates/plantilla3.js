// Inicializar animaciones AOS al cargar
AOS.init();

// Alternar modo oscuro/claro
const toggleBtn = document.getElementById('theme-toggle');
toggleBtn.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
  toggleBtn.textContent = document.body.classList.contains('dark-mode')
    ? "Modo Claro"
    : "Modo Oscuro";
});

// Función para togglear una sección desplegable
function toggleSection(section) {
  const content = section.querySelector('.section-content');
  if (!content) return;

  if (section.classList.contains('open')) {
    content.style.maxHeight = "0";
    section.classList.remove('open');
  } else {
    content.style.maxHeight = content.scrollHeight + "px";
    section.classList.add('open');
  }
}

// Abrir sección colapsable (si aplica)
function openCollapsibleIfNeeded(section) {
  if (!section) return;
  if (!section.classList.contains('collapsible')) return;

  const content = section.querySelector('.section-content');
  if (!content) return;

  // Abrir siempre al mostrarla
  content.style.maxHeight = content.scrollHeight + "px";
  section.classList.add('open');
}

// Cerrar sección colapsable (si aplica)
function closeCollapsibleIfNeeded(section) {
  if (!section) return;
  if (!section.classList.contains('collapsible')) return;

  const content = section.querySelector('.section-content');
  if (!content) return;

  content.style.maxHeight = "0";
  section.classList.remove('open');
}

// Mostrar solo la sección con ese id (y ocultar el resto)
function showOnlySection(targetId) {
  const allSections = document.querySelectorAll('.container .section');

  // Si es "inicio", mostramos todas
  if (targetId === 'inicio') {
    allSections.forEach(sec => {
      sec.style.display = "";
      // No forzamos a abrir/cerrar aquí: respetamos el estado actual
    });

    // Scroll arriba al contenedor
    const top = document.getElementById('inicio');
    if (top) top.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return;
  }

  // Si no es inicio, ocultamos todas menos la target
  allSections.forEach(sec => {
    if (sec.id === targetId) {
      sec.style.display = "";
      openCollapsibleIfNeeded(sec);
    } else {
      sec.style.display = "none";
      closeCollapsibleIfNeeded(sec);
    }
  });

  // Scroll a la sección visible
  const target = document.getElementById(targetId);
  if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Click en títulos de secciones colapsables
document.querySelectorAll('.collapsible h2').forEach(h2 => {
  h2.addEventListener('click', () => {
    const section = h2.parentElement;
    toggleSection(section);
  });
});

// Navegación: mostrar solo el apartado pulsado
document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const targetId = this.getAttribute('href').substring(1);
    showOnlySection(targetId);
  });
});
