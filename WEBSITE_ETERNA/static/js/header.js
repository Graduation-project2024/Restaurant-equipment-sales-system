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

        // Handle touch events for mobile
        document.addEventListener('touchstart', function(event) {
            if (isDropdownOpen && !userDropdown.contains(event.target)) {
                hideDropdown();
            }
        });

        // Add hover functionality
        userDropdown.addEventListener('mouseenter', function() {
            showDropdown();
        });

        userDropdown.addEventListener('mouseleave', function(event) {
            // Check if the mouse is moving to the dropdown menu
            const rect = dropdownMenu.getBoundingClientRect();
            if (
                event.clientX < rect.left ||
                event.clientX > rect.right ||
                event.clientY < rect.top - 10 || // Add some tolerance
                event.clientY > rect.bottom
            ) {
                hideDropdown();
            }
        });

        dropdownMenu.addEventListener('mouseleave', function() {
            hideDropdown();
        });
    }
});
