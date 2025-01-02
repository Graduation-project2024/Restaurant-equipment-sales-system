function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

document.addEventListener('DOMContentLoaded', function() {
    const userDropdown = document.getElementById('userDropdown');
    const dropdownMenu = document.getElementById('dropdownMenu');

    if (userDropdown && dropdownMenu) {
        let isDropdownOpen = false;

        function showDropdown() {
            dropdownMenu.style.opacity = '1';
            dropdownMenu.style.visibility = 'visible';
            dropdownMenu.style.transform = 'translateY(0)';
            isDropdownOpen = true;
        }

        function hideDropdown() {
            dropdownMenu.style.opacity = '0';
            dropdownMenu.style.visibility = 'hidden';
            dropdownMenu.style.transform = 'translateY(-10px)';
            isDropdownOpen = false;
        }

        // Toggle dropdown on click
        userDropdown.addEventListener('click', function(event) {
            event.stopPropagation();
            if (isDropdownOpen) {
                hideDropdown();
            } else {
                showDropdown();
            }
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            if (isDropdownOpen && !userDropdown.contains(event.target)) {
                hideDropdown();
            }
        });

        // Prevent dropdown from closing when clicking inside it
        dropdownMenu.addEventListener('click', function(event) {
            event.stopPropagation();
        });

        // Close dropdown when pressing Escape key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && isDropdownOpen) {
                hideDropdown();
            }
        });
    }
});
