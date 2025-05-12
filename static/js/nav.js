
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.querySelector('.md\\:hidden');
    const mobileMenu = document.createElement('div');
    mobileMenu.className = 'mobile-menu hidden bg-gray-800 w-full absolute top-16 left-0 p-4';
    mobileMenu.innerHTML = `
        <a href="/" class="block text-white hover:text-gray-300 py-2">Home</a>
        <a href="/about" class="block text-white hover:text-gray-300 py-2">About</a>
        <a href="/contact" class="block text-white hover:text-gray-300 py-2">Contact</a>
    `;
    
    document.querySelector('nav').appendChild(mobileMenu);
    
    mobileMenuButton.addEventListener('click', function() {
        mobileMenu.classList.toggle('hidden');
    });
});
